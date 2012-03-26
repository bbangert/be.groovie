A Mason component to fill-in error messages
===========================================

How often have you seen those sites with a form, and after you miss a
field, it pops up a little message in red under the text box indicating
what went wrong? I'm guessing a lot, and when writing web applications
this can be a pain to code in.

Typically in Perl/PHP, you'd add this by going through your form, adding
little bits of code under each and every form element to display the
error on invalid input. I quickly got tired of this, and decided to
simplify the process.

In examining
`HTML::FillInForm <http://search.cpan.org/~tjmather/HTML-FillInForm-1.04/lib/HTML/FillInForm.pm>`_,
I noticed I needed a slightly different tool to easily parse the HTML
form. After a little bit of shopping about, I decided on
`HTML::Parser <http://search.cpan.org/~gaas/HTML-Parser-3.36/Parser.pm>`_
to do the heavy lifting. Here's a snippet from a Mason page using my
error\_fill.mas component to toss in the error messages:

::


    % if ($form_status eq 'errors') {
    <&| /lib/error_fill.mas, errors => $errors_hash_ref &>
    <p style="color: red; font-weight:bold;">Errors Found: Please correct the fields indicated.
    <& /forms/myform.mas, %ARGS &>
    </&>
    % } else {
    <& /forms/myform.mas, %ARGS &>
    % }

$errors\_hash\_ref is a hash ref that is keyed by the form field name,
with the value set to the error message you want displayed. Right now,
error\_fill.mas does not have custom pre/post-fix variables for you to
tweak how the error message is inserted. It currently puts a <br>
followed by a red span element containing your message.

myform.mas is the form I want to display, I prefer to split sections out
in Mason to keep my web application modular and the sections of my pages
more reusable.

Here's error\_fill.mas:

::

    $errors%args>$errors is a hash reference keyed as:
                'field name' > 'Error message'
        use HTML::Parser;my $form = $m->content;

        my $p = HTML::Parser->new(api_version > 3);$p->handler(default => sub { print _ }, "text");
    $p->handler(end => sub {
                  my ($tagname, $text, $attr) = _;
                  if (($tagname eq ‘select') && (exists $errors->{$attr->{name}})) {
                    print $text;
                    print ‘’;
                    foreach my $err (@{$errors->{$attr->{name}}}) {
                      print ‘’.$err;
                    }
                    print ‘’;

                  } else {
                    print $text;
                  }
                },
                “tagname, text, attr”);
    $p->handler(start => sub {
                  my ($tagname, $text, $attr) = _;
                  if (($tagname eq 'input') && (exists $errors->{$attr->{name}})) {
                    print $text;
                    print '<span style="color:red;">';
                    foreach my $err ({$errors->{$attr->{name}}}) {
                      print ‘’.$err;
                    }
                    print ”;

                  } else {
                    print $text;
                  }
                },
                “tagname, text, attr”);
    $p->parse($form);
    %init>

Hopefully this will help some people out.


.. author:: default
.. categories:: Perl, Code
.. comments::
   :url: http://be.groovie.org/post/296355100/a-mason-component-to-fill-in-error-messages
Emulating Ruby's anonymous blocks with Myghty
=============================================

Ruby's anonymous block capability is probably the main feature I find
myself wishing Python had on more than one occasion. While the upcoming
Python 2.5 `PEP 323 <http://www.python.org/peps/pep-0343.html>`_
provides for the “with” statement which will enhance generators to get a
bit closer. Though as `Ryan Tomayko
notes <http://lesscode.org/2005/07/12/ruby-colored-blocks-in-python/>`_,
this still doesn't make the block available within the “generator”.

There are of course, many uses for having the block (with its closure
scope), available in the function/generator you're using. I've seen this
used to easily register code call-backs with a CleanUp/Initializaiton
manager, and other cases where its preferable to actually retain the
block in its entirety for later execution. It's also very useful when
you want the function to control execution of the block, and return its
output in a modified form.

In these ways, it would appear that the generator enhancements won't
quite be bringing the full power of Ruby anonymous blocks to Python.
However, I recently found out that a relatively recent feature in my
favorite Python template language, `Myghty <http://www.myghty.org/>`_,
implements something quite close to this.

Myghty's Component Calls with Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In a `previous entry on Formencode and
SQLObject <http://groovie.org/articles/2005/12/14/handling-form-data-w-formencode-sqlobject-redux>`_
I noted how useful the component call with content can be. What I failed
to note (I didn't know at the time as well), was that not only is the
function/component able to get the content of the content “block”, but
its also able to execute it again and again.

Consider this example from my prior entry:

::

    Hi, lets translate the content under:
    <&| MODULE:mylib:translate, lang='es' &>
        This entire block of content will be sent in as a 
        single variable to translate.myt
        for use. This includes any <b>HTML tags and such</b> as well.
    </&>

and the function it calls:

::

    from mytranslater import translated

        def translate(m, lang):
        body = “The translated text is:“
        body += translated(lang, m.content())
        m.write(body)

The ``m.content()`` call can be called as many times as you want the
output of it, and it retains the scope of its original location. This in
many ways emulates how Ruby can yield to the block and capture its
output, however it is not possible to stash the block itself (in
Myghty/Python).

Next up is to actually be able to use values from the function inside
the block. In Ruby this is done in a very elegant fashion letting you
declare what you'll call them, then use them, like so:

::

    SomelistOfints.each do |item|
        item += 2
    end

To emulate this behavior, our block has to make a special function call
and know the name of the value in advance. Here's an example:

::

    % randomvar = 423
    <&| MODULE:mylib:translate, lang='es' &>
        This entire block of content will be sent in 
        as a single variable to translate.myt for use. 
        This includes any <b>HTML tags and such</b> as
        well. Here's something supplied by
        translate: <% m.content_args['value'] %>.
        Of course, <% randomvar %> is still in scope too.
    </&>

And just for fun, our translate function will call the block with some
different values:

::

    def translate(m, lang):
        body = "<p>The translated and repeated text is:</p>"
        for val in range(0,4):
            body += m.content(value=val)
        body += "<p>That's it, nothing else.</p>"
        m.write(body)

The important thing to remember that makes the concept powerful is that
the block above is called in the scope you saw it in the template.
Whatever variables were available there are used as normal.

Close…
^^^^^^

This method brings us close to Ruby's anonymous blocks, as close as
might be possible in Python. Unfortunately its only usable within Myghty
(if not, please let me know), and its still not true anonymous blocks.
At the very least, its close enough to make me happy for now. While I
could just switch to Ruby entirely, there's still way too many things
about Python that I'd miss.

From the details of PEP 343, it appears that this full capability to
pass the block in was purposely avoided as having flow control in the
“macro” makes the code inscrutable. Hopefully someday the utility and
power such functionality provides will result in it being available in
Python. Or at the very least, some clever person can try a variant in
PyPy and see what sticks.

And yes, I know nested functions can be used and passed around with
their closure, but its pretty annoying to be nesting functions back and
forth solely for that purpose. It feels like all we have is a hammer…

**Further reference:**

`Myghty docs on Component-Call-With-Content
Arguments <http://www.myghty.org/docs/components.myt#components_callwithcontent_ccallcontent_args>`_


.. author:: default
.. categories:: Code, Myghty, Python, Ruby
.. comments::
   :url: http://be.groovie.org/post/296346524/emulating-rubys-anonymous-blocks-with-myghty
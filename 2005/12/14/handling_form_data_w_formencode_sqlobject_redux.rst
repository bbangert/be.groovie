Handling Form data w/Formencode+SQLObject Redux
===============================================

In a `prior post on handling form
data <http://groovie.org/articles/2005/08/24/handling-form-data-with-formencode-sqlobject>`_
I covered how to easily populate a form using FormEncode/SQLObject and
validate/save the data.

One of the things I noted was that I had to take the HTML form output
first, and use htmlfill with it to populate it with defaults and errors
before displaying. This required some extra lines I wasn't to thrilled
with in the controller. After an evening of chatting with `Ian
Bicking <http://blog.ianbicking.org/>`_ about whether FormEncode could
somehow be cleaned up to make this easier, Ian suggested I use a
`Myghty <http://www.myghty.org/>`_ feature I had forgotten about.

Component Calling with Content blocks in Myghty
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Somewhat ironic since I use Myghty all day and Ian doesn't (afaik). It's
a very useful feature called `Component Calls with
Content <http://www.myghty.org/docs/components.myt#components_callwithcontent>`_.
It's probably easiest to understand the cool ability this provides by
seeing it. In Myghty, each template is known as a component, and complex
arrangements can easily be put together by component inheritance and
component calls between them.

Normal Python function calls and expressions in a Myghty component
(template) looks like this:

::

    Hi everyone, 2 + 2 = <% 2+2 %> and your name is <% lookup_name() %>
    </pre>

        To include content from other components, you can either call the component through the function call m.comp('/some/template.myt') or you can use the component call syntax:


    Hi everyone
      <& /sidebar.myt &>

So here's how we will use a component call with content:

::

    Hi, lets translate the content under:
    <&| /translate.myt, lang='es' &>
        This entire block of content will be sent in as a single variable to translate.myt
        for use. This includes any <b>HTML tags and such</b> as well.
    </&>

And the ``translate.myt`` template might look like:

::

    The translated text is:

        

        lang%args>from mytranslater import translatedcontent = m.content()%init>

This is probably a lot to absorb, as it utilizes a few different Myghty
concepts. Components can have arguments they expect, here the
``translate.myt`` component expects a lang arg which is passed in. The
content block is then available as ``m.content()`` inside the template.
The ``<%init>`` block is called first and variables defined there are
available inside the template.

So how does this help us with the original problem?

Module Components
^^^^^^^^^^^^^^^^^

So far, all of these abilities are possible in Myghty's ancestor, Mason.
One more powerful construct available in Myghty however is the ability
to not only call components, but `Module
Components <http://www.myghty.org/docs/modulecomponents.myt#modulecomponents_templates>`_.

I've been familiar with these for awhile as I use them for Controllers.
It had never occurred to me though, that they can call any function in a
module as if it was a component, not just ‘Controllers'.

Module components allow you to do a variety of interesting things,
mainly, calling functions, classes, or objects that are in Python
modules. Let's take a look at the last ``translate.myt`` example using
this approach instead.

::

    Hi, lets translate the content under:
    <&| MODULE:mylib:translate, lang='es' &>
        This entire block of content will be sent in as a single variable to translate.myt
        for use. This includes any <b>HTML tags and such</b> as well.
    </&>

And the ``mylib`` Python module (assumed to be in the search path):

::

    from mytranslater import translated

        def translate(m, lang):
        body = “The translated text is:“
        body += translated(lang, m.content())
        m.write(body)

Myghty will examine the function signature to determine what variables
it wants and will search the current scope to make sure they're passed
in. Very handy. :)

Putting it All Together
^^^^^^^^^^^^^^^^^^^^^^^

So let's see how this helps us out, first, rather than having to take
the form and render it in the controller, we'll push this into the
template using a component call with content. So our new ``myform.myt``
looks like:

::

        myform.myt
        basic formUsername: Age: &>



.. author:: default
.. categories:: Python, Code, Myghty
.. comments::
   :url: http://be.groovie.org/post/296346712/handling-form-data-w-formencode-sqlobject-redux
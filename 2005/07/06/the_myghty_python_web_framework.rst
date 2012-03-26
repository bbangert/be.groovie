The Myghty Python Web Framework
===============================

`Myghty <http://www.myghty.org/>`_ is a powerful web application
framework that builds on the strengths of Perl's
`Mason <http://www.masonhq.com/>`_ using my favorite language,
`Python <http://www.python.org/>`_. While Myghty also handles page
templating, it has some very powerful features that make it a full
fledged framework in my opinion.

Wondering if Myghty is something you should check out?

I would highly recommend looking into Myghty if you're looking for any
of the following:

-  Clean, unobtrusive `templating
   language <http://www.myghty.org/docs/embedding.myt>`_ for integrating
   Python data and HTML
-  An easy way to write pages that
   `inherit <http://www.myghty.org/docs/inheritance.myt>`_ their
   look/feel without needing .include statements
-  Re-usable code that you can carry from one project to the next
-  `MVC programming
   paradigm <http://www.myghty.org/docs/modulecomponents.myt>`_ , or
   page-driven paradigm (Myghty doesn't care, it can be anywhere in
   between as well)
-  `Advanced caching ability <http://www.myghty.org/docs/cache.myt>`_,
   tunable to just the time intensive sections of a page
-  Run as `WSGI, FCGI, SCGI, mod\_python, or
   stand-alone <http://www.myghty.org/docs/configuration.myt>`_ with
   hardly a single change to your code (to switch between them)
-  Architecture that scales, from a single developer's personal project,
   to a multi-developer's company website

History
-------

Myghty first came into existence a little over a year ago when Mike
Bayer looked around at the Python web application frameworks and
couldn't find one that really sucked him in. Having used
`Mason <http://www.masonhq.com/>`_ for various projects, but not finding
anything as elegant as it for Python he decided to port Mason to Python.

This ported code was based on the Perl code almost line by line,
resulting in a Python web application framework that worked almost
exactly like Mason, except with Python as the base language. It wasn't
very long before Mike started adding to Myghty, such as Module
Components, and threaded features not found in Mason.

Terms Used
----------

**MVC** – Model, View, Controller paradigm is typically used to describe
an approach that separates the code in these 3 steps rather than mingle
them all in one place. Model usually refers to the database and its
abstraction, the Controller handles the logic of dealing with the
request, getting the data from the Model, and passing it to the View for
display to the user.

**Component** – A component in Mason is what a template is known as. A
template might display a full web-page, just one small section, or send
data to other components. Components typically correspond to files on a
filesystem, and appear as normal HTML pages with a few lines of Python
in them, although they're far from normal HTML pages…

**Resolver** – Used to describe the process of determining what to do
with a given URL. Myghty has some incredible flexibility here.

Distinctive Features
--------------------

Module Components
~~~~~~~~~~~~~~~~~

In Python, your modules contain all your Python code. In Myghty, the
Component contains a mixture of Python with HTML. To handle a MVC
approach to development, Myghty has Module Components. These are a cross
of a Myghty Component with a Python Module, that leaves you with a
fairly normal Python Module. It's called directly from Myghty in a
similar way to how Myghty would call a Component. These Module
Components can be explicitly defined in the configuration, or called
implicitly.

The Module Component allows you to directly handle URL's, and respond
from within the Module by sending data back to the client or processing
data then sending it on to a normal Component for processing. Module
Components work within the Resolving process, and have control passed to
them according to a `configuration
mapping <http://www.myghty.org/docs/modulecomponents.myt#modulecomponents_resolution>`_
. The mapping uses regular expressions to match URL's to modules that
contain the method to be called, like so:

::

    module_components = [
        {r'myapplication/home/.*' : 'myapp.home:HomeHandler'}, 
        {r'myapplication/login/.*' : 'myapp.login:LoginHandler'}, 
        {r'.*/cart' : 'myapp.cart:process_cart'}, 
        {r'.*' : 'myapp.home:HomeHandler'} 
    ]

This would map the URL ``http://yourapp/myapplication/home/blah`` to the
HomeHandler component class, in the home module file, under the myapp
package. The method in the HomeHandler class called can be done in two
different ways, implicitly, or explicitly. For more details on this,
read the `Myghty docs on Module
Components <http://www.myghty.org/docs/modulecomponents.myt>`_

While other frameworks implement an MVC approach, Myghty's goes a step
farther by letting you tie it into the resolution options used by the
Resolver, and even use your own resolvers…

Advanced Resolver
~~~~~~~~~~~~~~~~~

In version 0.97alpha2 (maybe a better naming scheme could be used? :)
the resolver implementation was heavily rewritten to allow massive
flexibility in how a URL is handled. When Myghty handles a request, it
goes through a fairly complex process to determine what to do with it.
This is called the default strategy:

#. **Translate the URL against the path translation options** – This can
   act as an internal URL rewriting scheme, changing a URL to be handled
   differently
#. **Resolve a dhandler** – This rule matches conditionally. It is only
   called if the rules under it don't find a match, it then strips off
   part of the URL its looking for and adds dhandler. So a search for
   /article/view/38 becomes a search for /article/view/dhandler if 38
   isn't found. `Read more about
   dhandlers <http://www.myghty.org/docs/specialtempl.myt#specialtempl_dhandler>`_
#. **Check the URI Cache** – The URI cache is searched for the incoming
   URI at this point, to see if a component has matched it before. This
   rule is also executed on a conditional basis.
#. **Upwards Search** – The 3rd conditional rule of the bunch, this rule
   is called during inheritance when a component searches parent paths
   for an autohandler. `Read more about
   autohandlers <http://www.myghty.org/docs/specialtempl.myt#specialtempl_autohandler>`_
#. **Resolve a Module** – Matches a Module Component to the incoming
   URI.
#. **Resolve a File** – Matches a file under the component roots
   specified for a match to the incoming URI. This will directly call a
   Myghty template file on the system in response to a URL.

As soon as any of the non-conditional rules matches, the file or module
component method is served up. Myghty gets an additional speed boost by
keeping compiled versions of all your template files around, so that
they're only compiled the first time they're called. By using the basic
Python way of compiling the templates as .pyc files, it also ensures
that they're re-compiled the second you update one of them. This way
you're always sure you're viewing the latest update of your template.

So where's the real power in all this?

These are just the **default** rules. They can be completely, and
utterly customized. You can switch the order around, you can remove
resolver rules entirely, **and you can even write your very own resolver
rules**.

Maybe you've decided you want to serve some of the components from a
database instead of the file system. You could write a custom resolver
rule that does just that, and loads the entire component from the
database as well. You could write your own version of the Path Translate
module to get its rewrite rules from a database table. As if this wasn't
powerful enough, Myghty also lets you have **different resolver
strategies for different contexts**.

Conclusion
----------

Myghty is a very powerful web framework. It has features that go beyond
any pure “templating” language I've encountered. If you're not quite
happy with what you're using right now, or something I described above
makes you giddy with thoughts of power, maybe its time to take Myghty
for a test drive.

In future posts, I'll describe more of the features I use daily in
Myghty, and share code tidbits that let you get complex tasks done
easily.


.. author:: default
.. categories:: Python, Code, Myghty
.. comments::
   :url: http://be.groovie.org/post/296354976/the-myghty-python-web-framework
Ingredients to the Pylons Python Web Framework
==============================================

As the date edges closer to a `Pylons <http://pylonshq.com/>`_ release,
I find myself already thinking about future directions of Pylons. I'm
obviously rather biased when discussing Pylons as I'm one of its
creators, though I still find that thought humorous as the vast vast
majority of the code that resulted in an excellent framework is not
actually in Pylons, nor did James Gardner (the other Pylons dev) and
myself write it.

Matt mentions in a `blog entry on Python Web frameworks, maybe its just
too
easy <http://panela.blog-city.com/python_web_framework_rewrite_take_two.htm>`_
to write a Python web framework. I didn't originally see myself writing
a framework as such, but it became a fairly logical conclusion to the
work I was doing at the time and the framework was originally extracted
(like many others) from a large production application. It really is
quite easy to write a web framework, and there's tools available that
make it even easier.

`WSGI <http://www.python.org/peps/pep-0333.html>`_ has changed the point
at which re-usability is possible in a Python web framework as well, the
only possible result I see in the future is more frameworks (Not in the
way people think though). Many would argue this is “bad”, however I
think due to the different point in re-use made possible by WSGI there
will actually be more collaboration and less web developer divisions
despite how many ‘frameworks' are out there (once they're more WSGI-ish
that is). Consider this analogous in some ways to how many linux
distributions are out there, and the fact that people can switch between
them very easily.

So what went into building Pylons?

The Basics
^^^^^^^^^^

First, there's a few things you're going to need in even the most basic
web framework:

-  Dispatcher
-  Request API/Object

That's really the utter basics, and there's frameworks that don't do
much more than this. Obviously many people are going to want more…. like
sessions. The question that WSGI raises is why lock a session interface
to a framework, when it can be re-used as WSGI middleware? While the
term “WSGI Middleware” can be rather intimidating, I `previously covered
why WSGI is actually quite
easy <http://groovie.org/articles/2005/10/06/wsgi-and-wsgi-middleware-is-easy>`_
despite the sometimes scary or just annoying term. It's something to be
reckoned with, and there's no excuse not to get familiar with it if
you're doing web development in Python.

As I needed something rather reliable and sturdy, I went with
`Myghty's <http://www.myghty.org/>`_ session and request API. For
dispatching, I used a custom resolver utilizing
`Routes <http://routes.groovie.org/>`_ that dispatches to a controller
and action (controller method). This results in a fairly MVC'ish style
web architecture that's rather extensible.

So check those off the above list plus sessions:

-  Dispatch – `Routes <http://routes.groovie.org/>`_ based
-  Request API – Myghty's `HTTP request
   object <http://www.myghty.org/docs/globals.myt#globals_globalr>`_
-  Sessions – Myghty's `session
   interface <http://www.myghty.org/docs/session.myt#session>`_, which
   is also now available as WSGI middleware

At this point, we'd have a framework that can interpret a URL, setup an
easy to use request object, and call your controller. Your controller
would also be able to save data using sessions. We'd have a bit of a
problem distributing such a framework though, as it probably wouldn't be
very convenient to setup and install.

In the case of Pylons, so far it means I've written just a `class to
handle
dispatch <http://pylonshq.com/docs/0.8/module-pylons.myghtyroutes.html>`_,
locating the controllers (actually, Routes will do this), and calling
them. A measly hundred or so lines of Python code.

Defaults, Structure Creation, Stand-alone Server
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

What really helps people get started quickly with a framework is if its
easy to install, creates a basic structure of a working web application
for them to get started with, and some way to run it. So our new
additions:

-  Web Framework Installer
-  Template for starter Web Application
-  Stand-alone Server

This can quickly be a fairly substantial amount of code to write,
especially if you want cross-platform installation, and a system that
also runs on multiple platforms. Not a problem though,
`Paste <http://pythonpaste.org/>`_ quickly makes the last two of these
quite easy, and
`setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_
handles installing your framework and any requirements it may have. I
should note that setuptools isn't perfect, but it sure beats asking
users to go to a half dozen sites and install various packages.

Paste is divided into 3 parts, though it can be tricky to see the
relation between them. The core part of Paste contains wsgi middleware
parts that will likely appeal to many, and some other basic request
handling functionality. PasteScript contains the structure creation bit
used in Pylons that generates the starting template. There's also
PasteDeploy which comes in useful later when deploying and running web
applications made with a framework using it.

We're looking at a decent little framework so far, now that we can
install it, quickly start a new project, and run it. What's next?

Templating and Object-Relational Mappers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Some frameworks, typically known as “full-stack” frameworks try and make
more choices for you. They aim to fill your needs top-to-bottom, or at
least their vision of your needs. While SQLObject is a very popular ORM,
it seemed that good use of a layout and basic Python import statements
would make using any ORM just as easy.

In Pylons, a models directory is provided, with some commented out
suggestions for how you'd go about setting up an ORM. There's hooks
provided in the base application module that's imported by all your
controllers, so its easy to define your ORM classes and use them in your
controllers.

One of the other objectives for Pylons was to try and be very
‘Pythonic'. That is, it should re-use as much of a developers Python
knowledge as possible. This is used by default for templating since
Myghty uses normal Python syntax for its templates in addition to
providing powerful caching functionality and great re-use through
components.

Not wanting to force anyone into something they couldn't stand (template
languages can be a love-hate thing), we also implemented the `TurboGears
Template Engines <http://turbogears.org/docs/plugins/template.html>`_
plug-in functionality. This made it very easy to let people use the
template language of their choice, in a fairly uniform manner. It was
also pretty minimal to `implement the template language
renderer <http://pylonshq.com/docs/0.8/class-pylons.util.Buffet.html>`_
as the `Buffet project <http://projects.dowski.com/projects/buffet>`_
provided a great head-start.

Our new list is looking rather complete for a “full-stack” framework:

-  Web Framework Installer
-  Template for starter Web Application
-  Stand-alone Server
-  Dispatcher
-  Request API/Object
-  Sessions
-  Templating
-  Database Integration

Making the most of Middleware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This is one of the areas where Pylons was able to make some great leaps,
with very little actual code. In several areas, thanks to the use of
middleware, Pylons is able to offer features other frameworks are still
working on.

To start off with, there's the excellent EvalException middleware which
provides an `AJAXy exception
catching <http://blog.ianbicking.org/ajaxy-exception-catching.html>`_
system I have yet to see in any other framework. We've formatted it
slightly to fit in nicely with Pylons, and it works like a charm.
Extremely useful for those times when you want to `interactively
debug <http://pylonshq.com/docs/0.8/interactive_debugger.html>`_ a web
application to see what's what, and it's a lot quicker than putting
``print`` statements all over.

Another important bit, that a lot of frameworks skimp on is unit
testing. Using Paste's fixture middleware, its easy to `test your web
application <http://pythonpaste.org/testing-applications.html>`_. Pylons
`adds a few objects to the response you can test
with <http://pylonshq.com/docs/0.8/testing_web_application.html>`_, so
you can ensure that the session was setup properly, the right template
components were called with the right arguments, etc. In the future
we'll likely add some defaults to make using
`twill <http://www.idyll.org/~t/www-tools/twill/>`_ an easy option.

The best thing about all of this of course, is that these useful parts
can be integrated seamlessly and re-used by other frameworks.

Taking the framework out of Framework
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Given how most of these parts are definitely not unique to Pylons, nor
are they intended to be, it shouldn't be long until more frameworks
start using the great modularity that Pylons is utilizing. A lot of
these parts will likely become standardized to an extent, so that
there's even less barrier to switching frameworks.

At this point, Pylons becomes less of a “framework” in one sense, and
more a set of defaults and structure for how a Python web application
should be put together. Pylons has more features of course that I
haven't described, the `WebHelpers <http://pylonshq.com/WebHelpers/>`_
functions are made easily available for use in templates, more Paste
middleware is used for slick traceback email's when you're in production
mode, PasteDeploy makes running your Pylons webapp easy in a variety of
situations, etc.

It's a very easy-to-extend model, with little need to put great amounts
of application-y type stuff into the framework itself. It also keeps its
components separate for easier testing, out of the actual framework.
This means that while Pylons comes with a great set of middleware and
parts set up for you, its very easy to swap in your preferred template
language, your preferred ORM, a different exception handler, etc. The
choice is up to you, but the defaults are set to a good starting point
(also called “convention over configuration”).

Upping the Re-usability Ante
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Increasing re-usability is what I'd consider the future for Python Web
Development. With WSGI middleware driving re-usability, such concepts
that “to use Feature X, you must use your Framework Y” just doesn't
apply. Unifying development work on excellent components that can be
re-used in any WSGI-compatible framework makes Python Web Development
better.

Pylons isn't alone in aiming for this style of framework, Ian Bicking is
working on a project that starts the opposite direction, with just a
layout and you add sessions, templating, etc. as you need it. TurboGears
is adding more Paste-compatible features that will shortly make it
trivial for them to add in the EvalException middleware (assuming they
haven't already, I haven't checked lately) and other great components.
Different frameworks have different levels of re-usability, those that
are built with re-usability in mind at the beginning will likely be able
to adapt quicker to new demands and requirements, and take maximum
advantage of the great middleware being created.

While having more people use Pylons would be great, it isn't necessary
for Pylons to become a better framework. Having more people use the
WebHelpers package, or make their framework Paste-compatible, or use
Routes, or Myghty's powerful caching/session API's all helps Pylons. It
also helps any other framework using these components, and that's what
counts the most.

Here's the final tally of Pylons features and where they came from:

-  Web Framework Installer – setuptools
-  Template for starter Web Application – PasteScript
-  Stand-alone Server – Paste
-  Dispatcher – Routes / Myghty
-  Request API/Object – Myghty
-  Sessions – Myghty
-  Caching – Myghty
-  Templating – Myghty, or any that support the TurboGears Template
   Plug-In
-  Helper functions/AJAX – WebHelpers
-  JSON – simplejson + Pylons decorator
-  Global “convenience” objects – Pylons
-  Database Integration – SQLObject, SQLAlchemy, anything else
-  Interactive Debugging – Paste
-  Traceback E-mails – Paste
-  Webapp Unit Testing – Paste
-  Webapp Deployment – PasteDeploy
-  Webapp Distribution/Installation – setuptools

This is just the default set-up, its trivial to add more middleware,
which would make this list very, very long and includes such things as
OpenID Authentication, authenticated session tickets, along with other
great stuff.

The Pylons Code-base:
`Pylons Module
Reference <http://pylonshq.com/docs/0.8/module-index.html>`_


.. author:: default
.. categories:: Python, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296346453/ingredients-to-the-pylons-python-web-framework
WSGI Framework Components and other thoughts on WSGI
====================================================

In light of Phillip Eby's recent `post concerning WSGI Middleware as
harmful <http://dirtsimple.org/2007/02/wsgi-middleware-considered-harmful.html>`_,
I've had more than a few thoughts on the issue. None of them are all
that new, but given the post I think its useful to get some of them out
there.

First, I agree 100% with PJE's post. The issue it raises results in two
lines of thought. Without a doubt these objects using the WSGI
specification should not be called **WSGI Middleware** or **WSGI
Applications**. This means that either:
1) People should stop using the WSGI spec for non WSGI
application/middleware objects.

Or…
2) WSGI needs new terminology for this application of the specification,
and should not be muddling up the WSGI middleware/application
definitions and environ namespace with meta-framework API's.

To answer either of these possibilities it helps to evaluate why things
are developing like this right now, and almost all of it comes down to
one thing… **tool developers are incredibly picky and opinionated**.

To avoid further muddling up WSGI definitions, I'll be using the
following term:

**WSGI Framework Component (WFC)** – A WSGI specification based
component that acts possibly as either a WSGI application or WSGI
middleware, or some mix of both. Example, a WFC that ensures users are
logged in before accessing your WSGI application (thus acting as WSGI
middleware), but will render its own form and go through its own login
procedure should they need to login (thus acting like a WSGI
application). This is referred to as a WFC because using WSGI is seen as
a way to avoid binding it to a specific framework, while its clear that
an application using it actually requires it to be there to operate
(thus its not WSGI middleware).

Dealing with Disagreement the WSGI Way
--------------------------------------

WSGI makes it a lot easier to disagree, yet still harness the code and
development efforts of those that disagreed with you. WFC's allow
re-usable code that isn't utterly dependent on your framework of choice
as long as its WSGI compatible. Thus the fact that many frameworks are
WSGI compatible at various levels makes it very enticing to build
re-usable components at the WSGI level instead of using framework-bound
API's.

A thought that started cropping up, and hitting the Web-SIG mail list,
and which I believe one target of Phillip Eby's post, regards putting
‘standard' keys into the WSGI environ for applications to utilize. This
would to an extent allow you to swap WFC's that do similar things, but
in different ways. Maybe you want to swap two resolving middleware, so
you use the `wsgi.org routing
spec <http://wsgi.org/wsgi/Specifications/routing_args>`_ to determine
how the URL was resolved then dispatch appropriately. You can now swap
WFC's that do routing to an extent since there's a further specification
in place.

There are other wsgi.org specifications underway, and lots of `various
WFC's being developed <http://wsgi.org/wsgi/Middleware_and_Utilities>`_.
If I'm using Pylons, and someone using CleverHarold or some other WSGI
type application makes a WFC that does something cool, I can use it as
is without having to agree with the design of their application of WSGI
based framework.

Compare that to a CherryPy2 filter, CherryPy3 tool, or Django
middleware. To use any of those, I need to use the whole framework. For
CherryPy, this may not be the case in the future should it allow a
CherryPy tool to act in the middle like middleware. Robert Brewer has
said in the past he wants CherryPy to be the end-point and not continue
dispatching elsewhere which would rule out its use as a library for a
WFC. Thus, I'm labeling CherryPy as a framework in the context of WFC
creation, while `Paste <http://pythonpaste.org/>`_ and
`Yaro <http://lukearno.com/projects/yaro/>`_ are libraries usable both
in WSGI apps/middleware and in WFC's (Note that CherryPy3 is almost
capable of being used as a WFC, except it can only dispatch to non-CP3
WSGI apps).

Going Overboard with WFC's and WSGI
-----------------------------------

The other aspect to these new WFC's that I think Phillip hit on the
head, is that there's quite a few being pushed into this layer that
really don't belong there. No one has put out a solid checklist to know
when something should be in a library, a plugin API (possibly using
`setuptools
entrypoints <http://peak.telecommunity.com/DevCenter/setuptools#extensible-applications-and-frameworks>`_
like the `TG Template Plugin
API <http://docs.turbogears.org/1.0/TemplatePlugins>`_), actual WSGI
middleware, or a WFC. As a result, there are WFC's that do very little,
and in some cases have no reason to be operating at the WSGI layer.

So, I'm going to propose some guidelines, a rough draft as I'm sure
there'll be plenty of useful feedback, on when something should be
considered for a WFC and when it should be a library. It's also useful
to note that libraries can operate on things from WSGI, vs WFC's which
get plugged into a framework/app as if it was WSGI middleware.

The guidelines for WFC's should roughly follow the same guidelines you'd
want for any WSGI middleware. There's some conditions that make it more
obvious than others on where some functionality belongs and of course
there's always exceptions to the rules.

Signs some code would be a good candidate for a WFC (It's assumed that
if you're thinking of making a WFC, you will be wrapping your actual
‘application' with it):

-  A set of operations needs to always occur before and after the
   application is called, and requires knowledge of the incoming **and**
   outgoing headers
-  Modifications are done to the HTTP headers and/or content being
   returned to the client (cookies, HTTP caching, content
   transformation)
-  The application may not be called at all (authentication,
   authorization, conditional dispatching)

Note that the first condition doesn't apply to functionality that merely
requires something to setup. It's overkill using WSGI just to run a
function at the start of every request — even if it needs environ —
there's no reason you couldn't just put the function call in your app,
call it every request, and put the function in its own module/package
(thus easy to re-use).

A lot of the Paste functions operate like this, and many of them just
take the environ as their call giving you a nice API without requiring a
WFC (which Phillip Eby advocates as well):

::

        request = paste.wsgiwrapper.WSGIRequest(environ)
        print request.cookies, request.path_info

There's no reason a variety of WFC's I see `on the WSGI middleware and
utils list <http://wsgi.org/wsgi/Middleware_and_Utilities>`_ couldn't
operate like this as well. Take
`wsgiakismet <http://cheeseshop.python.org/pypi/wsgiakismet/>`_ for
example, which parses the form submission and screens it against
Akismet. The example as a WFC actually looks more involved than I could
see a library based version looking:

::

        theoretical library version of wsgiakismet
        from akismetverify import verify_akismet

        def app(environ, start_response):
        # Wordpress API Key and website name are required arguments
        usersub = verify_akismet(key='3489012ab121', site='http://blog.example.com/', environ)
        start_response('200 OK', [('Content-type', 'text/plain')])
        return ['Comment is %s' % usersub['comment'][0]]

Note that using it like this as a function that takes environ and the
other 2 keys actually makes it easier to use than the original sample
requiring you to import cgi and re-parse the form vars.

So some good ways to know you might be on the wrong track with a WFC:

-  Only a few things are being done on setup, and stuffed into environ
-  Some environ keys are manipulated
-  Your code never alters or does anything with the status codes,
   headers, or content
-  … or none of the conditions to know when it should be a WFC exist

I'm sure there's more criteria I've missed, and it'd be great to have a
page possibly on wsgi.org regarding design decisions to hopefully avoid
having anymore functionality pushed into the WSGI layer when there's
**no good reason for it**.


.. author:: default
.. categories:: Python
.. comments::
   :url: http://be.groovie.org/post/296345940/wsgi-framework-components-and-other-thoughts-on-wsgi
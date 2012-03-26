WSGI and WSGI Middleware is Easy
================================

Really, its quite simple.

If you already knew that, this post isn't going to enlighten you at all.
If WSGI had been one of those things you kept saying to yourself, “Oh,
yea, I'll learn that someday”, consider this a short intro to all the
info a web developer and to some extent a framework author, will likely
care about.

All the gory details of WSGI along with a nice overview are available in
`PEP 333 <http://www.python.org/peps/pep-0333.html>`_. As I'm mainly
interested in it as a web developer, or as the PEP refers to it, a
“application developer”, I'll be focusing on that aspect.

Basic Usage
^^^^^^^^^^^

WSGI is intended to bridge the gap in deploying Python web applications
that might use different frameworks in a more uniform manner. A web
application that implements the WSGI interface can be called in the same
way as any other web application that implements WSGI. The basic call of
a web application using WSGI is quite straight forward (example straight
from the PEP):

::

    def simple_app(environ, start_response):
        """Simplest possible application object"""
        status = '200 OK'
        response_headers = [('Content-type','text/plain')]
        start_response(status, response_headers)
        return ['Hello world!\n']

That really shouldn't scare anyone who remembers the ‘good' old days
when your CGI scripts had to write every little bit of the content to
the web browser. ``environ`` is merely a `dict thats loaded with some
common CGI environment
variables <http://www.python.org/peps/pep-0333.html#environ-variables>`_
that anyone who has worked with CGI applications should recognize. The
``start_response`` is a Callable that the web application uses to start
the response, send the status, as well as the typical response headers.

Pretty basic stuff so far, but as web developers, we're not even likely
to need to know that much. This is because we don't need to muck around
with setting the status and dumping our content out, our web framework
takes care of it for us (the majority of which now support WSGI).

WSGI Middleware
^^^^^^^^^^^^^^^

Despite the acronym and somewhat ambiguous ‘Middleware' term, WSGI
Middleware isn't any big deal either. Take a good look at the code
fragment above… its just a function. It could be any Callable, since the
server (which we don't care about) is just going to call it. We could
wrap that Callable inside another one without much hassle. I could even
show you an `example of some WSGI middleware
code <http://www.python.org/peps/pep-0333.html#middleware-components-that-play-both-sides>`_,
but I'll leave that for you to explore.

The thing to remember here, is that your entire web application can be
called with that one simple command up above. As such, other functions
or classes can wrap around your web application object and do other
things before and/or after your web application gets called. That's
really all WSGI middleware is.

There is currently WSGI middleware that will:

-  Handle web application errors
-  Provide session support
-  Profile your web application
-  Deal with Login authentication
-  and Gzip the output

I'm sure there's even more I'm missing. The three I cited here come with
`Python Paste <http://pythonpaste.org/>`_, and using them is rather
easy. Let's assume I wanted to trap the traceback our basic web
application shown above throws, **and have it emailed to us** (if for
some reason it died a nasty death). Here's what the code would look
like:

::

    from paste.exceptions.errormiddleware import ErrorMiddleware
    wrapped_app = ErrorMiddleware(simple_app, global_conf, debug=False,
                                  error_email='fred@example.com',smtp_server='localhost')

That's it, we've now used WSGI Middleware. If you wanted to add
profiling on top of that, you'd just pass the wrapped\_app in as an
argument to another WSGI Middleware class.

Now instead of telling your server to use ``simple_app`` as your WSGI
web application, you just have it use ``wrapped_app``. Notice that we
just passed in ``simple_app`` as an argument to the ``ErrorMiddleware``
class. ``global_conf`` is a dict that Paste builds for us based on the
Paste config file, so we don't have to worry about that here either. The
other 3 keyword arguments are `visible in the ErrorMiddleware
docs <http://pythonpaste.org/class-paste.exceptions.errormiddleware.ErrorMiddleware.html#__init__>`_
and I think its pretty obvious what they all are for.

Other WSGI Middleware, like the session middleware, will add extra keys
to the ``environ`` dict that gets passed into your web application. That
way you can get to objects or variables the middleware has setup for
your use. There's nothing hidden or mysterious here, just one Callable
calling another.

PEP 333 calls this the “middleware stack”. I like to think of it as
function wrappers, or object wrappers since each one is a Callable.
We're just passing an object into a new object as an argument, and so
on.

Running a WSGI Callable
^^^^^^^^^^^^^^^^^^^^^^^

Ah yes you're wondering, great, we got this function that takes two
arguments and throws out the response, now *how do we make it run*?
There's several packages that adapt a WSGI Callable to some more common
forms of running a web application.

Probably the easiest of these to use, and the one that Paste has in it,
is the `flup package <http://www.saddi.com/software/flup/>`_. It
contains several different WSGI servers that will take your WSGI
Callable, and make it available either as Fast CGI, SCGI, or AJP. I'd
highly suggest checking out that page as it also contains an example of
using several bits of WSGI Middleware back to back.

If you were hesitant or unsure what WSGI and WSGI Middleware was before,
hopefully this post has helped. It really is pretty basic, and by
putting common tasks like error handling into WSGI Middleware it can
help people using other frameworks avoid repeating existing work.


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296349572/wsgi-and-wsgi-middleware-is-easy
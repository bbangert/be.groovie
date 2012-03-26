Pylons 0.9 released
===================

Last week during `OSCON
2006 <http://conferences.oreillynet.com/os2006/>`_, I was able to get a
release of `Pylons <http://pylonshq.com/>`_ out. This version had some
big internal changes, no longer using custom Myghty resolvers. We now
use a very straight-forward WSGI interface to setup the application and
the middleware. It's easier to customize as a result, and the call-cycle
is very understandable.

A bonus of our emphasis on using the WSGI specification and having a
flexible architecture, has been that we've been able to maintain a very
high degree of backwards compatibility despite such a large internal
change-up. Many Pylons 0.8 applications run with **absolutely zero**
changes under Pylons 0.9. Now that we're using a clean and powerful API
for our internal components, we can begin to add more new features
without any backward compatibility issues.

Additional cool features in 0.9:

-  `Swap the default templating
   language <http://pylonshq.com/docs/0.9/template_plugins.html#switching-the-default-template-engine>`_
   to your choice of `TurboGears compatible template engine
   plug-ins <http://www.turbogears.org/docs/plugins/template.html>`_
-  Controllers are called with the WSGI interface, enabling powerful
   application re-use
-  Custom version of Buffet that can cache templates rendered with any
   supported template engine
-  Mapping system now supports HTTP method restrictions for REST-ful web
   services
-  Interactive debugger can be used to examine AJAX triggered exceptions

We're still adding more great features, and working towards a very solid
and robust 1.0 release soon. The existing feature set of Pylons is
rather large as well, since many of the projects Pylons leverages have
been making great strides (SQLAlchemy, Paste, Routes, etc.).

About Pylons
^^^^^^^^^^^^

Pylons combines the very best ideas from the worlds of Ruby, Python and
Perl, providing a structured but extremely flexible Python web
framework. Python concepts are utilized as often as possible to increase
your knowledge re-use (Knowing Python makes Pylons easy), in addition to
fully leveraging the WSGI protocol for maximum code re-use.


.. author:: default
.. categories:: Python
.. comments::
   :url: http://be.groovie.org/post/296346143/pylons-0-9-released
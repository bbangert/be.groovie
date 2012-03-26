Routes 1.2 Released
===================

I got Routes 1.2 out the door today, it's a fairly important update for
2 reasons:

-  A bug crept in with 1.1 using the default controller directory
   scanner. The scanner wasn't properly retaining the directory prefix
   which causes mismatches when using controllers underneath a
   sub-directory.
-  url\_for can (and should) be used for all your URL needs, including
   static files

The second one is pretty important if you're at all interested in
creating portable web applications that can be used along-side other
applications. While some frameworks provide generation of URL's that
lead to other web pages, hard-linking the other ‘static' content will
cause problems if you try and use the application under a different
mount point.

Instead of using a url like ``/css/source.css`` it should instead be
generated with ``url_for('/css/source.css')``. This way Routes can
ensure that if you're running under a WSGI environment and there's a
``SCRIPT_NAME`` present (this indicates the applications location), it
will be pre-pended to your absolute URL's. When used like this,
additional keyword arguments passed in will be used as query args on the
URL making url\_for a handy way to create URL's that are properly URL
encoded.

Another useful feature that made it into 1.2 allows you to alias URL's
you might want to use throughout your web application, I call these
`static named
routes <http://routes.groovie.org/manual.html#static-named-routes>`_. An
example can be found in the `named routes
section <http://routes.groovie.org/manual.html#named-routes>`_ of the
`Routes Manual <http://routes.groovie.org/manual.html>`_.

Enjoy!


.. author:: default
.. categories:: Python, Code, Routes
.. comments::
   :url: http://be.groovie.org/post/296346498/routes-1-2-released
Zachary on Routes with CherryPy
===============================

`Zachary.com <http://www.zachary.com/>`_ has a very nice `update on
Routes with
CherryPy <http://www.zachary.com/s/blog/2006/02/02/integrating.cherrypy.and.routes.part.two>`_
covering not only how to integrate them, but **why** you'd want to use
`Routes <http://routes.groovie.org/>`_ style dispatch instead of the
object publishing approach CherryPy uses by default.

In the future, there'll also be an independent dispatcher for Routes
that handles dispatch at the WSGI level. I believe Ian Bicking already
has such code, though he hasn't released it yet. I'm sure it'd make a
great Part 2 in his series(?) on working with WSGI up close and
personal. If you haven't read his `Do-It-Yourself
Framework <http://pythonpaste.org/do-it-yourself-framework.html>`_, I'd
highly suggest giving it a read.

Not only does it help demystify WSGI, but it should hopefully make it
more obvious why WSGI is changing the point of competition in the world
of web programming.


.. author:: default
.. categories:: Python, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296346548/zachary-on-routes-with-cherrypy
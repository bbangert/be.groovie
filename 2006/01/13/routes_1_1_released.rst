Routes 1.1 Released
===================

I've released `Routes 1.1 <http://routes.groovie.org/>`_ today after
extending the unit tests for the new Groupings syntax and updating the
docs.

The new syntax is quite powerful and will hopefully make everyone using
Routes rather happy. While I'm not about to encourage anyone to use
URL's with .html at the end, there's plenty of times when you want
extensions to mingle with dynamic parts. You can also get some useful
abilities like being able to pull out the extension like so:

::

    map.connect('archives/:category/:(section).:(format)', controller='archive', action='by_extension')

This makes it easy to toggle the response depending on the extension,
and the regexp business is handled for you.

Integration Enhancements
^^^^^^^^^^^^^^^^^^^^^^^^

An additional feature, suggested by a Routes user was to make
integration easier in WSGI environments. Earlier, at the beginning of
each request you would have to populate the Routes config with the host,
protocol, and match result. Now, merely passing the WSGI environ to the
Routes config object will run a match, and populate those attributes for
you.

The Routes Mapper now can take a function that when called returns a
list of valid controllers. If you want to use the directory scanner
Routes comes with, all you need to do is pass in the directory you'd
like to scan and Routes will scan it for you.

These two new integration improvements make it rather simple to
integrate Routes, here's a basic WSGI app showing this off:

::

    #myapp.py

        from routes import *

        map = Mapper(directory='/my/directory/of/controllers')map.connect(':controller/:action/:id')map.connect('home', '', controller='home', action='splash')

        class WSGIApp(object):
        def init(self, mapper=map):
            self.mapper = mapper

        def call(self, environ, start_response):
            config = request_config()
            config.mapper = self.mapper
            config.environ = environ

            if not config.mapper_dict:
                start_response(“404 Not Found”, [(“content-type”,“text/html”)])
                return [“No match”]
            else:
                start_response(“200 OK”, [(“content-type”,“text/html”)])
                return [“Match with the following dict: %s” % str(config.mapper_dict)]

That's it! If you're not using WSGI, there's been no backwards breakage
so the old style of setting up all the attributes of the config will
work fine as well.

So, now I have to figure out if there's anything else Routes should
possibly have… or is the only space for improvement at this point
further optimization and perhaps usability improvements?


.. author:: default
.. categories:: Python, Code, Routes
.. comments::
   :url: http://be.groovie.org/post/296346581/routes-1-1-released
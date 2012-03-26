Routes 1.4 Release and Web Services
===================================

This is slightly old as `Routes <http://routes.groovie.org/>`_ 1.4 was
released about a week and a half ago, but I thought it deserved some
attention. There were a handful of fixes and some slightly major feature
enhancements in 1.4.

From the changelog:

-  Fixed bug with map.resource related to member methods, found in Rails
   version.
-  Fixed bug with map.resource member methods not requiring a member id.
-  Fixed bug related to handling keyword argument controller.
-  Added map.resource command which can automatically generate a batch
   of routes

intended to be used in a REST-ful manner by a web framework.

-  Added URL generation handling for a ‘method' argument. If ‘method' is
   specified, it

is not dropped and will be changed to ‘\_method' for use by the
framework.

-  Added conditions option to map.connect. Accepts a dict with optional
   keyword args

‘method' or ‘function'. Method is a list of HTTP methods that are valid
for the route. Function is a function that will be called with environ,
matchdict where matchdict is the dict created by the URL match.

-  Fixed redirect\_to function for using absolute URL's. redirect\_to
   now passes all

args to url\_for, then passes the resulting URL to the redirect
function. Reported by climbus.

Web Resources
^^^^^^^^^^^^^

The map.resource command is based directly off the `Simply
Restful <http://plugins.radrails.org/directory/show/69>`_ Rails plugin
which adds support for various verb-oriented controller actions in a
`RESTful
service <http://www.xml.com/pub/a/2004/12/01/restful-web.html>`_ style
approach. The Simply Restful layout is more or less the exact service
style laid out in the `Atom Publishing
Protocol <http://bitworking.org/projects/atom/draft-ietf-atompub-protocol-09.html>`_.

It's a great approach and it also meant providing a few other features
to Routes that I hadn't implemented previously, the most important being
able to limit matching of a URL based on the HTTP method used. This is
present in the new conditions clause for a Route:

::

    map.connect('user/:id', controller='user', action='edit', 
        conditions={'method', ['GET', 'HEAD']})
    map.connect('user/:id', controller='user', action='update',
        conditions={'method', ['PUT']})

The conditions clause can also accept your own function should you want
to restrict the route to matching based off some other criteria
(sub-domain, IP address, etc).

::

    def stop_comcast(environ, match):
        if 'comcast.net' in environ['REMOTE_HOST']:
            return False
        return True

        map.connect(':controller/:action/:id', conditions={'function':stop_comcast})

`David Heinemeier Hansson <http://loudthinking.com/>`_ recently posted
an `entry about Resources on
Rails <http://www.loudthinking.com/arc/000593.html>`_ discussing how
important web services are. The other key point was to make it easier to
write controllers that could not only give you easy browser access to
your resources, but provide a web service API as well.

The two snippets shown above give you an ``edit`` and ``update``
capability that restricts matching based off the HTTP method (verb).
Writing a huge mess of those for the rest of the functions needed for a
full web service API like Atom is a bit of busy-body work, so in the
opinionated style of Rails a single command wraps up the whole thing. In
Routes it looks like this:

::

    map.resource('user')

That will make the two routes at the top of this entry in addition to
routes that handle PUT, and DELETE. It maps them out to a set of actions
in the controller, and provides the capability to easily add more
methods for specific verbs.

The ``map.resource`` command is still getting tuned up, and we're
integrating the additional functionality it provides back into
`Pylons <http://pylonshq.com/>`_ as well. Josh Triplett also wrote some
Python code that will parse HTTP Accept headers fully so that we can add
some nice functionality to use in the controller to return the
appropriate data given what the client is expecting (HTML, XML, JSON,
etc.)

If you're using a Python web framework that doesn't use Routes… maybe
its time to put a request in. :)


.. author:: default
.. categories:: Code, Python, Rails, Routes
.. comments::
   :url: http://be.groovie.org/post/296346106/routes-1-4-release-and-web-services
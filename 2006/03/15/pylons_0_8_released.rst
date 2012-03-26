Pylons 0.8 released
===================

Finally pushed out release 0.8 of `Pylons <http://pylonshq.com/>`_, a
bunch of great features bundled up in a slick package that makes web
development easy and brings re-use to new levels. I'm not going to
repeat `the full
announcement <http://pylonshq.com/project/pylonshq/wiki/ReleaseAnnouncement>`_
here, but I'd suggest checking it out if you're the slightest bit
interested in a framework leveraging WSGI for re-use and ease of use.

Now that 0.8 is out, its already time to get to work on 0.9 which is
going to have a slightly more stream-lined WSGI stack but other than
that won't be very different from 0.8 from a usability perspective.

Ian Bicking `noted that I was considering building the next Pylons on
RhubarbTart <http://blog.ianbicking.org/cherrypy-and-rhubarbtart.html>`_
which is sort of true. `Julian Krause <http://thecrypto.org/>`_, Ian and
myself are working on WSGI and associated components that will find
themselves in all of our “frameworks” and most likely quite a few others
too. That's really one of the best things about writing solid pieces of
web code in a more component style vs. a hulking framework, portability
is great and the re-use is fantastic.

So far, `Routes <http://routes.groovie.org/>`_ has found itself embedded
in at least a half-dozen different frameworks and I've heard some rumors
its to be ported to PHP for the Zend framework as well. The
`WebHelpers <http://pylonshq.com/WebHelpers/>`_ package is also picking
up users and is being used by some Djangonauts which is great as Django
is generally a fairly ‘helper' friendly framework.

Ah yes, back to the topic, Pylons has tied together these pieces of code
in a very seamless fashion that make it easy to write what you want
without forcing you down a path that may confine you later. On the other
hand, Pylons currently doesn't have some of the friendlier elements that
frameworks like TurboGears and Django both have. Such as a pretty Admin
interface, or an extensive Toolbox app, but that stuff is in the works
where appropriate.

Our main desire with this release was to get solid footing for the
integration of these parts, and a good architecture for building web
applications. To that end, we think Pylons is a very solid performer and
will adapt easily to a wide variety of needs. You'll also get a
framework that makes it a snap to plug-in new middleware whenever
something striking your fancy appears on the radar, and you can keep
using the parts you like best, even if you stop using Pylons.


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296346326/pylons-0-8-released
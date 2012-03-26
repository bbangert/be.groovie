Routes planning and the road to Routes 2.0
==========================================

`Routes <http://routes.groovie.org/>`_ has been a wonderfully successful
project of mine as its used not just in `Pylons <http://pylonshq.com/>`_
but quite a few other small WSGI apps. It's even been `integrated as a
CherryPy URL dispatching
option <http://www.aminus.org/blogs/index.php/fumanchu/2006/10/14/if_you_like_cherrypy_except_for_the_disp>`_
for those using TurboGears 1.x or plain CherryPy. It's come a long way
since 1.0 and has diverged on quite a few fronts from the Rails version
that it was originally duplicating in functionality, which has me
thinking that perhaps its time to consider 2.0 and what that will mean.

First, I think there's quite a few behaviors that don't make sense and
probably never have. The `Route minimizing
functionality <http://routes.groovie.org/manual.html#minimum-urls>`_
sounds neat and fulfills the Rails ideal of ‘keeping urls pretty' yet
suffers from a fundamental flaw… they result in `multiple valid URL's
for the same
page <http://jtauber.com/blog/2007/08/22/trailing_slashes/>`_. James
Tauber covers some of the implications of this in addition to the issue
with relative URL's not working right either. The example he cites is
even worse for Routes since Routes can easily result in multiple URL's
mapping to the same controller action.

Routes 2.0
----------

To solve the multiple URL issue, and also address some Named Routes
confusion that recently hit the Pylons mailing list, Routes 2.0 will do
a few things differently than Routes 1.X. Many things will be
significantly more explicit and more predictable as a result. In
addition, I want to add more functionality so that Routes can be the
end-all of URL generation in addition to URL dispatching, even for use
purely generating links conditionally that aren't even used for URL
dispatching.

Some of the key changes planned for Routes 2.0:

-  **Routes recognition and generation will always be explicit**

Currently, there's an explicit option that removes the keyword
controller/action/id defaults, 2.0 will not have these implicit
defaults.

-  **Defaults don't cause minimization**

Defaults just mean they'll be used, they won't result in Route
minimization which increases the amount of URL's that end up matching to
a single controller action.

-  **Trailing slashes shouldn't be an issue**

Without routes being minimized, a route such as ‘home/index' will always
be ‘home/index' instead of being minimized to /home/. This will resolve
the trailing slash issue.

-  **Named Routes will always use the route named**

A named route currently just means that the defaults for that route will
be used during route generation. This currently can cause confusion
because people believe that the named route actually forces that route
to be used during generation.

-  **Generation-only routes**

A new option, which will result in routes that are used purely for
generation. This option will likely be used primarily for static
resources which may be on other servers, or may need the domain rotated
so that the browser can do parallel resource loading. For example, one
would be able to provide a list of domains to be used, and the generated
links will rotate as desired on the page to split page resources over
multiple domains.

-  **Redirect routes**

Sometimes, (especially when replacing legacy apps), its desirable to
slowly migrate URL scheme's from the old to the new rather. While URL's
`should never change <http://www.w3.org/Provider/Style/URI>`_, sometimes
the system being replaced has horrid URL's that violate all URL
recommendations. Being able to provide a smooth migration path from the
old URL's to the new ones is handy, and permanent redirects are
respected by many search crawlers as well.

Migration and Compatibility
---------------------------

Routes 1.8 will include options to turn on behavior that will be the
default in Routes 2.0, and if you like how Routes 1.X works there's no
need to worry, it will still be maintained for the foreseeable future.
It's currently extremely stable, and has a massive unit test suite to
ensure it operates as designed.

Add Your Desired Feature Here
-----------------------------

What other features are Routes users currently looking for?


.. author:: default
.. categories:: Python, Routes
.. comments::
   :url: http://be.groovie.org/post/296343865/routes-planning-and-the-road-to-routes-2-0
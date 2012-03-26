Routes 1.9 Release
==================

I released `Routes 1.9 <http://routes.groovie.org/>`_ today, which is
another step on the `Road to Routes
2.0 <http://groovie.org/2007/08/29/routes-planning-and-the-road-to-routes-2-0>`_.
Some of the highlights that people will be most interested that I had
previously blogged about now available:

Minmization is optional
~~~~~~~~~~~~~~~~~~~~~~~

Pylons 0.9.7 will default to turning minimization off (projects are free
to leave it on if desired). This means that constructing a route like
this with minimization off:

::

    map.connect('/:controller/:action/')

will actually require both the controller and the action to be present,
and the trailing slash. This addresses the trailing slash issue I wanted
to fix as well.

Named Routes will always use the route named
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is now on by default in Routes 1.9, which results in faster
``url_for`` calls as well as the predictability that comes with knowing
exactly which route will be used.

Optional non-Rails'ish syntax
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can now specify route paths in the same syntax that Routes 2 will be
using:

::

    map.connect('/{controller}/{action}/{id}')

Or if you wanted to include the requirement that the id should be 2
digits:

::

    map.connect('/{controller}/{action}/{id:\d\d}')

Routes automatically builds the appropriate regular expression for you,
keeping your routes a lot
easier to skim over than a bunch of regular expressions.

Routes 2 will be bringing **redirect routes**, and **generation-only**
routes, making Routes 1.9 a great way to transition to Routes 2 when its
ready.


.. author:: default
.. categories:: Python, Code, Routes
.. comments::
   :url: http://be.groovie.org/post/296342719/routes-1-9-release
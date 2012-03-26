Routes 1.0 almost ready
=======================

I've almost got a 1.0 ready of `Routes <http://routes.groovie.org/>`_.
After reading Kevin Dangoor's post on `the mysterious
1.0 <http://www.blueskyonmars.com/2005/10/04/the-magical-mystical-10/>`_
I've come to the conclusion that Routes is 1.0 ready. In case you aren't
familiar with Routes, I'd suggest taking a `look at one of my earlier
posts about
it <http://groovie.org/articles/2005/08/08/porting-routes-from-rails>`_.

So where is it? It's in the `latest
svn <http://routes.groovie.org/svn/trunk/>`_ for now, because I'd like
to actually have a nicer site with more full fledged documentation
before the release. For example, some docs on how framework creators
should go about integrating it, as well as more detailed and thorough
documentation on usage. I also have to finish up one little change that
will make Routes fully compatible with the WSGI spec when the
path/script info is split-up (which happens when a WSGI app is put under
a URL-space).

Rails routes suffers from a lack of documentation as well, and the most
complete source of information is buried in the test units for it.
There's also good docs in the Agile Web Dev for Rails book, but that's
not exactly a free public resource. So I'll likely be “porting” my docs
back to Rails, especially since `Nicholas
Seckar <http://wiki.rubyonrails.com/rails/show/NicholasSeckar>`_ has
been a great help while working on this project.

Whats New?
^^^^^^^^^^

Short answer, not a lot. The main thing was actually very trivial to
implement, **named routes**. These act essentially as a short-cut for
when you want to pull some possibly long pre-defined route defaults.
Short-cuts are good of course, as they save you a bit of typing and in
this case also make your URL's more flexible should you decide to change
how to get to a “named” route.

Here's what a fairly basic Route setup looks like:

::

    m.connect(':controller/:action/:id')
    m.connect('', controller='home', action='splash')

To implement `Named
Routes <http://wiki.rubyonrails.com/rails/pages/NamedRoutes>`_ I added
the ability to specify an additional string before the keywords. Here's
an example:

::

    m.connect(':controller/:action/:id')
    m.connect('home', '', controller='home',action='splash')

Now take a look at using it inside a template:

::

        Without named routes
        url_for(controller='home',action='splash')url_for(controller='home',action='splash', id=4)

        With named routes
        url_for('home')url_for('home', id=4)

This is slightly different from the Rails approach as I was mainly
interested in keeping it “Pythonic”. So there's no extra symbols or
functions created when using a named route.

As you can see, it can save a bit of typing as using a named route is
sort of like having a set of keywords inserted for you.

A 1.0 Release
^^^^^^^^^^^^^

Kevin's article gave me a lot of food for thought regarding whether I
should keep incrementing the Routes version. I can't see any reason not
to just go 1.0 as my version of Routes will be feature equivalent (and
then some) with the Rails version, is heavily unit-tested, and is used
in a production environment.

I'm confident in the reliability of the code and its being used by quite
a few people in production environments (myself included). Being 1.0
doesn't mean its done, it just means its hit a point functionality wise
where I've accomplished everything I wanted the “finished” product to
have. Even 1.0 software has bugs, and when I think of more features I'd
like to add, I'll start on my way to 1.1 or maybe even 2.0.

Hopefully I'll have the docs ready to go sometime before November at
which point a fully redesigned web-page will be put up. Until then, if
any of this has you interested, head over to the `Routes
site <http://routes.groovie.org/>`_ or take a look at the `unit
tests <http://routes.groovie.org/trac/browser/trunk/tests/>`_ to get a
feel for using it. If you want to see it in action, try out the `latest
version of Myghty <http://www.myghty.org/links.myt?linkid=download>`_
which contains an easy-to-use project template using Routes integration
(currently with the 0.2 Routes which is lacking Named Routes).


.. author:: default
.. categories:: Python, Rails
.. comments::
   :url: http://be.groovie.org/post/296349416/routes-1-0-almost-ready
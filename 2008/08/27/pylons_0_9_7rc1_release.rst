Pylons 0.9.7rc1 Release
=======================

`Pylons <http://pylonshq.com/>`_ 0.9.7rc1 was released a week ago,
unfortunately I haven't had time to actually blog it so better late than
never. This is a big step towards the 0.9.7 release, and contains some
major changes over 0.9.6 while still retaining a huge degree of
backwards compatibility.

At this point, the thing I get asked the most is:

    **When will Pylons 0.9.7 be released?**

So the short answer, **when the new website and docs are ready**. We're
going to a lot of effort to totally eradicate that old mantra that
“Pylons has no docs”, and we're doing it big. Most of the docs have
already been updated, revamped, and moved to the new
`Sphinx <http://sphinx.pocoo.org/>`_ doc tool (Take a look at the `new
Pylons docs <http://docs.pylonshq.com/>`_).

The new website is nearing completion as well, and for those using the
0.9.7 release candidate, when posting a traceback you'll get a link to
it thats on the new beta website. Until then, **0.9.7 is feature-frozen
and newer RC's up to 0.9.7 are bug-fix only**.

New Features
------------

Pylons gets the substantial amount of its feature-set from the other
Python libraries it uses, and here's some of the new things these
libraries have brought Pylons users:

-  Moved to `WebOb <http://pythonpaste.org/webob/>`_ from Paste for the
   `Request <http://docs.pylonshq.com/modules/controllers_util.html#pylons.controllers.util.Request>`_
   and
   `Response <http://docs.pylonshq.com/modules/controllers_util.html#pylons.controllers.util.Response>`_
   objects
-  WebHelpers 0.6 (previous was 0.4)

This is a **huge** update, including safely escaped HTML builders, a
literal object to mark strings as safe (vs unsafe) for use in templating
languages, and a move away from all the old ported Rails helpers to new
ones that in many cases have more features with less bugginess

-  Routes 1.9, with
   `minimization <http://routes.groovie.org/manual.html#minimum-urls>`_
   turned off. This helps for more predictable route generation and
   matching which confused many, and in some cases led to hard-to-debug
   routes being created and matched. The new syntax available also
   breaks with the Rails'ish Routes form, and lets you easily include
   regexp requirements for parts of the URL.
-  Mako Automatic Safe HTML Escaping
-  Simplified `rendering
   setup <http://docs.pylonshq.com/views.html#custom-render-functions>`_
   that doesn't use Buffet
-  Simplified middleware setup with easier customizability
-  Simplified
   `PylonsApp <http://docs.pylonshq.com/modules/wsgiapp.html#pylons.wsgiapp.PylonsApp>`_
   for customizing dispatch and URL resolving
-  and lots of bug fixes!

There's a `more detailed page covering
0.9.7 <http://wiki.pylonshq.com/pages/viewpage.action?pageId=11174779>`_
changes available as well that can also assist in the rather minimal
change needed for a 0.9.6 project to get going with 0.9.7rc1.

Other things in Pylons-land
---------------------------

With TurboGears2 extending Pylons for its foundation, many various parts
of TG2 have become usable within Pylons, not to mention existing
packages that have been getting better and better.

ToscaWidgets has gotten drastically simpler, no longer requiring the
rather confusing RuleDispatch package with its generic methods. This
makes the `tw.forms <http://toscawidgets.org/documentation/tw.forms/>`_
package install with a fraction of the packages it used to require, and
since it comes with Mako templates won't incur any speed bumps it used
to have from its use of Genshi. The new Pylons tutorials for it also
make it a breeze to quickly create large forms with advanced widgets.

Some might have noticed that `Reddit <http://reddit.com/>`_ released
their source code, which happens to be in Pylons. Their code is a good
example of some of the customizing possible with a Pylons based project,
as they added some custom dispatching to make controllers work in a more
similar fashion to web.py controllers that they ported their app from.
In a way, its similar to how TG2 has been able to support TG1 users for
the most part by customizing Pylons to dispatch in a TG1 style manner.

Profiling an application got a lot easier with
`repoze.profile <http://pypi.python.org/pypi/repoze.profile>`_, and I'm
sure more cool bits of WSGI middleware will be coming out of the repoze
project in the future, not including some of the past handy bits like
`repoze.who <http://static.repoze.org/whodocs/>`_ which is used in TG2
for its new identity system.

I ported a little app that `Robert
Brewer <http://aminus.org/blogs/index.php/fumanchu>`_ `wrote to track
memory
leaks <http://www.aminus.org/blogs/index.php/2008/06/11/tracking-memory-leaks-with-dowser?blog=2>`_.
Being terribly uncreative on names for my new WSGI middleware version, I
called it `Dozer <http://pypi.python.org/pypi/Dozer>`_. It's a handy
little piece of WSGI middleware to throw in when you think you might
have a memory leak to try and sort it out.

Pylons is moving along quite nicely, and the amount of WSGI middleware
and tools that work with it continue to expand which makes it hard to
list all the cool new projects I've seen lately that work wonderfully
with Pylons.

`Mako <http://www.makotemplates.org/>`_ and
`SQLAlchemy <http://www.sqlalchemy.org/>`_ continue to evolve with Mako
having pretty much zero backwards incompatible changes in the past 6+
months, while SQLAlchemy slowly deprecates things as they prepare the
0.5 release. These packages have massive amounts of features and are
rapidly becoming very stable easily making Pylons + Mako + SQLAlchemy a
tough combination to beat.


.. author:: default
.. categories:: Python, Pylons
.. comments::
   :url: http://be.groovie.org/post/296329296/pylons-0-9-7rc1-release
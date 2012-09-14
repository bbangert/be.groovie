Why Extending Through Subclassing (a framework's classes) is a Bad Idea
=======================================================================

Ok, I’ll admit it, overly ambitious blog post. So I’ll refine it a
little now, this is intended mainly as my thoughts on why as a tool
developer (one who makes tools/frameworks that other programmers then
use), its a bad idea to implement extensible objects via developer
subclassing. This is actually how the web framework I wrote - Pylons -
provides its extensibility to developers and lets them change how the
framework functions.

Please excuse the short and possibly incomplete description, this is
mainly a quick post to illustrate a tweet I recently made.

First, some background…
-----------------------

One of the things that Pylons 1.0 and prior is missing is a way to
easily extend a Pylons project. While it can be done, its very ad-hoc,
kludgy, and generally not very well thought-out. Or thought-out at all
really. What was somewhat thought-out was how a developer was supposed
to extend and customize the framework.

In a Pylons project, the project creates a PylonsApp WSGI object, and
all the projects controllers subclass WSGIController. This seemed to
work quite well, and indeed many users happily imported PylonsApp,
subclassed it to extend/override methods they needed for customization,
or changed how their WSGIController subclass worked to change how
individual actions would be called.

Everything seemed just fine…. until…

Improving Pylons
----------------

When I had some free time a little while back, I set about looking into
how to extend and improve Pylons to make up for where it was lacking,
extensibility. I quickly realized that I’d need to change rather
drastically how Pylons dispatch worked, and how controller methods were
called to make them more easily extendable. But then with a certain
feeling of dread, the subclassing issue nipped me. All my
implementations of PylonsApp and WSGIController were **effectively
frozen**.

Since every single developer using Pylons sub-classes WSGIController,
and to a much lesser extent, PylonsApp, any change to any of the main
methods would result in immediate breakage of every single Pylons users
app that happened to customize them (the very reason subclassing was
used!). This meant that I couldn’t very well change the implementation
of the actual classes to fix their design, because that would just cause
complete breakage. Ugh!

So after looking into it more, I’ve ended up with this short list of the
obvious bad reasons this shouldn’t be done. BTW, in Pylons 2,
controllers don’t subclass anything, and customization is all with hooks
into the framework, no subclassing in sight!

Short List of Why It’s Bad
--------------------------

From a framework maintainers point of view…
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Implementations of the classes are effectively frozen, because **all
   the class methods are the API**.
#. Correcting design flaws or implementation flaws are much more
   difficult if not impossible without major breakage due to point #1.
#. Heavily sub-classed/large hierarchy classes can have performance
   penalties.

From a developer ‘extending’ the classes point of view…
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#. Figuring out how to unit-test is more difficult as the full
   implementation is not in your own code… its in the framework code.
#. When using mix-in’s and other classes that also subclassed the
   framework, strange conflicts or overrides occur that aren’t at all
   obvious or easy to debug/troubleshoot.

I think there were a few more reasons I came across as well, but I can’t
recall them at the moment. In short, I’m now of the rather firm opinion
that the only classes you should ever subclass are your **own** classes.
Preferably in the same package, or nearby.


.. author:: default
.. categories:: Pylons, Python
.. comments::
   :url: http://be.groovie.org/post/1347858988/why-extending-through-subclassing-a-frameworks
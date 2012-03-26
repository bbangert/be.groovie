Hooked on Myghty
================

I've been programming web sites for many years, and have yet to come
across a templating language as appealing as
`Mason <http://masonhq.com/>`_ / `Myghty <http://www.myghty.org/>`_. To
avoid confusion I'm going to talk about Myghty, but since its a direct
port of Mason (plus some MVC stuff) all of my comments apply to Mason as
well (unless otherwise noted). So if you find yourself stuck using Perl
(or you prefer Perl) and something here sounds appealing, by all means
use Mason as I did.

Despite Myghty only having come into existence approximately 14 months
ago, the code-base is stable, very quick, and has been running in
production environments for over 8 months. This is mainly because it
started as a very direct port of Mason to Python, it then `grew a few
additional
features <http://www.myghty.org/docs/technical.myt#technical_differences>`_
that made it great for MVC use. The methodologies present in Mason (thus
Myghty as well) are known to scale to very large and complex sites, as
this `list of Mason-powered
sites <http://masonhq.com/?MasonPoweredSites>`_ shows. But it's the
little things added up that really make Myghty my template language of
choice.

This is a rather lengthy post as I highlight and explain some core
concepts of Myghty, please bear with me… also, if you'd like to follow
along and try the examples out, its really easy to get started using
`Myghty with
Paste <http://www.myghty.org/docs/installation.myt#installation_paste>`_.

Syntax
^^^^^^

Template languages vary a lot in style, there are the very basic string
replacement template languages all the way to more advanced template
languages. Myghty definitely weighs in on the latter as it has many of
its own concepts with regards to templating that produce a very robust
and advanced templating system.

The syntax itself is also very appealing to me, as I'm a fan of
templating languages that keep their guts inside < > signs. The only
exception to this being if you need a quick line of Python, which is
done just by having a % in front of it. Here's what a loop would look
like:

::

    % for person in people:
       <b>Hi</b><% person %>
    % #end

You'll notice an additional line is needed to indicate the end of the
loop. This is because Python uses white-space to determine blocks and
Myghty needs to know when the indentation is over.

Components and Inheritance
^^^^^^^^^^^^^^^^^^^^^^^^^^

In Myghty, each template is more properly referred to as a Component.
When a component is directly called as a request (or sub-request),
inheritance is applied. This is how a site's skin is typically applied.
Rather than having to specify in your template that it *includes* or
*extends* some other template, in Myghty your component **automatically
inherits** from an autohandler file above it.

An easier way to think of it is to consider your template directory
layout as a Class, and all the templates in it are methods. Every
directory inside that root one is another Class, and so on. The
``autohandler`` in this context acts much like your ``__init__`` method.
Here's a little example:

::

        /autohandler
        Sitename% m.call_next()



.. author:: default
.. categories:: Python, Perl, Myghty
.. comments::
   :url: http://be.groovie.org/post/296349456/hooked-on-myghty
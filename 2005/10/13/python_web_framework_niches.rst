Python Web Framework Niches
===========================

I've come to the belief lately that the web frameworks available in
Python are increasingly fine-tuned to specific application requirements.
Of course, anyone reading the ‘About' sections for these frameworks
should realize this as well. I wonder how many people actually read that
section as I've seen people latch onto web frameworks without knowing
the task it was originally made for.

Without knowing the reason the framework was created, its common for
many people to leap to the conclusion that its another Rails wanna-be
just because its a ‘full-stack' web framework. I was playing around with
a nice full-stack framework called
`WebObjects <http://www.apple.com/webobjects/>`_ **years ago** which
made it easy to setup database objects, generate CRUD, etc. Zope's been
doing the same stuff for what now seems like eons as well, yet I don't
see people declaring RoR a Zope clone (It obviously isn't).

In light of that, I'm inclined to agree with `Ian Bicking's
response <http://developers.slashdot.org/comments.pl?sid=164824&cid=13756986>`_
about the lessons Python web people did learn from RoR.

The concept I want to focus on is that **people create these new
frameworks because they make their task easier than any of the other
frameworks already out there**. While they might pick up features from
other frameworks, most of them aren't aspiring to be “Python on Rails”.
Sometimes this task is easier when other tools can be integrated to
avoid code replication, as is the case in one framework I cover here.

Many people have declared the amount of Python web frameworks a
“problem” that should be “solved” somehow, perhaps a Highlander fight
with swords to the death (\_There can be only one!\_). I'd like to
suggest the opposite, there's a lot of Python programmers and I think
there's room for even more web frameworks. The variety is a **strength**
because they make it easier to get specific web applications done.

TurboGears
^^^^^^^^^^

The `TurboGears <http://turbogears.com/>`_ site has a nice `about
page <http://turbogears.com/about/index.html>`_ describing its purpose,
though I feel it doesn't completely explain the rationale for its
creation. There's some interesting and unique decisions made in
TurboGears, like using `Kid <http://kid.lesscode.org/>`_ instead of
`Cheetah <http://www.cheetahtemplate.org/>`_ or
`Myghty <http://www.myghty.org/>`_ for templating. Then there's the
inclusion of `Mochikit <http://www.mochikit.com/>`_ and the TurboGears
decorators for returning output as JSON for use with Mochikit.

So what kind of applications is this web framework geared for? (Please
excuse the pun)

The best way to answer this is to look at the application this framework
was created for, `Zesty News <http://www.blazingthings.com/>`_, and the
abilities of some of the tools being used. Zesty News is in a rather
interesting category of web applications in that the end-users
themselves will be installing it, quite likely on their home computer
rather than a server. Being able to package it up and easily
distribute/upgrade it becomes a key issue along with database
portability and code thats database agnostic.

Two tools assist here,
`setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_ for
distribution/packaging and `SQLObject <http://sqlobject.org/>`_ for
portable database code. Zesty News deals extensively with RSS and XML,
so it makes sense that the templating language chosen was actually
`created for dealing with web
services <http://lesscode.org/2005/09/24/web-services-infrastructure-kid/>`_.

These design decisions behind TurboGears should make it fairly obvious
when to consider it for your next project. The cohesive toolset you get
when you choose TurboGears is ideal for developing portable, easily
deployable AJAX-enabled web applications that likely deal with XML
frequently and need to stay database agnostic. Even if your web
application doesn't deal with XML frequently, the decisions TurboGears
makes for AJAX integration will make it easy to add heavy dynamic
interaction to a TG webapp.

Django
^^^^^^

`Django <http://www.djangoproject.com/>`_ was created to deal with the
requirements of working in the web development department of a news
publisher. As such, the framework was created specifically to deal with
the requirements placed upon the author. What's rather interesting is
the lack of re-use in Django when it comes to doing things that have
been done before in other projects (Database mapper, form validation,
etc).

The tools and parts of Django were specifically built to work as one
package, and using Django makes that very obvious. One of the things
most common when in a newsroom or publishing environment is dealing with
CRUD. That is, there is a lot of content and ways to get content into
the system and administrate the content is a high priority. As a web
framework built for dealing with Content, many of the design decisions
reflect the common tasks present in CMS's (Content Management System).

To start with, you get a slick administration interface for your
conntent, that's miles beyond any of the generated CRUD type stuff in
other web frameworks. This differs from the philosophy of other web
frameworks that give you basic CRUD (Scaffolding in Rails-speak) in that
Django's admin interface is aimed directly at being production-ready
with no modification at all.

Django also makes it fairly easy to make a Django ‘application' like a
Forum or Blog, then slot it into other Django application environments.
Again, this makes a lot of sense given the original requirements placed
on the creator of Django. If a company has 4 websites, and wants them
all to have the new Forum/Classified ability it makes a lot of sense for
this task to be optimized.

So what web applications are you going to want to use Django for?

Quite a few, as it turns out dealing with Content is a very common task.
If you're writing a web application heavy on content, that needs a full
featured web interface for managing the content it'd be really hard not
to recommend Django. It's easy to get started, and in almost no time you
have very powerful functionality running that gives you a lot of
usability.

Don't be Everything for Everyone
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Part of the reason I picked these two projects to talk about is that
they're both extracted from a working project (as Rails was). I also
haven't seen many people mention the fact that frameworks developed in
such a manner are also inherently going to be optimized for the
use-cases that brought them into existence.

Open-sourcing the project lets them grow to an extent, but their design
is largely baked in and a useful limitation. Too much expansion past the
initial design requirement will make them generic, and with that comes a
lot of complexity (sometimes worth it though for the extra
re-usability).

Note that the specific things Django gives you don't help that much if
you're trying to write a Zesty News style application. The same goes in
reverse as well, since building an Admin interface of your own isn't fun
and can be time consuming. While it's possible to make web applications
that do this in either framework, compensating for framework design will
require extra time when you try to use one framework for everything.

If you're using one framework for everything, maybe its time to take a
look around.


.. author:: default
.. categories:: Python, Thoughts, Code
.. comments::
   :url: http://be.groovie.org/post/296349521/python-web-framework-niches
Project/Code Re-Use, TurboGears, and Django
===========================================

`TurboGears <http://www.turbogears.org/>`_ has been making some
impressive strides in both features, documentation, and possible user
acquisition lately. Where it gets somewhat interesting is regarding its
user-base though. The approach TG takes – building glue on top of other
projects – is not new, as `Subway <http://subway.python-hosting.com/>`_
also utilizes this, however the popularity TG has been enjoying has
resulted in some interesting by-products.

First, its a bit interesting to take a look at some numbers. It's hard
to be precise, as users don't exactly announce themselves, but many of
them do usually join the mailing lists for the projects.

Django-users:

-  Users: 546
-  Activity: Medium
-  Average messages per month (5 months+): 340

**Update**: Eugene pointed out that there is Django-developers as well.
Many of the Django-devel members are also on the Django-users list, so
adding them together wouldn't be too accurate. Here's the Django-devel
information, along with the total traffic if you take the two combined.

Django-developers:

-  Users: 323
-  Activitiy: Low
-  Average messages per mont (5 months+): 177
-  Average messages of Django-devel+users: 517

TurboGears:

-  Users: 668
-  Activity: High
-  Average messages per month (3 months+): 1,124

*Information taken from Google Groups as of Nov. 14th, 2005*

While each list is bound to pick up users that contribute and lurk **who
do not actually use the framework**, I think this trend is significantly
higher with TurboGears. I believe this is because TurboGears builds on
several successful projects that are even used in fields **outside of
web development**.

Project/Code Re-Use and Explaining the Mail Traffic
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

`Django <http://www.djangoproject.com/>`_ takes a somewhat interesting
approach, especially when compared to TurboGears, in that re-use is
non-existent.The `reason given for the amount written from
scratch <http://www.djangoproject.com/documentation/faq/#why-did-you-write-all-of-django-from-scratch-instead-of-using-other-python-libraries>`_
does make sense to a certain extent, especially when you remember that
Django was created 2 years ago (some existing projects weren't too hot
back then). It's also interesting to note that in some cases, the syntax
and decisions being applied to Django now, reflect those made quite
awhile ago in other projects.

`TurboGears <http://www.turbogears.org/>`_ pushes re-use to the extreme,
and only resorts to writing it from scratch if there's no clean way to
integrate a similar project that does the same thing. Only the new
Identity framework, and the crud stuff was written from scratch for
example. But many of the largest, most heavily used pieces have large
communities of their own, i.e. `SQLObject <http://sqlobject.org/>`_,
`FormEncode <http://formencode.org/>`_,
`CherryPy <http://www.cherrypy.org/>`_,
`MochiKit <http://www.mochikit.com/>`_, and
`setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_ (I
likely missed some).

Also interesting to note, several of the top posters to the TG mailing
list happen to be the project developers for the individual projects TG
is comprised of. I doubt they're heavy users (or perhaps haven't even
used TG), however they have plenty to contribute as the questions often
relate to the individual parts. This creates a powerful community and
further fuels development and use of the individual projects TG pulls
together.

When considering the use of one framework vs the other, I think this
re-use issue is definitely something to be considered. Building on other
stable, established projects that are used widely and extensively leads
to a more mature platform. The size of each individual community also
means more people to work on solutions that benefit the whole (and even
those using the parts).

For example, the TG community is starting to tackle some basic
CRUD/administration type stuff. I don't actually use TG myself, but I do
use SQLObject and FormEncode which means I can plug my SQLObject classes
into a TG project, and use their web based admin tool with my database.
This is rather powerful and extremely useful code re-use, and in the
future it'll be even easier to do the same thing (likely using a WSGI
app).

Code re-use is important, and the project re-use that TG employs leads
to many benefits. Despite the reason cited on the Django page, I think
Django is still ripe for re-use cases. The Django syntax is now so close
to SQLObject, I wish Django would just switch to it and extended it
where needed, rather than continue to re-implement the rest of it.

To be fair, Django does make it possible to use other templating
languages, and Zope3 Page Templates are available (along with a Django
ZPT error formatter). If part of the argument for OOP and Python is code
re-use, projects that re-invent not just the wheel but the entire car
aren't exactly shining examples of what's possible in Python.


.. author:: default
.. categories:: Python, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296349154/project-code-re-use-turbogears-and-django
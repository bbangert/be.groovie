SQLAlchemy, Declarative layers, and the ORM 'Problem'
=====================================================

There's been a bit of `talk on the Pylons devel list regarding the
recommended way to use SQLAlchemy with
Pylons <http://groups.google.com/group/pylons-devel/browse_frm/thread/2b82c7093f50afc4/ace626bd4aa2d819#ace626bd4aa2d819>`_
mainly regarding how to use SA (SQLAlchemy) in a fashion that is well
documented and easy to work with (and maintain!).

Prior to Pylons 0.9.6 and SQLAlchemy 0.4 it was a bit of a mess, with
the framework needing to load the config (since thats where your db
settings are), then setup globals for SA…. eek. Mike Orr had a good
intermediary solution for SA 0.3 called SAContext that handled many of
the tricky parts. Unfortunately, this actually caused even more
confusion as more ways of doing the same thing came about. SAContext
solved some of the global config grabbing issues, but the additional
layer of indirection made trouble shooting even harder (despite how
small of a library it was).

Less is More
------------

So the fix? Less intermediary layers, less indirection… essentially,
`KISS <http://simple.wikipedia.org/wiki/K.I.S.S>`_. Despite how much
Pylons was attempting to help a user to get the db going, the additional
layers in the end actually caused more problems then they solved. Of
course, I shouldn't have been too surprised…. `Mike
Bayer <http://techspot.zzzeek.org/>`_ did warn me about many of these
things at the beginning. Being overly eager to make things “easier” for
new users, I ignored him. :)

This is why Pylons does **not** recommend Elixir, and with SA 0.4 the
recommended usage of SA is to use its plain mapper functionality should
you need an ORM layer. Yes, that's right, despite almost every web
framework out there pushing its ORM on you (or someone else's ORM),
there are many times when an app doesn't even **need** a full-blown ORM.

Declarative vs Basic SA
-----------------------

For a better look at why one might consider additional layers on SA a
bad thing lets compare a fairly basic table setup consisting of users
and groups. Each user can be in multiple groups, and lets use proper
referential integrity to ensure that groups aren't deleted when users
are still in them.

Compare the following two ways of setting up a basic many to many
relation and the tables:

**SQLAlchemy 0.4**

::

    from sqlalchemy import Column, ForeignKey, MetaData, Table, typesfrom sqlalchemy.orm import mapper, relation

        metadata = MetaData()

        person_table = Table('person', metadata,
        Column('id', types.Integer, primary_key=True),
        Column('name', types.String, nullable=False),
        Column('age', types.String))

        group_table = Table('group', metadata,
        Column('id', types.Integer, primary_key=True),
        Column('name', types.String, nullable=False))

        persongroups_table = Table('person_groups', metadata,
        Column('person_id', types.Integer, ForeignKey('person.id', ondelete='CASCADE'), primary_key=True),
        Column('group_id', types.Integer, ForeignKey('group.id', ondelete='RESTRICT'), primary_key=True),)

        class Person(object):
        pass

        class Group(object):
        pass

        mapper(Person, person_table, properties=dict(
           groups=relation(Group, backref='people', lazy=False)))mapper(Group, group_table)

**Elixir**

::

    from elixir import *class Person(Entity):
        has_field('name', String)
        has_and_belongs_to_many('groups', of_kind='Group')

        class Group(Entity):
        has_field('name', String)
        has_and_belongs_to_many('people', of_kind='Person')

On first glance, its pretty obvious that everyone should love Elixir vs
the obviously more tedious SA approach of layout out your tables, then
mapping them to the class objects. However, look at these two examples,
and try to quickly answer the following questions:

-  How do you add a column to the many to many table to store an
   additional bit of info for the join?
-  Do they both enforce referential integrity?
-  How do you control whether SA is eager loading the relation? Can you
   restrict it to just one column of the relation?
-  What are the table names used?
-  How many tables are in your database?
-  Where do you change the id column name?
-  Which one is closer to the `Zen of
   Python? <http://www.python.org/dev/peps/pep-0020/>`_

I think the explicit setup makes many of these questions easier to
answer just at a glance. Those with enough Elixir experience can fairly
easily answer most of these questions, but consider what that implies.
Not only do you need to know SQLAlchemy options and parameters, but you
need to know Elixir options and how they map to the SQLAlchemy
functions. The desire to reduce the up-front setup of the ORM actually
increases the amount of knowledge a user has to have in order to use it,
and the most worrisome aspect… how to troubleshoot it.

Setups that Grow with You
-------------------------

With Pylons, a goal has been to provide out of the box recommendations
that grow with you. That is, using the set of recommended tools may not
be as apparently “easy” as some other frameworks. However, the pay-off
is that you don't hit a wall in 2 months when your application
inevitably gets a little more advanced and needs to do something the
simple tools either can't do at all, or it's incredibly difficult to do
even slightly complicated things (eager load 2 columns off a related
table, but not all of them). This way, the toolset you learned, you can
keep using as you get more advanced and you don't “outgrow” your tools.

While Elixir definitely appears to be easier at first glance, when you
need to get more complicated you can't exactly turn to the SA docs since
Elixir has put a layer between you and SA. This can be very crippling
when you eventually hit a wall, and so much ‘magic' is wrapped up in the
declarative layer that you have to troubleshoot additional layers of
code when something goes wrong. The result of this is that to
effectively use Elixir in complicated setups with SQLAlchemy, you need
to really **really** know both of them which actually requires more work
for a user than plain SQLAlchemy.

The SA example clearly requires a little more up-front setup, however,
are you really adding tables to your database every day? How often are
you going to be actually touching the table and mapper code, vs just
adding domain model methods to your Person/Group class? Did the layer
make it easier or harder to use multiple databases and/or put more
between you and advanced SA functionality you might need later?

`Adam Gomaa <http://adam.gomaa.us/blog/>`_ pointed out some interesting
`issues with Django's ORM and
Elixir <http://adam.gomaa.us/blog/the-django-orm-problem/>`_ but
unfortunately tries to do the same thing Elixir and TurboEntity do…. add
more layers. More layers more indirection more to wade through when you
need to do something that should be pretty basic with SQLAlchemy (and is
probably nicely documented on the SA site, which won't help with these
layers until you dig through the layer to find the basic SA objects the
SA site refers to…).

What really makes a lot of this even more trouble-some with SA, is that
when setting up complex relationships, the order of declaring table
objects becomes important, since relations need to refer to them and the
ORM classes. This usually results in some interesting metaclass hackery
when you have these Entity's in multiple modules, importing each other,
and doing other fairly common stuff.

SQLAlchemy 0.4
--------------

In the end, I've been using plain SQLAlchemy 0.4 (at beta5 now, but
quite stable) a lot lately, and its really great. Yes, setting up the
tables (generally a one-time thing) took me probably 15 mins longer than
it would've with Elixir. But I'm fairly certain I've saved myself
significantly more time in the long run since I won't need to worry
about diving into Elixir code to try and find SA objects when I need a
complex query, or trying to figure out how to hack Elixir's connection
should I need multiple db connections at once, etc.

So please, new users to SQLAlchemy, use **just** SQLAlchemy. It
definitely seems daunting at first, but the flexibility and
comprehensive documentation give you a solution that scales to meet your
needs, with no walls in sight.

**On a side-note, its interesting to compare my position on this issue
to the Django team lack of AJAX helpers. The Django team rightfully
claims that Javascript isn't that hard, so “get over it” and learn a
nice Javascript library so you can do powerful things. Also note that by
including AJAX helpers, Pylons is encouraging one part that doesn't
scale… as the AJAX helpers will have you hitting a wall sooner or
later.**


.. author:: default
.. categories:: Python, Thoughts, Pylons
.. comments::
   :url: http://be.groovie.org/post/296343813/sqlalchemy-declarative-layers-and-the-orm-problem
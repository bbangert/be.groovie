Google Datastore and the shift from a RDBMS
===========================================

So many random musings and theories on Google App Engine, I won't bother
musing about it myself, except to mention that Ian Bicking `put together
instructions for running Pylons on
it <http://code.google.com/p/appengine-monkey/wiki/Pylons>`_. These also
work fine for using the latest Pylons 0.9.7 beta.

I got `Beaker <http://beaker.groovie.org/>`_, the session and caching
WSGI middleware that Pylons uses, running fine on Google now, using
Google Datastore as the backend. Diving into the Datastore docs to get a
grip on what's the best way to implement it shed some light on the
transition any developer thinking about writing data-backed apps for GAE
(Google App Engine) will need to tackle.

Some notes on terminology, Google has Entities, Kinds, and Properties.
These correspond roughly to Rows, Tables, and Columns in RDBMS-speak.
Kinds can also be called classes, because in the Python API, you create
a class and inherit from the appropriate datastore class. Entities may
also be referred to as instances, since performing a query returns a
list of objects (instances).

Sessions and Datastore
----------------------

First, regarding sessions. Beaker will now let a Pylons app use normal
sessions on GAE, the real question is, should you?

The `Google User API <http://code.google.com/appengine/docs/users/>`_
makes it trivial to get currently logged in user, and the datastore
comes with a property type for a ‘table' that is specifically made for a
Google user account reference. So with just one short command, you can
have an entity from the Datastore that corresponds to a given user, ie:

::

    userpref = UserPrefs.all().filter('user =', users.get_current_user()).get()

The Datastore is blindingly fast for reads and queries, so there's a
compelling reason to ignore sessions altogether and just fetch the
appropriate preferences or what-have-you. This leaves people with the
normal reason for wanting **more**, ie, a **session**, “But wait, I want
to stash other little things with the user when they run around my
app!”. Not a problem.

Google's Datastore has an `Expando
class <http://code.google.com/appengine/docs/datastore/expandoclass.html>`_
for entities that lets you dynamically add properties of various types.
It's like having a RDBMS where you can just add columns to each row, on
the fly. The
`dynamic\_properties() <http://code.google.com/appengine/docs/datastore/modelclass.html#Model_is_saved>`_
entity method makes it easy upon pulling an object, to see what dynamic
properties were already assigned.

As far as I'm concerned, this pretty much mitigates the need for a
session system. If you didn't want to require user login, you could
always make a little session ID yourself, and keep that on the UserPrefs
table as a separate property, then query on that.

Rethinking how you store/query/insert data
------------------------------------------

Going slowly through all the Datastore docs and especially reading some
of the performance information people were drumming up on the GAE mail
list brought up a number of issues with how people with RDBMS
backgrounds approached Datastore. Many of the table layouts I saw pasted
on the mail list were clearly written for how an RDBMS works, with
sometimes significant work required to adapt it to deal with Datastore.

A little background might help understand this difference. Google
Datastore is implemented on top of
`BigTable <http://labs.google.com/papers/bigtable.html>`_, which is
described briefly in the paper as a “sparse, distributed, persistent
multi-demensional sorted map”. One of the other descriptions I heard in
a talk on data storage techniques at FOO Camp from a Google developer
was, “think of a BigTable table as a spreadsheet, except with pretty
much as many columns as you want”.

This brings about a fairly big shift in thinking for the developer who
grew up on an RDBMS. The fairly normalized organization of data written
without regard to massively distributed data stores suddenly becomes a
rather big problem. Consider a few of the ‘limitations' of Datastore
that will jump right out at you:

-  You cannot query across relations
-  You cannot retrieve more than 1000 rows in a query
-  Writes are much much slower than you're used to (a developer on the
   mail list said 50 inserts with 2 fields each almost ate up the 3
   seconds allowed for a web request)
-  There are **zero** database functions available
-  There is no “GROUP BY…”, which doesn't matter much if you read the
   prior bullet point
-  Transactions can only be wrapped around entities in the same entity
   group (ie, the same section of the distributed database)
-  Referential integrity only sort of exists
-  No triggers, no views, no constraints
-  No GIS Polygon types, or anything beyond just a GeoPoint (Odd,
   considering that Google has so much mapping stuff)

Then of course, a few of the new things that might leave you scratching
your head, quite happy, or both:

-  Keys for an entity may have ancestors (ancestors aren't relations,
   they're different and have to do with Entity Groups, which determine
   what you can do in a transaction, wheeee!)
-  An Entity Group doesn't have to all be of the same Kind, its more of
   an instruction to Datastore to keep these near each other when
   distributed
-  Key's can be made before the entity, just so you can make descendent
   entities of the key, then make the ancestor
-  The handy
   `ListProperty <http://code.google.com/appengine/docs/datastore/typesandpropertyclasses.html#ListProperty>`_,
   when used in a query, will let you use the conditional argument and
   apply it to every item in the list (sort of like an uber ‘IN (…)'
   query, except it can also find all the data where a member in the
   list was , or = to something else)
-  Making more Entity groups is a good idea when you frequently need a
   batch of “these few things” for a request, especially if you need to
   alter them all at once in a transaction
-  Normalizing is frequently bad since you can't query across relations,
   dynamic properties make it easy to heavily denormalize. If you do
   normalize some data and its for the same batch of ‘things you always
   need at once', use Entity groups. Or use a ReferenceProperty if its
   merely something related you may occasionally hit.
-  The ReferenceProperty() does not **have to refer to a known kind**,
   you can decide on the fly what datastore classes to reference if not
   specified when declaring the ReferenceProperty
-  Many to Many relations aren't what you think, now you could have a
   ListProperty() of ReferenceProperty()’s, which may or may not all
   refer to instances of the same class
-  A query may return entities of different kinds, if querying for
   entities of a given ancestor

(There's probably a bunch more as well, these were some of the obvious
ones that jumped out at me)

The end result of this, is that the standard way a developer writes out
the table schema for a RDBMS should be dumped almost entirely when
considering an app using Google Datastore. Storing data and using Google
Datastore isn't difficult, but it is a pretty hefty paradigm shift,
especially if you've never left RDBMS-land. This is not a trivial change
to make in approaching your data.

I rather enjoyed working with these new ways of tackling data, and the
possibilities opened by the ways it lets me store and refer to data in
many ways goes beyond the traditional RDBMS. In the short term though, I
doubt I'll be making any GAE app's until there's an `alternative
implementation <http://hadoop.apache.org/hbase/>`_ thats production
ready… I just can't handle the lock-in.

And of course, please note any corrections or inaccuracies in the
comments.


.. author:: default
.. categories:: Python, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296342863/google-datastore-and-the-shift-from-a-rdbms
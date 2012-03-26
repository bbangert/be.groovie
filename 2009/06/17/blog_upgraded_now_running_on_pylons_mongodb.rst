Blog upgraded! Now running on Pylons + MongoDB
==============================================

I've now updated the blog software powering my blog, which is very long
overdue. In the past, this blog was run off
`Typo <http://wiki.github.com/fdv/typo/>`_, which apparently now hosts
their home site off the github (its moved a dozen times in the past 3+
years).

Typo always worked moderately well for me, however, I found it sluggish
(Prolly Rails there), and incredibly horrid on ram usage. It was not at
all unusual to see it running past 700 megs of RAM after running for
just a few weeks, which is a bit annoying as the machine only has 4GB
total and is running quite a few things.

After last weeks `SF Python Meetup on
MongoDB <http://www.meetup.com/sfpython/calendar/10561903/>`_ I figured
it was time to get a little actual MongoDB usage under my belt. I also
inadvertently implemented enough of the MovableType XMLRPC API as I
didn't want my app to be too extensive, just enough for me to post to my
blog.

So in the end, I had a small set of requirements for the replacement:

#. Not be horribly slow
#. Not take up huge amounts of RAM
#. Retain **all existing URL's** (It really annoys me when people break
   their old links)
#. Compatible with my blog software (MovableType / MetaWeblog XMLRPC
   API)
#. Not screw up the RSS/Atom feeds and cause Planet Python to show all
   my posts as if they were new (I've seen this happen to a few people
   on occasion)

I wanted to build it myself, because of course, the world definitely
needs more blog apps, and I wanted one that used MongoDB. So for those
curious, `here's the source code to the blog
app <http://bitbucket.org/bbangert/minger/>`_.

It's rather rough, as its fairly custom built just for my needs, nor do
I have any plans to expand it into some general purpose blog engine,
with themes, etc. The only other thing pending at the moment is to add
the ability to comment again, as I haven't quite gotten that feature in
yet. For those trying it out, the README should help get started, but
its very rough (thus the name of the package).

Strings, Unidecode, and Slugs
-----------------------------

When copying some functionality I needed from the Rails app (to retain
URL compatibility), I noticed two things it did which I thought was
handy. To convert a title into slug for the article, it used a fairly
sophisticated scheme relying on two other packages.

First, was the use of a Ruby port of a Perl package called
`Text::Unidecode <http://search.cpan.org/perldoc/Text::Unidecode>`_
which is pretty cool, and converts UTF-8 chars into their closest ASCII
version. I figured someone must've ported it to Python as well, and
`sure enough, someone
did <http://www.tablix.org/~avian/blog/archives/2009/01/unicode_transliteration_in_python/>`_!
It wasn't on the cheeseshop though, which was unbearable for me, so I've
posted it to the Cheeseshop so others can easy\_install it.

Next up, was a Ruby library called
`stringex <http://github.com/rsl/stringex/tree/master>`_, which add's a
few things to Rails, including a string method called ‘to\_url'. That
method does a variety of transformations to remove all those funny
characters from a title, and do a bunch of other neat changes of common
characters to human readable versions (`source for those
conversions <http://github.com/rsl/stringex/blob/fafb90b75a5d694120d652870dead211b1c85f81/lib/lucky_sneaks/string_extensions.rb>`_).

I ported the key module of stringex to Python, and it `resides in my
blog
app <http://bitbucket.org/bbangert/minger/src/tip/minger/lib/stringex.py>`_.
If someone would like to extract it and make it into its own package, or
even better, if I somehow missed the fact that someone else has ported
it already, let me know (tweet me @benbangert!).

I'll be writing up my thoughts on making a small app with MongoDB, and
how it differs from my experience working with CouchDB for
`PylonsHQ <http://pylonshq.com/>`_ in a later post for those curious.


.. author:: default
.. categories:: Code, Pylons, Python
.. comments::
   :url: http://be.groovie.org/post/296328789/blog-upgraded-now-running-on-pylons-mongodb
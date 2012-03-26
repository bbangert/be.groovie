Where's Single Sign-On? Part 2
==============================

In a `recent Wired article regarding One
Login <http://www.wired.com/news/privacy/0,1848,68329,00.html>`_,
reference is made to a new social style network called GoingOn. The
article spends most of its time focusing on one site that hopes to
aggregate functionality that currently is split between Blogger, Flickr,
Friendster, and Bloglines (for the most part). However, the thing it
misses is what I `previously
discussed <http://www.groovie.org/articles/2005/08/15/wheres-single-sign-on>`_
regarding the lack of a working distributed identity system.

After looking around more, I'm happy to say there are indeed working
identity systems out there. Unfortunately the most promised of them, the
Liberty Alliance doesn't seem to have much oomph behind it, but two
others that I previously didn't know about are now out there.

The first is from the folks at Microsoft, which they've called an
Identity Meta-System (or something like that), which is `described over
at
vnunet <http://www.vnunet.com/vnunet/news/2127359/web-services-nears-federated-id-nirvana>`_.
It seems to be rather tied (or at least integrated heavily) to Microsoft
technology (go figure!), and will be included in Indigo and other
various Micrsoft technologies. As a mainly open-source coder, this has
little appeal to me, nor am I about to start using Microsoft API's to
write my websites and web code. The standards utilized by Microsoft for
their `Federated
Identity <http://en.wikipedia.org/wiki/Federated_identity>`_ are
generally known as WS-\* for some reason I'm too lazy to investigate.

The second is much more appealing (to interested users and web
developers), and has actually been around for a very long time in a
primitive form (2000 is ancient by web standards). The home site appears
to be the `identity commons <http://idcommons.net/index.html>`_, and the
current sole Identity Broker is `2idi <http://2idi.com>`_, the
organization behind the standards is `XDI <http://xdi.org/>`_. They've
made the entire code-base they run the Identity Broker on, open-source
under the `Affero General Public
License <http://www.affero.org/oagpl.html>`_ to ensure that users are
never locked into just one Identity Broker (Yea!).

If you're curious how the Microsoft and Liberty Alliance methodology
differs, `idcommons has a useful FAQ addressing the
differences <http://wiki.idcommons.net/moin.cgi/FaqDevelopment>`_.

The most exciting aspect for me, is that all the technology behind the
XDI approach is completely open-source, and geared towards maximum user
flexibility and empowerment. The user gets to move data between Identity
Brokers, and every care has been made to ensure the user is never locked
into a single Identity Broker. Actually, the most exciting part, is that
it works right now. :)

They're currently preparing to switch to a SAML-2.0 backed code-base,
however the code they have only works from PHP, Java, and Perl. If you
want to try it out, `here's how to get an
i-Name <http://wiki.idcommons.net/moin.cgi/GetAnIname>`_, and you can
try it out on those two sites. Also, a developer made a `ISSO (I-name
Single Sign-On) authentication system for
WordPress <http://www.planetwork.net/downloads/>`_ which is pretty cool.

So what's stopping ISSO from being used on more websites? It's free, its
open-source, its standards based, its not controlled by a commercial
corporation….

It needs Python libraries!

I should mention, when I first wrote this as far as I knew, there was no
Ruby version. There still isn't a public one, but `Victor
Grey <http://www.planetwork.net/2003conf/textpages/presenters/VictorGrey.html>`_
is fairly close to a Ruby version with a full Rails rig to go with it
which I'm rather looking forward to.

Anyone want to help? I'm tired of remembering a zillion usernames and
passwords, and with ISSO on the horizon I shouldn't need to, all the
Python web frameworks will be a bit better (at least the sites that use
usernames/passwords) with an easy way to use ISSO.

By the way, for a useful overview of SAML, there's a `very detailed
write-up of SAML2 on
xml.com <http://www.xml.com/pub/a/2005/01/12/saml2.html>`_.


.. author:: default
.. categories:: Code, Python, Rails, Ruby, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296352230/wheres-single-sign-on-part-2
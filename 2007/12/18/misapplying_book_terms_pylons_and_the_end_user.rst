Misapplying book terms, Pylons, and the 'end-user'
==================================================

On the Internet, I frequently see terms misapplied to other contexts.
Whether its a basic definition misapplied to a different realm, or an
analogy grossly misapplied to a context that is not in fact similar.
Since `this particular
term <http://adam.gomaa.us/blog/frameworks-exist-for-conceptual-integrity/>`_
‘conceptual integrity' however was used as a beating stick on Pylons, I
felt it's something worth discussing.

First, its very useful to actually understand the context of the book
the term comes from, `The Mythical
Man-Month <http://www.amazon.com/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959>`_.
The Mythical Man-Month is about Fred Brooks observations as a manager on
the OS/360 project at IBM, and the problems encountered when developing
an OS for **end-users**. Before getting into the question of whether an
OS end-user is equivalent to a web framework end-user, its useful to
look at the term being referred to, ‘conceptual integrity'.

Wikipedia has a fairly good summary of the term:

    **Conceptual Integrity**

    To make a user-friendly system, the system must have conceptual
    integrity, which can only be achieved by separating architecture
    from implementation. A single chief architect (or a small number of
    architects), acting on the user's behalf, decides what goes in the
    system and what stays out. A “super cool” idea by someone may not be
    included if it does not fit seamlessly with the overall system
    design. In fact, to ensure a user-friendly system, a system may
    deliberately provide **fewer** features than it is capable of. The
    point is that if a system is too complicated to use, then many of
    its **features** will go unused because no one has the time to learn
    how to use them.

Is there Conceptual Integrity?
------------------------------

The Pylons developers, including myself, spend quite a bit of time
deciding what goes into Pylons, and what does not. Pylons is in fact
very very small at its core due to our refusal to let ‘stuff' into
Pylons that is outside its strictly defined scope. In fact, a great many
comments I get are usually about features people want, but that aren't
in the scope of Pylons to provide. I would argue that this does show
thought has gone into ‘conceptual integrity', in the explicit decisions
made about what is and isn't provided.

The scope of Pylons is to provide a **small, concise, WSGI-driven,
lightweight** framework, that provides the flexibility for a web
developer to use the **best tools for the job at hand** for building
their web **application**. I would argue based on the definition, the
goal of Pylons, and what Pylons has in it now, that it fully meets the
design goal of having conceptual integrity with regards to feature
scope.

While the original blog post I cited above starts with conceptual
integrity, it delves deeply into framework design issues like, ‘Should a
framework pick the ORM for you?'. This is slightly odd in the context of
Pylons, as the default ORM, and template language are chosen, Pylons
merely emphasizes that the choice is yours should you wish to change it
(as `does
Django <http://programming.reddit.com/info/62snf/comments/c02ni9c>`_).

In another misapplied analogy, a parallel is drawn up between having an
opinion on a writing style, to having an opinion on a library. Consider
how odd this analogy is, that the fairly minor effect of adding a
trailing ‘S', should be compared to whether a particular ORM library is
capable of meeting your demands. Should the framework authors decide
whether the ORM meets your demands? Should the framework lose a
significant amount of capability the second its stock ORM fails to
handle your needs? These are interesting questions, well beyond an
attempt to draw a parallel to adding a trailing ‘S' to a word.

Since its clear that Pylons doesn't encroach on conceptual integrity
regarding features that are unused, the next aspect to look at is the
concept of a ‘user-friendly system'. This becomes a little more
difficult to analyze, because it brings into question the expectations
one has of the ‘user-base'. It also shows how the original term of
conceptual integrity was misapplied as another parallel is drawn, this
time one that I think all web developers should be somewhat terrified
by.

Website end-user == Website Programmer?
---------------------------------------

The last parallel, is to compare the programming expertise of a web
developer, to the internet naivety of the website end-user. (Does that
offend any other web developers?) The latter of which is well documented
in various web usability books, such as the “Don't Make Me Think” book.
The underlying concept being:

-  Website users have short attention spans
-  Website users won't use a website that requires thinking
-  Website users have no patience

The thesis of this parallel is that a framework author is somehow in the
superior position of knowing the appropriate library that will work for
your task, and should therefore decide the tools for you. The parallel
applied looks like:

-  Website programmers have short attention spans (ok, I somewhat buy
   this one :)
-  Website programmers won't think about whether the tools at hand will
   accomplish their task
-  Website programmers have no patience (Given the languages you have to
   learn to do anything, I seriously doubt this)

Now, there are quite a few website programmers that don't think about
whether the tools they use, work best for their task. I have seen many
websites that are slow, inefficient, or just not well designed because
of a lack of thinking regarding architecture, and tool choices. I would
not consider these to be website programmers I would want to work with,
nor are they the target audience or ‘end-user' of Pylons. The door is
purposely left open in Pylons, and lit up, with the choice available in
libraries to use with Pylons.

Regarding making decisions, Pylons has choices for all the same
components as Django has decided on:
ORM: SQLAlchemy
Templating: Mako
URL's: Routes
Sessions: Beaker
Caching: Beaker

The main problem apparently being, Pylons has emphasized that there is
choice, that the framework is built so that they **could** be swapped,
should one of these not be the best tool for your web application.

The Pilot System
----------------

    When designing a new kind of system, a team **will** design a
    throw-away system (whether it intends to or not). This system acts
    as a **pilot plant** that reveals techniques that will subsequently
    cause a complete redesign of the system. This second **smarter**
    system should be the one delivered to the customer, since delivery
    of the pilot system would cause nothing but agony to the customer,
    and possibly ruin the system's reputation and maybe even the
    company's.

In response to the original post regarding conceptual integrity, I
submit the issue of the pilot system. Django and other frameworks that
start off with libraries you didn't analyze in regards to your
particular web application, have more than a few times led to pilot
systems (I usually hear about the second incarnation, which was then
done on Pylons).

Where you realize later down the road, “wow, this ORM just can't handle
the data model I have”, which then leads to, “well, since the ORM was
hooked into the XML serializer, the admin UI, the form generator, etc.
there's now no competitive advantage over Pylons… which didn't have
those extras.” Systems with heavy and deep integration of libraries that
may or may not meet your demands, where large parts of the system become
relatively useless should you stop using one part of it, are extremely
prone to being a pilot system.

When your pilot system is done, I invite you to check out Pylons, and
think about what is going to work for your website application.

Notes
~~~~~

Please note that I take deliberate care in referring to Pylons for use
with developing web **applications**, its my belief that Django, and
similar systems in other languages with an ‘app' centric approach like
Joomla, Drupal, etc. are excellent for making web **sites**. While you
can easily make websites with Pylons apps, this is definitely not the
primary use-case emphasized and designed for, so it is harder and less
obvious in many respects than Django.

The other thing everyone should've learned from these posts, is that The
Mythical Man-Month is a rather good book worth reading. ;)


.. author:: default
.. categories:: Thoughts, Rants
.. comments::
   :url: http://be.groovie.org/post/296343628/misapplying-book-terms-pylons-and-the-end-user
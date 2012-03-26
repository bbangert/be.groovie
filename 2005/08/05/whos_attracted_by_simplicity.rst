Who's Attracted By Simplicity?
==============================

I've been reading a lot of various blogs lately, quite a bit of `loud
thinking <http://www.loudthinking.com/>`_ and some `37 signals vs
noise <http://www.37signals.com/svn/>`_ as well. A mantra I see over and
over regards simplicity, and focusing on doing a few things extremely
well. This is reflected in the 37 Signals products,
`Basecamp <http://basecamphq.com/>`_, and
`Backpack <http://backpackit.com/>`_. It also bubbles over into the web
framework these are all built on, `Ruby on
Rails <http://www.rubyonrails.com/>`_.

The Rails framework has a lot of appeal, in large part because of how
easy and simple it makes the vast majority of mundane web programming.
The sacrifice is completely intentional, and summed up with “Convention
over configuration”. This mantra is in the Agile Development with Rails
book, and has been uttered on Loud Thinking as well.

Ironically, the people I know that dislike Rails do so because of the
“lack of flexibility”. Many decisions have definitely been made for you
when you create a Rails application, though I see no harm in this
because every decision follows what most regard as the `best practice
and pattern <http://www.loudthinking.com/arc/000485.html>`_ for that
context.

While Rails and Ruby are skills I'm currently learning, I spend a lot of
time working with Python. The Python programmers I've talked to
generally regard lack of flexibility as very unappealing, and would
happily sacrifice simplicity or making any decisions for the programmer
(I'm referring to Python toolkits/frameworks intended for use by
programmers). The assumption is that the programmer will read how to use
the tool, see that there's a half dozen ways to use it, and plug it in
as he best sees fit.

Having more ways to use it is a good thing, with no clear direction on
any sort of *best practice or pattern* provided typically. Strangely
enough the majority of toolkits and web frameworks for Python generally
have rather small groups of users. Is this a coincidence?

My favorite framework, `Myghty <http://www.myghty.org/>`_ recently got
the very cool ability to `call module components
implicitly <http://www.myghty.org/docs/modulecomponents.myt#modulecomponents_flavor>`_
. This added two more mechanisms of dispatch control to the resolver,
very powerful stuff. It's also rather confusing, not because how it
works is actually difficult, but because now the way **you should use
it** has become even less certain with the added choices.

The fact that there's so many ways to use it has definitely hampered the
ability of people to understand it and use it effectively. The powerful
flexibility has made it powerful though, for totally different paradigms
to be built on top of it. For example, you could replicate the
pipelining methodology that `AxKit <http://axkit.org/>`_ uses by
configuring the resolver to pass the different extensions through
recursively until an “end” is signaled. Or you could configure Myghty to
dispatch control to a Controller exactly how Rails does (which I've
worked on doing).

In the end though, why should I waste my time replicating what another
framework already has? I've got to admit, even though I know how to pick
up the tools and plug them in, I'm still attracted to simplicity.


.. author:: default
.. categories:: Python, Rants, Rails
.. comments::
   :url: http://be.groovie.org/post/296353652/whos-attracted-by-simplicity
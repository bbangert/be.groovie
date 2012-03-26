Making Decisions for Others
===========================

*Please Note:* Reading the last post would help greatly for this one,
and this post does end up `comparing aspects of Django with
Rails <http://www.jrandolph.com/blog/?p=9>`_ in terms of making
decisions rather than actual usage.

As I mentioned in my last post, Rails has been greatly helped by the
decisions it makes for you. It decides the layout of your application
directory, the directories you put stuff in, where you put what parts,
etc. These decisions thankfully were done by someone familiar with good
application design and had most likely even read `Martin
Fowler's <http://www.martinfowler.com/>`_ `Refactoring to
Patterns <http://www.martinfowler.com/books.html#r2p>`_.

What results is a clean, well thought out application that you didn't
even need to think out very much. Before you know it, you fall into
these useful and powerful design patterns without even thinking about it
(I'd hope you would at least, they're good patterns for a reason).

A lot of web frameworks make the assumption you are familiar with these
patterns already, will setup your application to follow them, and use
them in a way that makes sense. Part of the reason for this is because
some web framework developers are rather appalled at the thought of
making these decisions for the framework user. To be making those
decisions for the framework user is looked at as holding their hand, and
typically the programmers who write frameworks don't need any hand
holding and don't expect their users to either (I'm assuming this based
on the frameworks I've tried).

For example, during `Ian Bicking's <http://blog.ianbicking.org>`_ `test
run with
Rails <http://blog.ianbicking.org/more-thoughts-on-ruby-on-rails.html>`_
he noted that having such a directory hierarchy setup for him put him
off a little and mentions people arguing about file layout. I've seen
very little, if anyone else, even comment on the directory structure
that Rails lays out for you. The other irony of this particular post is
that a lot of the stuff Ian finds “wrong” about Rails is actually Ruby's
“fault” (Implicit passing of names, mix-in's, etc.). But moving on….

Ian clearly doesn't want to lay down the law for users of his software,
neither do other Python web framework developers. Having choice in how
you lay out your application, with no clear direction what goes where,
is considered a good thing. I don't think there's anything wrong with
this approach, **if** the users you're aiming your framework at are
expected to be experienced, professional, programmers that are quite
familiar with web applications and what works best for them. This does
mean the audience will not be that large, and I think thats clearly
reflected in the small communities most Python web frameworks have.
While their communities are small, I've found them to be highly skilled
and you get great answers to questions on their respective mailing
lists.

The one Python web framework that has almost overnight gone from hardly
any users, to at least a few dozen (probably more, but even a few dozen
is quite good for a Python web framework), is
`Django <http://www.djangoproject.com/>`_. Django makes a **lot** of
decisions for the user, more so even than Rails by a pretty good amount.
While Rails was designed as a web application toolkit, and extracted
form a large webapp, Django is designed more as a CMS web application
toolkit as its been extracted from newspaper-style web sites. Thus, many
of the decisions Django makes for you assume you will want users,
user-access to the database objects, etc.

The question is, if someone else is making decisions for you, how
important is it that they be **good decisions**?

One of the decisions the Django team made originally irritated me quite
a bit. The Django framework is probably about 95% MVC in nature. It has
database files that clearly are acting as Models (which it calls
models), logic oriented files traditionally called Controllers (that it
calls views), and template files that display the results to the user in
a typical View role (though Django calls them templates).

The FAQ on the Django site notes that if you squint, sure enough the
observations I just made do pop out, however because of the 5% non-MVC I
mentioned they decided the names didn't work. Rather than calling them
by what they obviously were (or closest to), they swapped around names
in a way that I think is bound to confuse Django programmers when they
go into a real MVC environment and tell someone they edited the view
when in fact it was the controller. If they had come up with completely
different names that didn't relate to the MVC paradigm at all, I think
that would help to avoid later confusion on the part of a Django user.

Despite the naming of these parts, the decision made for the user is
clearly for a MVC-style (or influenced) environment which I think is
great ( **please change the naming! ;)** ). So what is the point of this
whole thing?

I think its a good thing for developers of toolkits and especially
frameworks to make some more decisions for the end-programmer of their
work. This makes it easier for not so experienced programmers to get
started quickly, and if you're using a good design pattern even the
experienced dev's wont have anything to complain about. The two
frameworks that currently are getting a lot of attention make a lot of
decisions for the programmer using them, and this definitely increases
the user-base (assuming you want a large user-base). Even though I know
good practices on laying out stuff, it makes my life that much easier
when its done for me.


.. author:: default
.. categories:: Code, Myghty, Python, Rails, Rants
.. comments::
   :url: http://be.groovie.org/post/296353565/making-decisions-for-others
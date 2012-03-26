Porting Routes from Rails
=========================

I've begun porting the
`Routes <http://manuals.rubyonrails.com/read/chapter/65#page164>`_
system from `Rails <http://www.rubyonrails.com/>`_ over the last
weekend. It's definitely been a good brain workout, as the one `Nicholas
Seckar <http://wiki.rubyonrails.com/rails/show/NicholasSeckar>`_ wrote
that drives Rails is quite a brain-fuck. His version actually does quite
a bit of code generation based on the routes one sets up. At first I
tried to do a fairly direct port of the Ruby code behind this to Python,
but my brain just couldn't wrap itself around what he was doing (He's
told me that quite a few others have said the same).

This left me kind of discouraged, and I left the project (more of a
thought at that point) alone and proceed to replicate most of Rails
ActionMailer in Python instead. Partly because I liked how ActionMailer
assembled mail, and partly because after hearing a talk by `Alex
Martelli <http://www.oreillynet.com/cs/catalog/view/au/918>`_ on
Metaclasses and other Python “black magic” I just had to find some
excuse to use a metaclass.

Why not just use Rails?
-----------------------

Now, before anyone starts yelling “Just use Rails!” at me, I should
explain something. I **am using Rails**, and I rather like it. However,
most companies wouldn't be too thrilled with their employee's changing
the entire codebase of the company every year when the latest, greatest,
way to write webapps comes along. Plus, since I already use Python
extensively, a lot of stuff that makes life pleasant in Rails-land can
be fairly easily adopted to Python-land.

Do I really want to re-write 5k or more lines of Python libraries in
Ruby just so I can use Rails? Should the entire web team learn a new
language and framework just because its a bit better than the current
way? The time spent doing all this wouldn't be paid off for at least a
year or more, if that (and maybe some other language+framework will be
the new thing by then). When it comes down to normal Python libraries, I
don't save any lines of code by moving to Ruby. So in the end, it makes
sense to adopt part of Rails that make my life easier.

In Case You Didn't Know
-----------------------

The `Routes <http://manuals.rubyonrails.com/read/chapter/65#page164>`_
system from Rails is used by Rails in a lot of functions. Virtually all
functions that require a URL to be written
(`url\_for <http://api.rubyonrails.com/classes/ActionController/Base.html#M000170>`_,
link\_to, form\_tag, etc) all use the Routes system to figure out what
URL to put in place.

In the Python world, as far as I know (and I've looked quite a bit),
there is **absolutely no web framework that will convert from
controller/action -> URL**.

**Update (9/26/05):** *Phillip J. Eby rightfully pointed out that other
Python web frameworks can do this. I should've been more specific in
that none of them operate in this manner. Since putting word out about
Routes I also found out Aquarium can designate routes for
dispatch/generation in this manner, however Aquarium cannot do automatic
route lookup to find the shortest URL. This ends up hard-coding the
template URL to the route.*

Plenty of web frameworks are happy to convert a regular expression into
a dispatch command and let you tweak it
(`Myghty <http://www.myghty.org/>`_,
`Django <http://www.djangoproject.com/>`_, etc.) but they are all
helpless if you want to generate a URL from the commands they used to
dispatch.

Progress
--------

Currently, I have URL generation (controller/action -> URL) and URL
recognition (URL -> controller/action) **working and passing all the
tests** that I've ported over from the Rails route testing. Since my
version of Routes is independent of the framework, its my hope that
multiple Python web frameworks will be able to incorporate the finished
Route system I'm building. The URL -> controller/action results in a
dict, that the web framework can choose to deal with as it pleases.

The first framework I plan on integrating this with is
`Myghty <http://www.myghty.org/>`_ as the resolver system is fully
user-customizable, no hacking on the framework source is needed to plug
it in. The dispatch model will then follow Rails and make the same
decisions for the user (controller goes in appdir/controllers/,
name\_controller.py, etc.) that Rails does.

Once I add a few more tests, and try and clean up my code some, I'll put
it out there. I'm considering a BSD license right now, in the meantime,
here's a sample:

::


    >>> from routes import Mapper
    >>> m = Mapper()
    >>> m.connect('page/:id', controller='content', action='show_page', id =1)
    >>> m.connect(':controller/:action/:id')
    >>>
    >>> m.generate(controller='content',action='index')
    '/content'
    >>> m.generate(controller='content', action='show_page')
    '/page'
    >>> m.generate(controller='content',action='show_page',id=4)
    '/page/4'

Speed
-----

My implementation choice was to rely heavily on the speed of set
operations using the built-in set/frozenset functions in Python 2.4.
Under Python 2.3 the sets module provides an ImmutableSet which I've
also tested my port with. I was actually quite impressed with how fast
the sets module is in 2.3, but there is a **three-fold speed increase**
using Python 2.4 built-in sets.

Even under 2.3 the speed should be more than sufficient for most
applications, plus, this is a first revision of the code. I'd hardly
expect it to be the peak of efficiency right now.

What's Missing
--------------

I currently haven't implemented memory of the match that got to the
current page. Rails does this so if you're inside a template that was
matched by ‘post/show/20' and you call ``link_to :id => 30`` it would
give you a url of ‘post/show/30'. It does this by remembering the match
that got you there. Since this match would be setup inside the web
framework, I'm considering how to implement it without tying one to a
specific framework.

The other noticeable feature missing is Named Routes which act as a sort
of macro on top of the normal url generation calls. This shouldn't be
too tough to add at a later point.

Parting Thoughts (ala Jerry Springer)
-------------------------------------

Before you submit some comment saying I'm an idiot for porting this and
should drink more Ruby kool-aid, **don't**, please. I'm already drinking
it, and it tastes quite good. But just because I like Ruby, doesn't mean
my taste for other languages has changed. Languages have their strong
points, and they have things they lack (Yes, they both lack some
things). When I'm writing Python, my web framework of choice is so very
close to perfection for me, Routes is one of those things that would
make it that much sweeter.

If you're interested in adapting this to your Python web framework and
want to start playing with the code I have so far, `send me an
email <mailto:ben@groovie.org>`_ and remember boys and girls, be safe.


.. author:: default
.. categories:: Python, Code, Rails
.. comments::
   :url: http://be.groovie.org/post/296353404/porting-routes-from-rails
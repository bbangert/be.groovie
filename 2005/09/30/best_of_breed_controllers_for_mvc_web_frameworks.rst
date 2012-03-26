Best of breed Controllers for MVC web frameworks
================================================

I've been doing a lot of comparisons and research into various Python
web frameworks lately, mainly focused on MVC oriented frameworks. Some
of them have templating languages they come with, some not so much. The
thing I have started to notice is how similar the Controller in them all
is starting to look. First though, lets see what they all can do when it
comes to the Controller.

For comparison's sake, I'm bringing out some examples using
`CherryPy <http://www.cherrypy.org/>`_,
`Myghty <http://www.myghty.org/>`_,
`Bricks <http://www.pythonweb.org/doc/bricks.doc.html>`_,
`Aquarium <http://aquarium.sourceforge.net/>`_, `Ruby on
Rails <http://www.rubyonrails.com/>`_, and
`Django <http://www.djangoproject.com/>`_.

Please note I'm not including frameworks built using any of the ones
mentioned as their Controller looks pretty much the same. I'm also not
an expert in all these frameworks as I only have so much time in the
day, so if I seem vague on something its because I don't know for sure.
Feel free to comment (or correct) and clear up any vagueness I express.

Dispatch and Responder Styles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

All the frameworks I've mentioned implement a style of object publishing
(sometimes referred to as dispatch-style) that maps to the URL coming
in. If you have another name you want to call this, go for it, I haven't
seen anything consistent on what to call this stuff.

Three different styles seem to exist that make sure an object responds
to the URL:

#. User creates a regular expression to explicitly map a URL to an
   object (\*Explicit Mapping\*)

   -  ``(r'^polls/(?P<poll_id>\d+)/vote/$', 'myproject.apps.polls.views.polls.vote')``
      (from Django tutorial)

#. Object is mapped out according to the URL (\*Implicit Mapping\*)

   -  /admin/login/hello/ —> admin/login.py/hello() (Myghty)

#. Programmatic rule set determines object that responds (\*Programmatic
   Mapping\*)

   -  map.connect ‘:controller/:action/:id' (Rails)
   -  m.connect(':controller/:action/:id')
      (`Routes <http://routes.groovie.org/>`_)

In the Python world, three different styles also exist for how that
object (or function) is defined. The first one is most popular, and is
similar to how Rails sets up the Controller. They are:

#. Create a class inheriting from a Controller object, methods of the
   class instance are called to respond (\*Class-method\*)
#. Create a callable object that responds (\*Callable\*)
#. Create a function thats directly called (\*Function\*)

Note that the last 2 are functionally equivalent for the most part,
however a callable object has the typical advantages (or disadvantages)
of persistence in some web frameworks, as such if a web framework only
shows one of those styles I won't mention the other. Curious what
frameworks use what styles from the above two sets?

For this listing, I'll refer to the mapping scenario as *dispatch-style*
and the method for defining the response as the *responder-style*, also
please note that some frameworks support multiple dispatch-styles and
responder-styles.

Aquarium:

-  Dispatch-Style Mapping \ :sup:`1`\ :

   -  Explicit, Implicit, Programmatic

-  Responder-Styles:

   -  Callable (Though it looks almost exactly like the Class-method
      style)

Bricks:

-  Dispatch-Style Mapping:

   -  Implicit

-  Responder-Styles:

   -  Class-method

CherryPy:

-  Dispatch-Style Mapping:

   -  Explicit (Not with regexp's though, each class is attached off the
      root to determine what URL leads to it)

-  Responder-Styles:

   -  Class-method (Must be explicitly exposed with @cpg.expose)

Django:

-  Dispatch-Style Mapping:

   -  Explicit

-  Responder-Styles:

   -  Function (Packaged in the same module if they're related)

Myghty:

-  Dispatch-Style Mapping \ :sup:`1`\ :

   -  Explicit, Implicit, (Programmatic with Routes in upcoming 0.99)

-  Responder-Styles:

   -  Class-method, Callable, Function

Rails:

-  Dispatch-Style Mapping \ :sup:`1`\ :

   -  Programmatic

-  Responder-Styles:

   -  Class-method

\ :sup:`1`\ : User can create custom dispatchers to determine responder
object

Who did it first?
^^^^^^^^^^^^^^^^^

If we throw in two more frameworks that utilize CherryPy, like
`Subway <http://subway.python-hosting.com/>`_, and
`TurboGear <http://www.turbogears.org/>`_, we can start to see that
using a responder-style of Class-method is pretty popular. What's even
more interesting is that all the Class-method Controllers look
remarkably similar, and I don't think its because they're copying each
other.

The Aquarium project appears to be approximately 4 years old now, but
from looking at the mailing list had little or no users until only 2-3
years ago (One poster from 2001 `describes his aquarium plants turning
brown… <http://sourceforge.net/mailarchive/forum.php?thread_id=3854776&forum_id=38053>`_).
From the sourceforge changelogs, the Controller stuff was added with 1.4
release in 2004. CherryPy has been around for 3+ years and I'm presuming
it had the Controller stuff in it from the get-go as it seems a pretty
core function of CherryPy. Rails has been out for a year or so, and was
used in a form internally for BaseCamp for awhile predating that.

If you really want to trace back this style of Controller, you'd most
likely find yourself looking at [STRIKEOUT:Java] Python code (`See
Phillip J. Eby's comment
below </articles/2005/09/30/best-of-breed-controllers-for-mvc-web-frameworks#comment-49>`_).
**I'm really just trying to point out here, that even if one of these
projects saw something they liked from the other, none of them were the
originators**. They all took a good concept, and implemented it
differently, though they've all started to look remarkably similar.

A Controller Line-Up
^^^^^^^^^^^^^^^^^^^^

So lets take a look at some of the examples on the pages of each
respective website. Django is the only one that really stands out, as
they're not using a Class to contain the methods, rather they're
grouping them as plain functions inside a module.

Aquarium
''''''''

::

    class BaseController(Controller):

        def call(self, callNext, *args, **kargs):
            “”“Save a reference to myself in ctx.controller.”“”
            self._ctx.controller = self
            callNext(*args, **kargs)

        def doMessageAddAction(self):
            “”“Add a new message.
            ...does a bunch of stuff…

I mentioned that it was Callable but functioned in a way like a
Class-method. This appears to be because Aquarium puts a context and
maybe other initialization stuff per request in the ``__call__`` bit,
then has it actually calls a different method to respond.

Bricks
''''''

::

    from bricks.controller.crud import CRUDfrom bricks import user

        class Test(CRUD): 
        # Override the default delete() method
        def delete(self, rowid):
            return CRUD.delete(self, rowid)
        delete.expose = user(level=1, app='app')

        controller = Test('todo')

Bricks adds an interesting ability here by attaching function attributes
to indicate what authorization is needed to execute the function called.
Some of the other frameworks shown here do similar things through
function decorators.

CherryPy
''''''''

::

    from cherrypy import cpg

        class HelloWorld:
        def index(self):
            return “Hello world!”
        index.exposed = True

        cpg.root = HelloWorld()

Notice that the class instance is attached to the location off cpg.root
thats desired. To map a URL to a class instance farther down, say under
``/booga`` instead of ``/``, you'd do that last line like so:
``cpg.root.booga = HelloWorld()``

Pretty handy I think, and it beats writing regular expressions (though
doesn't appear as flexible). One of the reasons I prefer the
Programmatic dispatch-style. Moving on..

Django
''''''

::

    from django.core.extensions import get_object_or_404, render_to_responsefrom django.models.polls import choices, pollsfrom django.utils.httpwrappers import HttpResponseRedirect

        def vote(request, poll_id):
        p = get_object_or_404(polls, pk=poll_id)
        ... does a bunch more stuff to use Django-supplied functionality…

If you imagined the functions inside a class, instead of a module, it'd
look rather similar to the others….

Myghty
''''''

::

    class HelloWorld:
        def doit(self, m, **params):
            m.write(“hello world!”)

        helloworld = HelloWorld()

At this point, the similarity between Bricks, CherryPy, and Myghty
should be pretty obvious. Aquarium is close as well, while Django is
only a wee farther from what's appearing to be the norm.

Rails
'''''

::

    class HelloController < ApplicationController
        def index
            return render :text => "hello world!"
        end
    end

Doesn't look too different from some of our Python MVC frameworks…

What it All Means
^^^^^^^^^^^^^^^^^

I have no idea. Really, I just thought it was fascinating that these
different frameworks started looking so similar. Some of them have been
incredibly similar before others, but obviously these approaches catch
on and find themselves adopted into other frameworks.

I do start to wonder at what point they'll be similar enough that the
barrier to switching web frameworks is narrowed down to only a few dozen
lines of code to change here and there. Sure, going to/from Rails is
going to be tough as that also means a language change, but for Python
programmers tempted by a feature a different web framework offers I
won't be surprised to see more people hopping back and forth.

With regard to the Python web frameworks, none of them appear to agree
on a template language. Several of them use Cheetah, some use Myghty's
template abilities, one uses `Kid <http://kid.lesscode.org/>`_, and
several of them have their very own template language.

It's also interesting to consider whether or not having more possible
dispatch/responder styles is beneficial or detrimental to the popularity
of a specific framework. Rails creator `David
Hansson <http://www.loudthinking.com/>`_ purposely includes only one
style for each as he emphasizes with a concept known as **convention
over configuration**. He provides defaults for pretty much everything,
and following conventions makes it easier to write code as it enforces a
consistent programming and naming style. I can't help but notice that of
the frameworks I mentioned above, the ones with less (apparent) options
and better defaults tend to have more users (With the exception of
Bricks as its still in alpha).

You might have noticed I designated Rails as being capable of
user-programmed dispatching. While Rails uses its routes system by
default, the thing people miss is that they're *just defaults*. You can
get in there and totally alter the way it works if you want, Ruby
doesn't completely close classes so you could just re-open them and
override any aspect of its dispatch system you like.

I think this a valuable lesson that some of the more “verbose” examples
above might want to consider. If there's lines of code in a controller
that you have to put in there every-time, find a way to make it the
default case so that boiler-plate isn't needed. It only needs to be a
default, an advanced programmer will know how to override it should they
need to. There's obvious limitations to this since things work
differently in Python, but there's still Python ways to do it in a way
that feels “right”.

For the Python Web Frameworks I missed
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I know, I didn't cover `SkunkWeb <http://skunkweb.sourceforge.net/>`_,
`Spyce <http://spyce.sourceforge.net/>`_,
`Snaklets <http://snakelets.sourceforge.net/>`_,
`Webware <http://www.webwareforpython.org/>`_ and more. Please feel free
to add the relevant information regarding your framework in the
comments. It'd be helpful if you could indicate what Dispatch-Styles and
-Responder-Styles your framework supports.

If I failed to properly cover one of the above frameworks, bringing that
to my attention is most appreciated.

The comment system supports the
`Textile <http://textism.com/tools/textile/index.html>`_ format.


.. author:: default
.. categories:: Code, Myghty, Python, Rails, Ruby
.. comments::
   :url: http://be.groovie.org/post/296349717/best-of-breed-controllers-for-mvc-web-frameworks
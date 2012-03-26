Fragmenting A Framework Userbase
================================

I've been thinking a lot lately about web programmers and the web
frameworks they choose, or don't choose, and why. I'm mainly going to
talk about Python Web Frameworks as the majority of them have small
communites, and possible reasons this could be.

I only started using Python for web development about a year ago, and it
took me about a month to settle down on a web framework. In that time, I
looked over at least a dozen different frameworks. There's so many
python web frameworks, quite a few people have actually setup `entire
pages <http://www.boddie.org.uk/python/web_frameworks.html>`_ and
`sections of their site <http://wiki.python.org/moin/WebProgramming>`_
just to covering them all.

I think part of the reason for the proliferation of frameworks is
because of the nature of many Python programmers, as I briefly mentioned
in a prior post on `Making Decisions for
Others <http://www.groovie.org/articles/2005/08/05/making-decisions-for-others>`_.

The recent appearence of Django on the Python web framework scene I'm
sure has quite a few other Python web framework developers wondering,
“Why isn't the web framework I made getting this much attention and
use?”

A Common Base
^^^^^^^^^^^^^

Many of these same people would like to blame it on hype and good
marketing. While that will certaainly boost initial usage, I don't
believe it will create a lasting user base. I think a huge driving
factor behind Rails and Django, besides for the hype and marketing, is
the fact that both of them make a lot of decisions for you. These
decisions start the users all off at a common base of understanding.

The linear progression from:

#. Never used the framework
#. Wrote the tutorial app
#. Wrote their own basic webapp
#. Wrote an advanced web application

Makes it easy for people a step or two up, to help other new users join
them. Because the steps they all take are the **same steps** to achieve
greater understanding of the web framework, they can easily help new
users get to where they are. Most, if not all the other Python web
frameworks I've seen are so flexible its hard to have a common base of
understanding amongst new users. The process looks more like this:

#. Never used the framework
#. Researched the frameworks options and choices to find a possible
   starting point
#. Wrote a basic web application using method X
#. Wrote an advanced web app using method X

The flexibility of the web framework becomes an obstacle to a strong
user-base in this case, as it fragments the users by the methodology
they're using to build their webapp. It also reduces the common
re-usable components available, since different users will utilize
different options of the framework and have possibly very different
starting points.

Have a Tutorial Application
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Also lacking from many Python web frameworks is a clear and obvious
Tutorial application. Ideally the front page of a Python web framework
should be an obvious path to become an experienced user of said
framework. Such as:

#. Install the framework
#. Write a basic tutorial application
#. Look here/there for instruction as need to write your own more
   complex application

A good tutorial should leave a user feeling confident that they know how
to install and start with a common base for writing their own web
applications. It's also amazing how many problems people can have just
getting a framework installed and running in a minimal configuration.
Having a tutorial that leaves them with a functioning web application
gives them a big leap forward.

Since many users will do the first tutorial web application, other new
users can give help to even newer users that run into a problem. This is
where the common base effect really provides some power.

Methods of Fragmentation
^^^^^^^^^^^^^^^^^^^^^^^^

The Python frameworks I've tried and used have fragmented their starting
points and users in various ways. All of them as a result of their
“flexibility and power”. Here are a few common trends of fragmentation
I've seen:

-  Let the user choose various template language schemes (Use ZPT, or
   Cheetah, or…)
-  Let the user choose from web paradigm (MVC, page-driven, pipelined…)
-  No base or example configuration for a fully working webapp (So
   everyone sets up their first application slightly differently)

The last one I listed, is probably the easiest to solve, especially with
useful web framework template creators like `Python
Paste <http://pythonpaste.org/>`_. Obviously, removing the first two
will be seen by many Python web framework developers as undesirable. I
think it'd really help the users though, as it gives them more in common
with each other. If they all use the same paradigm, and the same
template language with your framework, their ability to help each other
increases and they feel confident they made the “right” choice as well.

Assumptions
^^^^^^^^^^^

I've assumed for the purpose of this post, that Python web framework
makers are interested in having a large user-base. This isn't always the
case, I'm sure some just want a small, very experienced user-base that
isn't going to be asking basic questions like, “I can't connect to my
database like you show in the tutorial”.

I can understand that, but for the other Python web framework makers out
there, try and consider some of the things I mentioned. There are a
**lot** of Python coders out there, and a lot of them can live without
having 4 template language choices and 2 different design paradigms. So
when adding that feature that'd let people get so much “power and
flexibility”, will it fragment your user-base?


.. author:: default
.. categories:: Python, Thoughts, Code
.. comments::
   :url: http://be.groovie.org/post/296352345/fragmenting-a-framework-userbase
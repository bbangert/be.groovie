Routes 0.2 released
===================

`Routes <http://routes.groovie.org>`_ 0.2 has been released. The
change-log is pitifully short:

-  Added prefix option
-  Fixed Python 2.3 bug with thread-local singleton

But hey, its a small package to begin with so what the heck. Though its
only 0.2 I'm rather pleased with it so far, its performance is great and
quite reliable so I'm using it in production environments already.

If you haven't been following my blog long, Routes is a feature-complete
implementation of Rails routes system. I talk more about my `reasons for
re-implementing Routes in Python in an earlier
post </articles/2005/08/08/porting-routes-from-rails>`_ so I won't
repeat them all here.

It's fairly unique in the Python world as it will do a route lookup
search to turn a dictionary back into the URL (URL Generation) that will
ensure the same values are created. This allows you to generate URL's
from inside your web pages and easily add new URL schemes without
touching all your web pages.

The Routes package is aimed directly at integration with Python web
frameworks that support the MVC style paradigm as it returns a
controller and action value with the assumption your framework will know
what to do with it.

Tired of writing big regexp's to match URL's to a class/method for
dispatch in your webapp? Pester the framework creator to integrate
Routes. :)

Here's some Python Web Frameworks that currently or will shortly have
Routes support/integration:

-  `Aquarium <http://aquarium.sourceforge.net/>`_ has a URL Connector
   that uses Routes. Not sure if its been added to the core or only
   exists as an add-on right now.
-  `Myghty <http://www.myghty.org/>`_ will have Routes integration
   packaged with it in 0.99 which is on track to be released this week
   hopefully. It will also bring `Python
   Paste <http://pythonpaste.org/>`_ support and integration which will
   bring a whole bunch of goodies to webapp developers and users. (Note
   that Python Paste requires Python 2.4)

I'll be talking more about `Python Paste <http://pythonpaste.org/>`_ and
why you should care later this week. Any comments/suggestions on Routes
are greatly appreciated.


.. author:: default
.. categories:: Python, Code, Myghty, Routes
.. comments::
   :url: http://be.groovie.org/post/296351741/routes-0-2-released
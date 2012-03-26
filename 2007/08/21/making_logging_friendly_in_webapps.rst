Making logging friendly in webapps
==================================

Finding out whats going on in an application is always a key point when
trying to figure out what's happening when things don't go the way you
expect. In these kind of annoying situations, following the log of how
your request mapped in and what was going on can save a significant
amount of time. TurboGears has had great logging throughout it, and with
0.9.6, Pylons add's the same thorough logging.

But once the entire request is mapped out, it can be a real chore to
track through them, toggle modules you want and don't want logging for,
etc. `Chainsaw <http://logging.apache.org/log4j/docs/chainsaw.html>`_
has had excellent graphical support for navigating logging output, and
with the help of Phil Jenvey's
`XMLLayout <http://pypi.python.org/pypi/XMLLayout>`_ package its easy to
output logging statements in a format for use with it.

With the `recently updated Chainsaw section in the Pylons logging
docs <http://wiki.pylonshq.com/display/pylonsdocs/Logging#lumberjacking-with-log4j-s-chainsaw>`_,
you too can be lumberjacking with Chainsaw.

And of course, a shot of Chainsaw in action:
|image0|

.. |image0| image:: http://groovie.org/images/Pylons_Stack-Chainsaw-OSX.jpg


.. author:: default
.. categories:: Python, Pylons
.. comments::
   :url: http://be.groovie.org/post/296343960/making-logging-friendly-in-webapps
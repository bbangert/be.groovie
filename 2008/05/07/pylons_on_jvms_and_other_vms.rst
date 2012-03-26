Pylons on JVM's (and other VMs)
===============================

Phil Jenvey has been making some great progress getting all the
components of Pylons running on Jython, and posted a `good write-up of
the remaining
work <http://dunderboss.blogspot.com/2008/05/you-must-construct-additional-pylons-on.html>`_
being done. It's interesting to note that one of the big issues will
affect any web framework on Jython, not just Pylons. That is, the reload
time when used in development to restart the server.

While I don't plan on deploying Pylons apps in WAR files anytime soon,
its nice to see Jython emerging as a candidate for deployment.


.. author:: default
.. categories:: Python, Pylons
.. comments::
   :url: http://be.groovie.org/post/296342772/pylons-on-jvms-and-other-vms
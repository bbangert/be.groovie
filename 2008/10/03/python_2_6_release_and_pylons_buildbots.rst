Python 2.6 release and Pylons buildbots
=======================================

`Python 2.6 <http://python.org/download/>`_ came out yesterday, so I
figured I might as well see if `Pylons <http://pylonshq.com/>`_ works on
it. Pylons already has a set of `buildbots <http://buildbot.net/trac>`_
that `builds Pylons along with some of its
dependencies <http://pylonshq.com:8010/>`_, so it was fairly trivial to
add another builder to verify things ran swimmingly on Python 2.6.

Unfortunately, as one can see looking at the build results, things
weren't so great. It appears that `nose had a Python 2.6
incompatibility <http://code.google.com/p/python-nose/issues/detail?id=161&colspec=ID%20Type%20Status%20Priority%20Stars%20Milestone%20Owner%20Summary>`_
which is used to run all the various Pylons tests, meaning that they all
failed so far mainly because the testing tool was Python 2.6
incompatible.

Making Buildbot nicer
---------------------

While I wait for the new nose to be released, I did at least discover a
little bug in my new webapp that provides a nicer view of the buildbot
result set. I've been fairly displeased with the lack of conciseness of
buildbot's waterfall display for awhile, and noticed that if only
buildbot had a `few more xmlrpc
methods <http://www.bitbucket.org/bbangert/buildbot-xmlrpc/overview/>`_
then it'd be trivial to build my own more kind interface.

I should note that the waterfall display isn't totally horrible, the
Django folks `spiced their builders up with some CSS
work <http://buildbot.djangoproject.com/>`_…. which reminds me, it isn't
looking very good for those running on trunk at the moment. ;)

So after making my `own little buildbot
fork <http://beta.pylonshq.com/buildbot/index>`_ to add some additional
custom xmlrpc methods to, I've come up with my own buildbot status
viewer. I'm sure a more talented designer could spice it up even more,
but it gives me the pertinent data I'm interested in without all the
boring “builder connected, builder took a vacation” messages that cloud
up the waterfall. Also, rather than displaying the cryptic “shell\_21
failed” messages, it actually uses the names I attached, and shows them
quite clearly for the last build.

I'll submit some patches for these xmlrpc additions to buildbot when I
get the time, but right now I mainly needed the Mercurial 1.0 hook
compatibility (that was broken for quite awhile in buildbot), and a
fairly specific set of information from the xmlrpc methods that I wasn't
sure others would want.

I'm looking forward to trying out the new nose so that I can hopefully
verify Pylons is good to go on Python 2.6 as Phil Jenvey's been working
tirelessly on patches to Beaker and other dependencies to make them 2.6
compatible. Any suggestions or thoughts on improving my buildbot viewer
are welcome. :)


.. author:: default
.. categories:: Python, Code, Pylons
.. comments::
   :url: http://be.groovie.org/post/296329162/python-2-6-release-and-pylons-buildbots
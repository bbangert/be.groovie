Deploying Python web apps with toppcloud
========================================

`Ian Bicking <http://blog.ianbicking.org/>`_ recently released a rather
interesting package called
`toppcloud <http://bitbucket.org/ianb/toppcloud/>`_ that aims to tackle
what I see as a growing need for those of us deploying Python webapps.

I was actually interested in easing my own deployment woes before I saw
Ian’s announcement about his package, and was halfway through a rather
hefty amount of research on automating server deployments with tools
like `Chef <http://wiki.opscode.com/display/chef/Home>`_ and
`Puppet <http://reductivelabs.com/trac/puppet/>`_, but toppcloud is a
bit different. It not only tackles provisioning a new system on the fly
from the ‘cloud’ (using
`libcloud <http://incubator.apache.org/libcloud/>`_), but it also
handles *easy Python (and now PHP) web application deployments*.

With such a tantalizing set of goals, I couldn’t really resist getting
my feet wet. Boy am I glad I did. `PylonsHQ <http://pylonshq.com/>`_ is
now running with toppcloud, and I won’t be surprised when more people
get it running for them. When many shared hosting providers are $5-10 a
month, its rather nice to pay $10/mth for an automatically configured
VPS, with one-command deployments. Though of course, unless you go to
quite a bit of work yourself, most shared hosting providers don’t have
one-command deployments for you.

Before I continue on to describe how I setup
`Kai <http://bitbucket.org/bbangert/kai/>`_ - the source code behind
PylonsHQ - I should provide a few caveats about using toppcloud:

-  toppcloud is **alpha software**, there’s no releases of it yet, you
   will be checking it out from source code
-  currently, only Rackspace Cloud is known to be working, though since
   it uses libcloud, *in theory*, any cloud providers that it supports
   should be usable
-  toppcloud is changing rapidly, be ready to keep up on the commit log
   to see whats changing
-  there are **no unit tests**, most likely because its very tedious to
   make the rather significant amount of mock objects required to test
   the various local/remote commands and the fact that its changing so
   fast the tests would probably be obsolete in a week

toppcloud philosophy
--------------------

I’m half guessing here, based on talking with Ian and reading the docs
myself, but the philosophy of toppcloud is around providing a common
deployment platform, ala Google App Engine, except of course with
Postgres or other ‘services’ that you can request to use. At the moment
the only services that toppcloud comes with is CouchDB, Files (to
store/serve files for your app on the filesystem), and Postgres
w/postgis extensions. For those diving into the source code, it
shouldn’t be too hard to see how to create additional services and I
hope to see more get added as people get more interested.

Therefore, toppcloud is not expected to be everything to everyone, it is
expected to be at least an 80+% solution to deploying web apps in a
Google App Engine style ease-of-deployment process. toppcloud itself
then ensures that depending on what service you asked for, its setup and
ready for use on the server when your app is deployed.

If that sounds like something you’re dying to try out, you’re in luck!

Setting up a Pylons App
-----------------------

I’m not going to mention how to check out the toppcloud source, except
to mention the directions are in the

::

    /docs/index.txt

file in the toppcloud source (which should be read in its entirety!).
Once you have toppcloud installed on your computer, getting from zero to
running website on VPS is remarkably quick:

#. ::

       $ toppcloud create-node --image-id=14362 baseimage

   Wait until email arrived indicating that server is up and ready

#. ::

       $ toppcloud setup-node baseimage

   Server is now all setup to run web apps!

#. ::

       $ toppcloud init myapp

   Create an app to deploy to our server

#. ::

       $ source myapp/bin/activate

   Activate the virtualenv used for this app

#. ::

       $ pip install Pylons

#. ::

       $ cd myapp/src

#. ::

       $ paster create -t pylons awesomeapp

   Create our Pylons app, or check out an existing one from your VCS
   here

#. ::

       $ cd ../..

#. ::

       $ ln -s myapp/src/awesomeapp/awesomeapp/public/ myapp/static

   toppcloud will make available things in the static directory
   available without hitting the webapp

#. Configure myapp/app.ini similarly to (taken from pylonshq site):

   ::

               [production]
               app_name = pylonshq
               runner = src/kai/production.ini
               version = 1
               update_fetch = /sync_app
               service.couchdb =
               service.files =
               default_host = pylonshq.com


   In this case, the Pylons site needs CouchDB setup, and the files
   service (all Pylons sites should use the files service to store
   cached files, templates, etc.)

#. ::

       $ toppcloud update myapp/

   Note that we’re one directory above myapp, and we have a trailing
   slash on myapp, this is needed because an rsync is done to copy it to
   the server, don’t leave off the trailing slash! (This will prolly be
   fixed at some point)

That’s it! 10 easy steps to go from zero to a running **deployed**
website.

I should also note that you will need to make a production.ini file, and
that it should have a few important changes in it. All the references to
``%(here)s`` should be changed to ``%(CONFIG_FILES)s`` since that’s the
persistent location that files can be stored for a toppcloud app between
deployments. Other configuration information provided by services (Couch
supplies the db/host, Postgres has its host/user/pass info) can be
accessed via ``CONFIG_`` vars as well. The `services
docs <http://bitbucket.org/ianb/toppcloud/src/tip/docs/services.txt>`_
have some more info.

More apps can be added to a host as desired, until the ram runs out of
course. At the moment toppcloud is using a process pool of 5 with 1
thread under mod-wsgi for each application. This can use a bit of ram if
you have multiple heavy Pylons processes, hopefully there will shortly
be a way to ask toppcloud to use a single process with multiple threads
which will help cut the ram profile a bit.

Using Django and PHP
--------------------

Unfortunately I haven’t actually tried this myself, but there’s nothing
preventing it. You’ll need to change the ``app.ini`` so that instead of
using ‘src/kai/production.ini’ as the runner, it uses a Python file in
the directory, say ``main.py`` that then loads the Django app as a WSGI
application and returns it. Sort of `like
this <http://bitbucket.org/ianb/toppcloud/src/tip/toppcloud/init-files/main.py.tmpl>`_.
Note that the config vars Django needs for its database should then be
present in ``os.environ`` when setting up the ``settings.py`` that
Django uses.

If you’re looking through the toppcloud source code by now, you may have
also noticed there’s an example app that uses PHP. There’s nothing
holding back toppcloud from setting up mod\_passenger and deploying Ruby
apps at some point either should someone wish to add that feature.

dumb pipes
----------

There’s been numerous mentions on various blogs and in the news about
how much the cell phone carriers hate the concept of being nothing more
than “dumb pipes” for wireless Internet and phone use. That means of
course, that they’d no longer be competing on what phones you could use
but instead *solely on service quality and price*… I think the same type
of transition is in store for shared hosting providers and some of the
boutique app deployment shops like `heroku <http://heroku.com/>`_.

It’ll take awhile, toppcloud is very rough right now. But when you can
d/l a nice little open-source package, run it, choose your choice of
cloud provider (based on price + quality!), have it automatically setup
for you to deploy your apps to, then deploy apps with a single command…
you’ve already done the vast majority of what a service like heroku
does, except you could still modify toppcloud if there was something
lacking you really needed. And it’s a reason like that, that toppcloud
exists to begin with.

Oh, and thanks Ian for writing this before I wasted more time making it
myself.


.. author:: default
.. categories:: Pylons, Python
.. comments::
   :url: http://be.groovie.org/post/321827504/deploying-python-web-apps-with-toppcloud
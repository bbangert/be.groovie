Python Paste Power
==================

Mmm, tasty, a headline of P-word's. Recently `Ian
Bicking <http://blog.ianbicking.org/>`_ went on a bit of a `release
spree <http://blog.ianbicking.org/releases-releases-releases.html>`_
with a whole bunch of goodness that I'm way too lazy to link to in this
paragraph. The ones I've been waiting for were all in the line-up:
Paste, Paste Script, and Paste Deploy. I `blogged about paste and
setuptools <http://groovie.org/articles/2005/09/29/setuptools-and-python-paste>`_
earlier and hadn't followed up as I indicated I would partly because I
was waiting on their official release.

So, what's the big deal? `Paste <http://pythonpaste.org/>`_ and its
buddies solve a host of issues that commonly confront Python web
developers and web administrators, the `front page of Python
Paste <http://pythonpaste.org/>`_ does a good job of explaining briefly
why each group should care. Thus, I'll move directly onto the fun that
comes with using them.

Yes, I think its fun, but that might be just because I have a thing for
installing web frameworks…. so I'll cover using Paste as two groups of
users, as a Web Developer, and as a Web Administrator.

Using Paste as a Web Developer
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

First off, to create a web application we need to setup a directory for
the project. Since we want our web application to be Paste-enabled, the
template for the web application should be using
`setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_. That
way when we package up our web application and give/sell it on the
Internet, the people (Web Admins) using it will be able to install and
run it easily.

So… lets see what framework I should use to whip up this little web
application. I'll run a ``paster`` command that lets me see what
Paste-enabled web frameworks I have installed that come with new web
application directory templates:

::

    % paster create --list-templates
    Available templates:
      basic_package:            A basic setuptools-enabled package
      myghty_modulecomponents:  Module Component Template
      myghty_routes:            Routes Template
      myghty_simple:            Simple Template
      paste_deploy:             A web application deployed through paste.deploy
      pylons:                   Pylons application template
      turbogears:               TurboGear application template

Cool, right? Well, maybe its just cause I like having a big toolbelt of
web frameworks sitting around. Obviously not a lot of web frameworks
have paste templates available yet, but more are adding support and I'll
be rather excited when that list is 20 or more long.

If you go and install the Paste packages, your list won't be quite as
long as mine (insert evil laugh) as I'm running the CVS of
`Myghty <http://www.myghty.org/>`_ (0.99 release with these templates
coming shortly), along with some other stuff I've whipped up. Merely
installing a web framework package that's Paste-enabled and has
templates available will make it show up in that list.

Another interesting thing to consider here, is that there's no
requirement that only web frameworks are allowed to create directory
templates. Maybe a web application you're working on, is so powerful you
want to make it easy for end-users to extend it with their own custom
add-ons. You could provide a `paster
template <http://pythonpaste.org/script/developer.html#templates>`_ that
creates a plug-in ready directory template for custom themes. There's a
ton of power packed in the various ways you can extend these tools,
building on the dynamic discovery stuff in setuptools.

Moving along though, I'll go ahead and use
`Turbogears <http://turbogears.org/>`_.

::

    % paster create —template=turbogears pygoSelected and implied templates:
      TurboPaste#turbogears  TurboGear application template

        Variables:
      package:  pygo
      project:  pygoCreating template turbogears
      Creating ./pygo/
      Recursing into package
        Creating ./pygo/pygo/
        Copying init.py to ./pygo/pygo/__init__.py
        Copying model.py to ./pygo/pygo/model.py
        Recursing into templates
          Creating ./pygo/pygo/templates/
          Copying init.py to ./pygo/pygo/templates/__init__.py
      Copying package-start.py_tmpl to ./pygo/pygo-start.py
      Copying dev.cfg_tmpl to ./pygo/dev.cfg
      Copying prod.cfg to ./pygo/prod.cfg
      Copying setup.py_tmpl to ./pygo/setup.pyRunning /opt/local/bin/python setup.py egg_info

As you can see, it just setup our new project for us, which I called
**pygo** because it was the first name that popped into my head. If
you've actually used TurboGears, looking at that should have raised some
red flags as its missing a bunch of stuff that a TurboGears project
needs. This is mainly because the template was created by Ian as a
demonstration of how to make a Turbogears-style template. Hopefully an
upcoming version of TurboGears will be Paste-enabled so I can create a
new project like this (hint hint). :)

Ah well, I'll just make a basic Myghty project using Routes instead:

::

    % paster create —template=myghty_routes pygoSelected and implied templates:
      Myghty#myghty_routes  Routes Template

        Variables:
      package:  pygo
      project:  pygoCreating template myghty_routes
      Creating ./pygo/...Bunch more files…

So that's all there is to creating new projects with the web framework
of your choice (if its Paste-enabled). How do we go and start it up?

::

    ~% cd pygo
    ~/pygo% paster serve server.conf 
    Starting server in PID 6090.

In the case of the myghty\_routes template, it starts the server on port
5000. A quick look at the server.conf file makes it obvious:

::

    [server:main]use = egg:PasteScript#wsgiutilshost = 127.0.0.1port = 5000

        [app:main]use = egg:pygo#paste

That's really all the Paste you have to worry about as a web developer
(though it has even more capabilities you'll probably want to use). We
can see here that its using wsgiutils from PasteScript to run the
server. You can easily swap that out for any of the server support that
`flup <http://www.saddi.com/software/flup/>`_ offers such Fast CGI,
SCGI, or AJP.

At this point, as a web developer, you'd go ahead and create your web
application. Especially since the default myghty\_routes template is
pretty boring if you don't put anything in it. But for this example,
we'll assume its done and distribute it as a single egg file for people:

::

    ~/pygo% python setup.py bdist_egg
    running bdist_egg
    running egg_info
    ... whole bunch of stuff here...
    ~/pygo% ls dist/
    pygo-0.0.0-py2.4.egg

That's it. This is easy, right? You're ready to go ahead and give your
egg to anyone running Python 2.4 now (You could make a source
distribution and upload it to `Cheese
Shop <http://cheeseshop.python.org/pypi>`_ just as easily). So let's try
and totally forget that we're a web developer, and assume a different
role.

Using Paste as a Web Administrator
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Ah yes, the joys of setting up web applications you come across. Well,
I've rarely gotten any joy out of it at least. Let's take a look at how
Paste does make it a lot easier. First, we'll need to install the
insanely useful Pygo webapp that some other thoughtful user created. If
this Pygo application was released and uploaded to the Cheese Shop, I
could install it like so:

::

    % sudo easy_install Pygo                                  Searching for Pygo
    Reading http://www.python.org/pypi/Pygo/
    Best match: Pygo 0.0
    Downloading http://cheeseshop.python.org/packages/2.4/P/Pygo...
    Processing pygo-0.0.0-py2.4.egg
    ... more stuff happens...
    Installed /usr/local/lib/python2.4/site-packages/pygo-0.0.0-py2.4.egg
    Processing dependencies for Pygo

Now, since I didn't actually upload it to Cheese Shop, I've faked that
screen. But that's pretty close to how it would've looked if I had
released pygo and uploaded it to Cheese Shop.

After this one command, as a web administrator, we now have the pygo
application installed. There shouldn't be any need to be installing web
applications over and over for every user that wants to run it as the
vast majority of web applications get their customization and settings
from a database.

What needs to be configured, is the *instance* of the web application
that each user is running. We can set that up for each user inside our
`Paste configuration file <http://pythonpaste.org/deploy/>`_ like so:

::

    [server:main]use = egg:PasteScript#flup_scgi_threadhost = 127.0.0.1port = 3000

        [composit:main]use = egg:Paste#urlmap/blog/fred = fredpygo/blog/janet = janetpygo

        [app:fredpygo]use = egg:pygodatabase = mysql:/username@localhost/database

        [app:janetpygo]use = egg:pygo

These configuration files are quite flexible, and allow different
instances of a web application to run at different locations. In that
case, one of them is running for ‘fred' at ``/blog/fred``. Each block
for an ``app`` can have additional arguments that setup the database to
use, and other settings that should probably be customized for each
user. I threw in an additional database argument for one of them as an
example.

Maybe you're not a web administrator, but a web user comfortable
downloading and installing many of the other webapps out there (Typo,
MovableType, phpBB, etc.). Setting up your own site, using whatever
Paste-enabled Python webapps you want is just as easy. Ideally ISP's and
such would just run the easyinstall command to install whatever the
‘popular' webapps of the week are, and they can update them easily, keep
old versions around if needed, etc.

Making Python Web-Application Distribution/Use Easy
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

**This is pretty powerful stuff, and its quite easy to use**. Even if
you're not making a web application with the intent to distribute it to
the world, Paste is still going to help you out in a lot of ways.

An ISP or webapp end-user only needs to know how to add your webapp to
their `config file <http://pythonpaste.org/deploy/>`_ and installing it
is a breeze thanks to setuptools. I think this has an enormous benefit
for the Python web community, as it'll significantly increase the ease
of use when it comes to installing and managing web applications. Python
web developers will gain some good footing to create Python Web
Applications that compete with and surpass PHP webapps, especially if
more ISP's start supporting Paste-enabled applications.

Well, that's my hope at least as I'm sure the title of this section made
clear.

For the Python web framework creators out there, I like writing web
applications (with various web frameworks), and I really like how easy
Paste makes it to create them, package them up, and use them. *Please
add Paste support to your web framework*, I'll be happy to help and the
Paste mail list is very responsive.


.. author:: default
.. categories:: Python, Code, Myghty
.. comments::
   :url: http://be.groovie.org/post/296349639/python-paste-power
Where's the Capistrano knock-off for us Python web devs?
========================================================

Rails, and Ruby in general has had `Capistrano <http://capify.org/>`_
for awhile now to help with the task of deployment and automating builds
for servers, and even clusters of servers. Where is something like this
for Python?

Now, before people note that I could easily use Capistrano for my Python
project, I should note that it is rather annoying having to install yet
another language. On the other hand, given that I will likely only need
to install it on my development machine (which running OSX already has
Ruby… and gems), it doesn't seem too horrible to just use Capistrano and
be done with it.

However, Capistrano doesn't quite manage the Python egg's, and the task
isn't exactly trivial.
`zc.buildout <http://pypi.python.org/pypi/zc.buildout>`_, which I
`previously ranted about due to odd
docs <http://groovie.org/articles/2008/04/04/sacrificing-readability-for-automated-doc-tests>`_
does the management pretty well. It even results in a rather consistent
build experience no matter where it occurs. Two commands, and boom, the
app is ready to go.

Unfortunately, life isn't quite that easy. When something does go wrong
with buildout, trying to track it down can be exceptionally hairy.
Having a tool so ‘magical' as I've heard some describe it, carries its
own penalties when things fail. Buildout also fails to automate the task
of deploying the app itself to the other machine, which is still a
manual process. It does manage egg's rather well, though it does some
very odd mangling of ``sys.path`` to accomplish this in every script.

I don't need something as full featured as Capistrano, but I'd love to
see something that has no more requirements than I'm already depending
on (Python), that can handle the task of easily automating deployment of
a Python application – including ensuring all the proper versions of the
eggs I want are used – on a remote \*nix machine. I recall seeing a post
(I think by Jeff Rush) awhile back, on a system just like this that he
unfortunately never released.
`Vellum <http://www.zedshaw.com/projects/vellum/>`_ also looks like it
could be hacked further to do this task…

Is there some build/deployment tool that is just Python that I've
missed? Something that will let me setup a script for some commands on
how to deploy my app on another server and setup (hopefully in a
`virtualenv <http://pypi.python.org/pypi/virtualenv>`_) the webapp so
its ready-to-run (and optionally restart it/migrate the db/etc :)?


.. author:: default
.. categories:: Python, Thoughts, Rants
.. comments::
   :url: http://be.groovie.org/post/296342920/wheres-the-capistrano-knock-off-for-us-python-web
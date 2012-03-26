setuptools and Python Paste
===========================

I indicated in my last article that I would begin blogging about a very
misunderstood, and what I would consider unappreciated Python package
called `PythonPaste <http://pythonpaste.org/>`_. Python Paste is
currently undergoing a documentation and website update after which it
will hopefully be much more useful for those wishing to use it, or even
understand why they'd want to.

To really get started with Python Paste its exceptionally useful to know
about a package that is used extensively by Paste to accomplish some of
the magic it performs. This package is setuptools by `Phillip J.
Eby <http://dirtsimple.org>`_, and knowing where setuptools is being
utilized form actual Paste code will make it much easier for both web
framework creators and web framework users (Web Application end-users
don't need to know any of this).

A Better distutils
^^^^^^^^^^^^^^^^^^

One of the things that setuptools in a way replaces/upgrade/enhances is
the commonly used Python disutils package. Many issues are present in
distutils that setuptools resolves, such as:

#. Automatically installing dependency packages
#. Using multiple versions of a package at once
#. Upgrading a package and its dependencies
#. Installing a package retrieved automatically over the Internet

These are just some of the common things people might want to do, that
distutils doesn't provide. setuptools add's even more, such as:

#. Easily develop a package without installing it
#. Install packages in your user-space rather than the system
#. Create extensible applications/frameworks that automatically discover
   extensions using ‘entry points'. (This is a big feature that Paste
   uses)
#. Register/Upload your package to a central Python package repository
   (Cheeseshop)
#. Create Python eggs – a single-file importable distribution format
#. Include data files inside your package directories with modules
   making it easy to access them

The functionality of setuptools most likely to crop up during an
exploration and use of Paste, is #3 and #6. Knowing that these functions
are coming from setuptools rather than Paste will make it easier to see
what parts Paste handles, and what setuptools is doing. There's `more
features of
setuptools <http://peak.telecommunity.com/DevCenter/setuptools>`_ than
I'm not mentioning here, as what's most important for Paste is to see
where the features I mentioned fit in.

Using setuptools
^^^^^^^^^^^^^^^^

Quite a few programs `use setuptools and
cheeseshop <http://cheeseshop.python.org/pypi>`_ for distribution.
Changing your package to `use setuptools instead of distutils is very
simple <http://peak.telecommunity.com/DevCenter/setuptools#basic-use>`_,
as the setup() block in the setup.py file is almost identical. I'd
suggest taking a quick look at the setuptools site for what this config
looks like if you aren't already familiar with it.

Discovering Libraries
^^^^^^^^^^^^^^^^^^^^^

This feature is used by Paste to discover support that other web
frameworks enable for Paste usage. setuptools' full name for this is
`Dynamic Discovery of Services and
Plugins <http://peak.telecommunity.com/DevCenter/setuptools#dynamic-discovery-of-services-and-plugins>`_
and its very handy. You could use it for your blog to discover plugins
that announce support for it, or your web server can discover webapp's
that are available for it, etc.

Dynamic discovery of plugins is a very powerful ability, and one you'll
see throughout Paste-compatible web frameworks and web applications.
When you see Paste documentation talking about ‘entry\_points', its
referring to something you'd configure for your package. Here's what a
PasteDeploy compatible setup.py is likely to contain:

::

    from setuptools import setup, find_packages

        setup(
        name=Joe Smitch,
        version=0.1,
        install_requires=[“PackageOne”, “PackgeTwo >= 1.3”],
        packages=find_packages(),
        entry_points=”“”
        [paste.app_factory]
        main=PACKAGENAME.wsgiapp:make_app
        “”“,
        )

Paste is just looking for a command that will give it a WSGI application
(we'll talk about Paste later). The entry point group (or EPG) there is
called paste.app\_factory, so Paste can scan for packages that have this
EPG and learn what packages will work with it.

While it looks like Paste is doing a lot of work, this is all setuptools
so far. The install\_requires just indicates that those two packages
should be installed at the same time as our new one, and that PackageTwo
should be a version >= 1.3. The rest of the lines should look familiar
to anyone who has used distutils.

Including Data Files at Run-time
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you've distributed data files (Non-Python code that goes with your
program), you might've resorted to ``__file__`` hacks to make sure your
program knew where the files actually were. setuptools provides
`facilities to make getting to these installed data
files <http://peak.telecommunity.com/DevCenter/setuptools#accessing-data-files-at-runtime>`_
a bit easier, more reliable, and even compatible with PEP 302-based
import hooks (don't worry if the last one makes no sense, its good
news).

When you look through or use code that imports ``pkg_resources``, this
is something setuptools provides for your use. It's also used to run
version-specific code, in the event that you have multiple versions of
the same package installed. This way, you can upgrade packages without
breaking code thats relying on a specific version of the package, as
long as you keep around the older package (You'll need to use the
`multiversion
option <http://peak.telecommunity.com/DevCenter/EasyInstall#upgrading-a-package>`_
when installing).

Conclusion
^^^^^^^^^^

As you might have noticed, this is a fairly brief overview on some of
the functionality of setuptools. It does a lot more than I'm noting
here, as this post is mainly intended to cover heavily used features of
setuptools that will crop up when using Paste. Knowing that
‘entry\_points' and such are what setuptools provides will make it
easier to understand Paste and how Paste discovers the abilities you
supply for it (Using your own packages that employ setuptools).

*Coming up next… **What Paste means for end-users***


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296351471/setuptools-and-python-paste
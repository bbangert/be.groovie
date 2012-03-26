Separating Web Development Environments in Myghty
=================================================

On many occasions, its quite useful when developing web applications to
have the webapp know whether its in a production/development/testing
environment. Rails builds this into the framework and its rather easy to
add this toggle throughout a `Myghty <http://www.myghty.org/>`_ webapp
(or some other Python web framework) as well.

We'll make use of an environment variable so that the webapp environment
can be easily configured from lighttpd or Apache. This way just
deploying the application under a different handler can toggle the web
applications mode of operation. The other thing we'll setup while we're
at it, is a variable to keep track of the absolute root of our web
application. I've found it quite useful in many cases to be able to get
at this information without hardcoding it in, this way its always
accurate no matter where the program is.

There's a few rather commands that'll give you the information we're
looking for. It took me awhile to find this, so hopefully it'll help
someone else out there.

Getting our Absolute Location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Let's assume our directory hierarchy looks like this:

::

    webapp/
       templates/
       components/
       scripts/
          dispatch.fcgi

Maybe you have the script called by mod\_python or
`lighttpd <http://www.lighttpd.net/>`_ somewhere else, I'm assuming
it'll be inside the root of your web application somewhere. In this
case, the handler called by lighttpd is ``dispatch.fcgi``. So
``dispatch.fcgi`` needs to figure out what the absolute path of the
directory is above it.

Here's the code that figures this out:

::

    import os

        Set the prefix to our base path for the webapp
        myloc = os.path.join(os.getcwd(), file)prefix = os.path.normpath(myloc + ‘../..')

The myloc assignment gets the absolute file-name with path of the
current file, in this case ``dispatch.fcgi``. Unlike a normal
os.getcwd(), this call doesn't care what directory we happen to be in
when we import the module, it will always be the absolute file-name of
that file.

In case you're curious why this happens, ``__file__`` will return the
path of the file relative to the working environment its called from. So
combining it with the full path name of the current working environment
results in the complete absolute path of the module no matter what the
current context or working directory.

The prefix assignment uses the normpath call to strip off the filename,
and backup one directory to our webapp root. This leaves us with the
absolute path to our ``webapp/`` directory.

Setting and Using the Environment variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Figuring out if we're in a special runtime environment is quite easy and
looks like this:

::

    import os

        MYGHTY_ENV = os.environ.get('MYGHTY_ENV') or 'development'

Now we can just test MYGHTY\_ENV to determine whether to contain errors
ourself, or drop them to the web (as you would want in development
mode). We default to being in development mode, since this is what you'd
typically run your webapp in.

To switch it to production mode, here's what the lighttpd config looks
like:

::

    fastcgi.server = ( 
       ".fcgi" => (
         "www" => (
            "min-procs" => 2,
            "max-procs" => 4,
            "socket" => "/tmp/webapp.socket",
            "bin-path" => "PATH/TO/webapp/scripts/dispatch.fcgi",
            "bin-environment" => ("MYGHTY_ENV" => "production" ),
            "idle-timeout" => 120
          )
        )
    )

To set the extra environment variables with Apache, use `mod\_env with
the SetEnv
directive <http://httpd.apache.org/docs/1.3/mod/mod_env.html#setenv>`_
which would look something like this:

::

    # Make sure you have mod_env loaded, this line assumed to be in the VirtualHost
    # block of your config
    SetEnv MYGHTY_ENV production

At this point, you might've noticed (if you've used Rails) how similar
my Fast CGI setup with lighttpd looks when compared to the some of the
Rails examples for a lighttpd + Fast CGI setup. This is intentional, as
I'm adding a `Routes <http://routes.groovie.org/>`_ dispatcher to Myghty
so it makes sense to layout my web application in a similar directory
hierarchy.

Anytime you need to toggle some behavior depending on your webapp's
runtime context, just import ``os`` and check it as I showed up above.


.. author:: default
.. categories:: Python, Myghty
.. comments::
   :url: http://be.groovie.org/post/296352150/separating-web-development-environments-in-myghty
Routes functional conditions and WSGI Middleware
================================================

Sometimes, it amazes me whats possible fully utilizing WSGI middleware
in an application stack. While it likely isn't something totally unique
to the framework, the relative ease with which it can be done still
sometimes gets me to grin.

Tonight, a Pylons user on the IRC channel (irc.freenode.net, #pylons)
asked if it was possible to get a URL laid out so that /s/SOMETHING
would map into their ‘s' controller, with the second part passed in as a
variable. That alone is pretty easy, however the additional requirement
was that the controller action would change depending on the user's
“type”.

There's two ways to deal with this, the first of which is the only
possible way in many frameworks. Have every request to the URL map to a
single function, and in that function load up the session and call the
appropriate function to handle the request based on their user type.
This way works fine in Pylons too, but thanks to Routes and WSGI
middleware we have another option.

Routes has a lot of capabilities to it, there's been numerous additions
to the Python implementation that the Rails version is not capable of.
One of them is the ability to alter the resulting URL match dictionary
in various conditional functions. To toggle the controller action used,
we'll be using the ability to `pass in a function to Routes
conditions <http://routes.groovie.org/manual.html#conditions>`_ that can
alter the resulting match.

This condition checking function has full access to the `WSGI
environ <http://www.python.org/dev/peps/pep-0333/#environ-variables>`_
so if you wanted to restrict a specific controller/action combination to
people referred from Slashdot, no problem! You can carefully fine-tune
the conditions required for dispatch at the same place you define your
URL resolution.

Since Pylons uses `Beaker <http://beaker.groovie.org/>`_ for session
handling via WSGI middleware, the session object will already be
available when our Pylons app gets called. Beaker loads the user session
into ``environ['beaker.session']``. Given this knowledge, we can write a
conditional function for use with Routes like so:

::

    def check_user(environ, result):
        session = environ['beaker.session']
        user_type = session.get('type')
        if not user_type:
            result['action'] = 'index'
        elif user_type == 'admin':
            result['action'] = 'view_action'
        else:
            result['action'] = 'not_logged_in'
        return True
    map.connect('s/:domain', controller='s', conditions=dict(function=check_user))

Viola! Now Routes will run the function provided to see if it returns
``True`` before accepting that as a valid match. In the process, the
action used will be set as desired. I've always thought a good sign
something is well designed is when people can use it in ways you didn't
originally anticipate. If that's the criteria, I think Routes succeeds
and then some.

**Disclaimer: Yes, I wrote Routes, and a good chunk of Beaker and
Pylons, so I might be biased and tooting my own horn. :)**


.. author:: default
.. categories:: Python, Routes
.. comments::
   :url: http://be.groovie.org/post/296345896/routes-functional-conditions-and-wsgi-middleware
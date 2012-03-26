Routes 1.1 Preview
==================

The major feature I was waiting on for Routes 1.1 is for the most part
done, mainly adding more unit tests for the new syntax now. As I
`mentioned previously when announcing Routes
1.0 <http://groovie.org/articles/2005/11/21/routes-1-0-released>`_, this
feature is the one quite a few people have been waiting for. The ability
to split the route path somewhere other than on a ``/``.

Here's what a few Routes using the new feature look like:

::

    map.connect(':category/:(page).html', controller='stories', action='view')

        map.connect('feeds/:(section).:(extension)', controller='feeds', action='formatter')

        map.connect('archives/:(year):(month):(day).html', controller='archives', action='view',
              requirements=dict(year=r'\d{4}',month=r'\d{2}',day=r'\d{2}'))

The new section dividers, ``:(something)`` can be used side-by-side as
the last example above shows, however in such cases each path part must
have a rigid regexp requirement placed on it to ensure proper collection
of the variables. Typically you will have some characters in between
each dynamic part so this issue doesn't arise.

I've retained full backward compatibility with the old syntax as well,
if you don't designate the dynamic part using the ``()`` modifier it
will fall back to looking for the next ``/`` instead. So far, all the
existing (and **extensive**) unit tests are passing, in addition to new
tests I've been adding.

Routes generates a full regular expression for URL matching based off
the route path you give it. This makes it a great way to setup URL
routing with the power of regexp's yet avoiding the hassle of writing a
large complex regexp yourself. The other very powerful ability you gain
is that Routes can turn the keywords back into the URL, like so:

::

    >>> url_for(controller='archives', action='view', year=2004, month=10, day=12)‘archives/20041012.html'

        >>> url_for(controller='feeds',action='formatter',section='computers',extension='xml')‘feeds/computers.xml'

If you're interested in giving it a spin, it can be checked out and
installed easily from the svn repository using setuptools:

::

    sudo easy_install -U http://routes.groovie.org/svn/branches/newsplit

Feedback / Suggestions / Bug Reports greatly appreciated.


.. author:: default
.. categories:: Python, Code, Routes
.. comments::
   :url: http://be.groovie.org/post/296346625/routes-1-1-preview
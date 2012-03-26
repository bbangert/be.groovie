Advanced Caching with Django and Beaker
=======================================

After seeing more than a few blog posts and packages attempt to provide
more advanced caching capability for Django, it occurs to me I should
actually just blog how to use `Beaker <http://beaker.groovie.org/>`_
**in Django**, rather than just keep mumbling about how “Beaker already
does that”. So, if you've needed caching in Django that goes beyond
using **just one backend at a time**, or maybe can actually cope with
the `Dog-Pile
Effect <http://hype-free.blogspot.com/2008/05/avoiding-dogpile-effect.html>`_,
this is the blog entry for you (Until I flesh it out further into actual
docs on the Beaker site).

Install Beaker
--------------

This is simple enough, if you have ``easy_install`` available, just:

::

     easy_install -U Beaker

Or if you prefer to download tar files, grab `the Beaker 1.4 tar.gz
file <http://pypi.python.org/packages/source/B/Beaker/Beaker-1.4.tar.gz#md5=7d9992f193db1e2f658905e6234d6bc5>`_

Configuring the Cache
---------------------

Setting up Beaker's cache for your Django app is pretty easy. Since only
a single cache instance is needed for an app, we'll set it up as a
module global.

Create a ``beakercache.py`` file in your Django project with the
following contents:

::

     from beaker.cache import CacheManager
     from beaker.util import parse_cache_config_options

     cache_opts = {
         'cache.type': 'file',
         'cache.data_dir': 'cache/data',
         'cache.lock_dir': 'cache/lock'
     }

     cache = CacheManager(**parse_cache_config_options(cache_opts))

There's a lot more options available, such as memcached, configuring
multiple cache backends at once, etc. Now that you know how to provide
the configuration options, further customization can be done as needed
`using the Beaker configuration
docs <http://beaker.groovie.org/configuration.html>`_. (Note the very
handy cache region configurations which make it easy to toggle cache
backend configurations on the fly!)

Using the Cache
---------------

Beaker provides a `conveinent decorator
API <http://beaker.groovie.org/caching.html#decorator-api>`_ to make it
easy to cache the results of functions. In this example we'll just sleep
and make a string including the time, add this to your ``views.py``:

::

     import time
     from datetime import datetime

     from django.http import HttpResponse

     from YOURPROJECT.beakercache import cache

     def hello(request):
         @cache.cache(expire=10)
         def fetch_data():
             time.sleep(4)
             return 'Hello world, its %s' % datetime.now()
         results = fetch_data()
         return HttpResponse(results)

In this case, the cached data is in a nested function with the
decorator. It could of course be in the module elsewhere as well.

Hook the view function up in your ``urls.py``, and hit the view. The
first time it will wait a few seconds, then it will return the old time
until the cache expires (10 seconds in this case).

The cached function can also accept positional (non-keyword) arguments,
which will be used to key the cache. That is, different argument values
will result in different copies of the cache that require those
arguments to match.

That's it, it's really quite easy to use.

**Update**: It occurs to me this post does say ‘advanced', and that
example wasn't very advanced, so here's something a bit more
interesting. Let's configure cache regions to make it easy to toggle how
long **and where** something is cached. Cache regions allow you to
arbitrarily configure batches of settings, a ‘region'. Later you can
then indicate you want to use that region, and it uses the settings you
configured. This also make its easy to setup cache policies and change
them in a single location.

In this case, we'll have ‘long\_term' and ‘short\_term' cache settings,
though you can of course come up with as many regions as desired, with
the name of your choice. We'll have the long\_term settings use the
filesystem, since we want to retain the results for quite awhile and not
have them pushed out like memcached does. The short\_term settings will
use memcached, and be cached for only 2 minutes, long enough to help out
on those random slashdog/digg hits.

In the ``beakercache.py`` file:

::

     from beaker.cache import CacheManager
     from beaker.util import parse_cache_config_options

     cache_opts = {
         'cache.type': 'file',
         'cache.data_dir': 'cache/data',
         'cache.lock_dir': 'cache/lock',
         'cache.regions': 'short_term, long_term',
         'cache.short_term.type': 'ext:memcached',
         'cache.short_term.url': '127.0.0.1.11211',
         'cache.short_term.expire': '1200',
         'cache.long_term.type': 'file',
         'cache.long_term.expire': '86400',
     }

     cache = CacheManager(**parse_cache_config_options(cache_opts))

Now in our ``views.py``:

::

     import time
     from datetime import datetime

     from django.http import HttpResponse

     from testdjango.beakercache import cache

     def hello(request):
         @cache.region('long_term')
         def fetch_data():
             time.sleep(15)
             return 'Hello world, its %s' % datetime.now()
         results = fetch_data()
         return HttpResponse(results)

     def goodbye(request):
         @cache.region('short_term'')
         def fetch_data():
             time.sleep(4)
             return 'Bye world, its %s' % datetime.now()
         results = fetch_data()
         return HttpResponse(results)     



.. author:: default
.. categories:: Code, Python
.. comments::
   :url: http://be.groovie.org/post/296328691/advanced-caching-with-django-and-beaker
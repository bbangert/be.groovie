Beaker 1.3 is juicy caching goodness
====================================

`Beaker 1.3 <http://pypi.python.org/pypi/Beaker>`_ is out, actually, its
been out for awhile and I'm just not getting around to blogging the
fact. It's a shame I've been a bit too busy lately to blog this earlier
because in addition to some bug fixes it has some nice new features that
make it even easier to use in **any** Python
script/application/framework.

First, to air my dirty laundry, the important bug fixes in Beaker 1.3:

-  Fixed bug with (non-cookie-only) sessions not being timed out
-  Fixed bug with cookie-only sessions sending cookies when they weren't
   supposed to
-  Fixed bug with non-auto sessions not properly storing their last
   accessed time

The worst thing with the first two of these is that they were
regressions that snuck in despite unit tests that exercised the code
fairly decently. They're fixed now along with more comprehensive tests
to help prevent such regressions occurring again.

Beaker has always had session's, and caching, but except for Pylons I've
yet to see anyone actually **use** Beaker's caching utility. I've seen
the SessionMiddleware used in other WSGI based frameworks, but not the
caching, which is kind of a shame since it:

-  Supports various backends: database, file-based, dbm file-based,
   memcached
-  Has locking code to ensure a single-writer, multiple reader model
   (This **avoids** the dreaded `dog-pile
   effect <http://hype-free.blogspot.com/2008/05/avoiding-dogpile-effect.html>`_
   that caching systems such as the one in Django experience!)

For clients that hit the cached function while its already being
regenerated, Beaker serves the old copy until the new content is ready.
This avoids the dog-pile effect, and keeps the site snappy for as many
users as possible. Since the lock used is disk-based though, this does
mean you only avoid the effect per machine (unless you're locking
against NFS or a SAN), so if you have 20 machines in a cluster, the
worst the dog-pile effect can get is that you'll have 20 new copies
generated and stored.

Now, in Beaker 1.3, to try and encourage its use a bit more, I've added
a few decorators to make it easier to cache function results. Also with
`Mike Bayer's <http://techspot.zzzeek.org/>`_ suggestion, there is now
cache regions to make it easier to define various caching policy
short-cuts.

Cache Regions
-------------

Cache regions are just pre-defined sets of cache instructions to make it
easier to use with your code. For example many people have a few common
types of cache parameters they want to use:

-  Long-term, likely to a database back-end (if used in a cluster)
-  Short-term, not cached as long, perhaps to memcached

To set these up, just tell Beaker that about the regions you're going to
define, and give them the normal Beaker cache parameters for each
region. For example, in this Pylons app, I define 2 cache regions in the
INI:

::

     beaker.cache.regions = short_term, long_term
     beaker.cache.short_term.type = ext:memcached
     beaker.cache.short_term.url = 127.0.0.1:11211
     beaker.cache.short_term.expire = 3600

     beaker.cache.long_term.type = file
     beaker.cache.long_term.expire = 86400

**Note**: For those wondering about multiple memcached servers, just put
them in as the url with a semi-colon separating them.

If you want to use the caching outside of Pylons without middleware (ie,
as a plain library), that's a bit easier now as well:

::

     from beaker.cache import CacheManager
     from beaker.util import parse_cache_config_options

     cache_opts = {'cache.data_dir': './cache',
                   'cache.type': 'file',
                   'cache.regions': 'short_term', 'long_term',
                   'cache.short_term.type': 'ext:memcached',
                   'cache.short_term.url': '127.0.0.1:11211',
                   'cache.short_term.expire': '3600',
                   'cache.long_term.type': 'file',
                   'cache.long_term.expire': '86400',
     }

     cache = CachManager(**parse_cache_config_options(cache_opts))

And your cache instance is now ready to use. Note that using this cache
object is thread-safe already, so you just need to keep one around in
your framework/app (Can someone using Django explain where you'd keep a
reference to this object around so that you could get to it in a Django
view?).

New Cache Decorators
--------------------

To make it easier to use caching in your app, Beaker now includes
decorators for use with the cache object. Given the above caching setup,
lets assume you want to cache the output of an expensive operation:

::

     # Get that cache object from wherever you put it, maybe its in environ or request?
     # In Pylons, this will be: from pylons import cache
     from wherever import cache

     def regular_function():
         # Do some boring stuff

         # Cache something
         @cache.region('short_term', 'mysearch')
         def expensive_search(phrase):
             # Do lookup with the phrase variable
             return something
         return expensive_search('frogs')

The second argument to the region decorator, ‘mysearch'. That isn't
required unless you have **two** function's of the **same name in the
same module**, since Beaker records the namespace of the cache using the
function name + module + extra args. For those wondering what a Beaker
namespace is, its a single cache ‘block'. That is, lets say you wanted
to cache 4 versions of the **same thing**, but change them differently
depending on the input parameter. Beaker considers the **thing** to be a
namespace, and the things that change the thing being cached are the
cache keys.

**Only un-named arguments** are allowed on the function being cached.
These act as the cache keys so that if the arguments change, a **new**
copy is cached to those arguments. This way you can have multiple
versions of the function output cached depending on the argument it was
called with.

If you want to use arbitrary cache parameters, use the other decorator:

::

     # Get that cache object from wherever you put it, maybe its in environ or request?
     # In Pylons, this will be: from pylons import cache
     from wherever import cache

     def regular_function():
         # Do some boring stuff

         # Cache something
         @cache.cache('mysearch', type='file', expire=3600)
         def expensive_search(phrase):
             # Do lookup with the phrase variable
             return something
         return expensive_search('frogs')

This allows you to toggle the cache options per use as desired.

If there's anything else I can do to make it easier to use Beaker in
your application, be sure to let me know (Yes, I know more docs would
help, this blog post was a first attempt to help out on that front, more
docs on the way!).


.. author:: default
.. categories:: Code, Python
.. comments::
   :url: http://be.groovie.org/post/296328850/beaker-1-3-is-juicy-caching-goodness
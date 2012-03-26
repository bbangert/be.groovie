Beaker 1.4 Released
===================

`Beaker <http://beaker.groovie.org>`_ 1.4 has now been released, and
addresses several fairly important bugs. First, the full changelog:

-  Fix bug with hmac on Python 2.4. Patch from toshio, closes ticket
   #2133 from the TurboGears2 Trac.
-  Fix bug with occasional ValueError from
   FileNamespaceManager.do\_open. Fixes #10.
-  Fixed bug with session files being saved despite being new and not
   saved.
-  Fixed bug with CacheMiddleware overwriting configuration with default
   arguments despite prior setting.
-  Fixed bug with SyntaxError not being caught properly in entry point
   discovery.
-  Changed to using BlobProperty for Google Datastore.
-  Added domain/path properties to the session. This allows one to
   dynamically set the cookie's domain and/or path on the fly, which
   will then be set on the cookie for the session.
-  Added support for cookie-based sessions in Jython via the JCE (Java
   Cryptography Extensions). Patch from Alex Grönholm.
-  Update Beaker database extensions to work with SQLAlchemy 0.6
   PostgreSQL, and Jython.

Note that the beaker database extension now works on Jython, and the
cookies for sessions can be set dynamically during a request (for sites
that operate across multiple domains/sub-domains).

Most importantly though, a bug in the import of the Google back-end has
been fixed, which caused installation failures on Beaker 1.3.x.

Docs can be found on the `Beaker site <http://beaker.groovie.org/>`_.

To upgrade your Beaker with easy\_install:

::

     easy_install -U Beaker
     

This release is also notable as the majority of the fixes were
contributed by several web framework communities. Thanks for the
patches!


.. author:: default
.. categories:: Pylons, Python
.. comments::
   :url: http://be.groovie.org/post/296328720/beaker-1-4-released
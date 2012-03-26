Pylons 0.9.7 Released
=====================

I'm pleased to announce after a rather lengthy release candidate period,
that Pylons 0.9.7 is finally out. Pylons 0.9.7 brings a good amount of
changes to Pylons from 0.9.6 while still retaining a fairly hefty amount
of backwards compatibility to ensure a mostly painless upgrade.

Some helpful documentation on the new release:

-  `Upgrading to Pylons
   0.9.7 <http://pylonshq.com/docs/en/0.9.7/upgrading/>`_
-  `Pylons 0.9.7 Documentation <http://pylonshq.com/docs/en/0.9.7/>`_
-  `Pylons 0.9.7 Docs in
   PDF <http://pylons.cachefly.net/download/0.9.7/Pylons.pdf>`_
-  `Pylons Book <http://pylonsbook.com/>`_ (Will be updated soon with
   the final copy from the printed book)

Major changes in 0.9.7:

-  Switched to using WebOb for the request/response object
-  Various performance improvements to object initialization
-  Beaker and Routes updates
-  Middleware improvements, and optimizations

This is a huge step forward for Pylons, and I'd like to thank all of the
contributers who have helped make Pylons what it is today. We've knocked
off more bugs for this release than any before, which shows just how far
the Pylons community has come:

-  0.9.5 tickets: 45
-  0.9.6 tickets: 64
-  0.9.7 tickets: 160

And we have finally made a huge dent in the historical “lack of docs”
problem that Pylons previously suffered from with the new Sphinx
generated docs and a comprehensive Pylons book.

The full changelog which describes the major changes (Look for the bits
marked with WARNING that might affect backwards compatibility).

0.9.7 (February 23, 2009)

-  WARNING: A new option is available to determine whether or not an
   actions

arguments should be automatically attached to ‘c'. To turn off this
implicit behavior in environment.py: config[‘pylons.c\_attach\_args'] =
False This is set to True by default.

-  WARNING: Fixed a minor security hole in the default Pylons error page
   that

could result in an XSS security hole.

-  WARNING: Fixed a security hole in the default project template to use
   the

StaticURLParser to ensure arbitrary files can't be sent.

-  WARNING: Refactored PylonsApp to remove legacy PylonsApp, moved

session/cache and routes middleware into the project template. This will
require projects to be updated to include those 3 middleware in the
projects middleware.py.

-  Changed to using WebTest instead of paste.fixture for app testing.
-  Added render\_mako\_def to render def blocks within a mako template.
-  Changes to cache\_decorator and cached\_template to support Beaker
   API

changes in version 1.1. 1.0.3 is still supported.

-  Fix HEAD requests causing an Exception as if no content was returned

by the controller. Fixes #507. Thanks mvtellingen, Petr Kobalicek.

-  Fix a crash when returning the result of “etag\_cache“ in a
   controller.

Fixes #508.

-  “response” flag has been removed from
   pylons.decorators.cache.beaker\_cache,

as it sends all headers along unconditionally including cookies;
additionally, the flag was taking effect in all cases previously so
prior versions of beaker\_cache are not secure. In its place, a new
option “cache\_headers” is provided, which is a tuple of specific header
names to be cached. It defaults to (‘content-type',’content-length').

-  “invalidate\_on\_startup” flag added to beaker\_cache, which provides
   a

“starttime” to the cache such that when the application is started or
restarted, the cache entry is invalidated.

-  Updating host to use 127.0.0.1 for development binding.
-  Added option to specify the controller name with a *controller*
   variable

in the controller's module. This name will be used for the controller
class rather than the default naming scheme.

-  setup.py egg\_info now restores projects' paster\_plugins.txt,

allowing paster shell to work again after the egg-info directory was
lost. fixes #282. Thanks sevkin.

-  The paste\_deploy\_config.ini\_tmpl template is now located at

package/config/deployment.ini\_tmpl for new projects.

-  Project's default test fixtures no longer hardcode test.ini; the ini

file used can now be specified via the nosetests —with-pylons argument
(defaults to test.ini in setup.cfg). fixes #400.

-  ``validate now defaults to translating FormEncode error messages via   Pylons' gettext catalog, then falls back to FormEncode's. fixes #296.   Thanks Max Ischenko. * Fixed SQLAlchemy logging not working in paster shell. Fixes #363. Thanks   Christoph Haas. * Added optionally engine initialization, to prevent Buffet from loading   if there's no 'buffet.template_engines' in the config. * Updated minimal template to work with Tempita and other new templating   changes. * Fixed websetup to parse location config file properly when the section   isn't 'main'. Fixes #399. * Added default Mako filter of escape for all template rendering. * Fixed template for Session.remove inclusion when using SA. Fixed    render_genshi to properly use fragment/format options. Thanks Antonin    Enfrun. * Remove template engine from load_environment call. * Removing template controller from projects. Fixes #383. * Added signed_cookie method to WebOb Request/Response sub-classes. * Updated project template to setup appropriate template loader and controller   template to doc how to import render. * Added documentation for render functions in pylons.templating. * Adding specific render functions that don't require Buffet. * Added forward controller.util function for forwarding the request to WSGI   apps. Fixes #355. * Added default input encoding for Mako to utf-8. Suggested in #348. * Fixed paster controller to raise an error if the controller for it already   exists. Fixes #279. * Added __init__.py to template dir in project template if the template engine   is genshi or kid. Fixes #353. * Fixed jsonify to use application/json as its the proper mime-type and now   used all over the net. * Fixed minimal template not replacing variables properly. Fixes #377. * Fixed ``validate
   decorator to no longer catch exceptions should they be

raised in the action that is supposed to display a form. Fixes #374.

-  Fixed paster shell command to no longer search for egg\_info dir.
   Allows

usage of paster shell with installed packages. Suggested by Gavin
Carothers.

-  Added mimetype function and MIMETypes class for registering
   mimetypes.
-  WARNING: Usage of pylons.Response is now deprecated. Please use

pylons.response instead.

-  Removed use of WSGIRequest/WSGIResponse and replaced with WebOb
   subclasses

that implement methods to make it backwards compatible with the Paste
wsgiwrappers.

-  Fixed missing import in template controller.
-  Deprecated function uses string substitution to avoid Nonetype error
   when

Python optimization is on. Fixes #334.

-  E-tag cache no longer returns Content-Type in the headers. Fixes
   #323.
-  XMLRPCController now properly includes the Content-Length of the
   response.

Fixes #310, thanks Nicholas.

-  Added SQLAlchemy option to template, which adds SQLAlchemy setup to
   the

project template.

-  Switched project templating to use Tempita.
-  Updated abort/redirect\_to to use appropriate Response object when
   WebOb is

used.

-  Updated so that 404's properly return as Response objects when WebOb
   is in

use instead of WSGIResponse.

-  Added beaker\_cache option to avoid caching/restoring global Response
   values

that were present during the first cache operation.

-  Adding StatusCodeRedirect to handle internal redirects based on the
   status

code returned by the app. This replaces the use of ErrorDocuments in
projects.

-  Refactored error exceptions to use WebError.
-  WSGIController now uses the environ references to response, request,
   and

the c object for higher performance.

-  Added optional use of WebOb instead of paste.wsgiwrapper objects.
-  Fixed bug with beaker\_cache defaulting to dbm rather than the beaker

cache app-wide default.

-  The —with-pylons nose plugin no longer requires a project to have
   been

registered with setuptools to work.

-  The config object is now included in the template namespace.
-  StaticJavascripts now accepts keyword arguments for StaticURLParser.

Suggested by Marcin Kasperski.

-  Fix pylons.database.AutoConnectHub's doInTransaction not
   automatically

connecting when necessary. Fixes #327.


.. author:: default
.. categories:: Python, Code, Pylons
.. comments::
   :url: http://be.groovie.org/post/296328884/pylons-0-9-7-released
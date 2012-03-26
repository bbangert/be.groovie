Pylons 0.9.4 Released
=====================

It's with great pleasure that I announce the release of Pylons 0.9.4.
This release has quite a few bug fixes and enhancements, the most since
the 0.9 milestone. It's also likely one of the last big updates before a
1.0 release candidate (there will be some small changes in 0.9.5 and
possibly a 0.9.6).

First, the most important changes for those upgrading from an existing
Pylons application:

-  WARNING: Removed the lang\_extract and lang\_compile commands. They
   used

pygettext.py and its associated msgfmt.py, which lacked the ability to
extract ngettext style function calls and had issues with unicode
strings. The new I18NToolBox project aims to provide this functionality
(and more) via the gettext command line utilities.
`http://i18ntoolbox.ufsoft.org <http://i18ntoolbox.ufsoft.org>`_

-  WARNING: Myghty's allow\_globals config var has changed, causing the

following when running pre-compiled templates: Error(TypeError):
do\_run\_component() takes exactly 13 non-keyword arguments (5 given)
Delete the compiled Myghty templates directory (specified by cache\_dir
or myghty\_data\_dir in the config file) to resolve the error.

-  WARNING: The localization function ‘\_' now uses ugettext (returns
   unicode

strings) instead of gettext. To preserve the old behavior, append the
following line to your project's lib.base and lib.helpers imports: from
pylons.helpers import gettext as \_

-  WARNING: Removed 0.8.x legacy code and backwards compatibility
   functions.

Please note that since some i18n functions have moved, your helpers.py
will need to be updated to import \_, and ungettext from pylons.i18n.

Also:

- The XMLRPC Controller got a significant update so that it now provides
the full range of XML-RPC Introspection facilities for your service
methods.

- SQLAlchemy convenience functions have been added to pylons.database
for use with the SessionContext plugin, and to create and retain SA
engines.

- Paste dependency was updated to 1.1.1, Routes to 1.6.1 (important
update for map.resource functionality)

- Pylons special objects (g, c, h, request, session) now available in
interactive debugger without \_attach\_globals.

- Controller actions can now be generators

- Pylons base WSGI app uses wsgi.org routing\_args spec for easier
swapping of URL resolvers.

Install
-------

Please see
`http://pylonshq.com/docs/0.9.4/install <http://pylonshq.com/docs/0.9.4/install>`_
for installation details.

Full Changelog
--------------

-  WARNING: Removed the lang\_extract and lang\_compile commands. They
   used pygettext.py and its associated msgfmt.py, which lacked the
   ability to extract ngettext style function calls and had issues with
   unicode strings. The new I18NToolBox project aims to provide this
   functionality (and more) via the gettext command line utilities.
   `http://i18ntoolbox.ufsoft.org <http://i18ntoolbox.ufsoft.org>`_
-  All Pylons special objects are now available within paster shell (not
   just h and g).
-  WARNING: Myghty's allow\_globals config var has changed, causing the
   following when running pre-compiled templates:

Error(TypeError): do\_run\_component() takes exactly 13 non-keyword
arguments (5 given) Delete the compiled Myghty templates directory
(specified by cache\_dir or myghty\_data\_dir in the config file) to
resolve the error.

-  Changed i18n functions in templates to use proxy objects so that
   using set\_lang in a template works right. Fixes #153.
-  Now allowing any template plugin to overwrite global PYLONS\_VARS
   (such as c, g), not just pylonsmyghty.
-  Adding SQLAlchemy support to the database.py file. Saves the session
   engine to g to maintain it during the apps lifetime. Uses
   SessionContext plugin for management of the current session.
-  Updated config object so that init\_app can take an optional template
   engine argument to declare the default template engine.
-  Updated Myghty plugin to use extra\_vars\_func when passed in.
-  Fixed Buffet to use extra\_vars\_func properly.
-  Fixed the validate decorator when there are validation errors and
   variable\_decode=True: now passing the original params to
   htmlfill.render instead of the varable\_decode'd version. Patch by
   FlimFlamMan.
-  Added ungettext function for use with pluralized i18n, and the N\_
   function (gettext\_noop) to mark global strings for translation.
   Added ungettext, N\_ and translator objects to be globals for
   templates. Refs #126.
-  WARNING: The localization function ‘\_' now uses ugettext (returns
   unicode strings) instead of gettext. To preserve the old behavior,
   append the following line to your project's lib.base and lib.helpers
   imports:

from pylons.helpers import gettext as \_

-  Pylons special objects are now available within the interactive
   debugger (deprecating \_attach\_locals).
-  Added setup-app run before unit tests run so that webapp has proper
   setup tasks handled. Fixes #113.
-  Added paste.deploy.CONFIG setup to middleware.py, websetup.py and
   testing files in the Pylons project templates. Closes #112.
-  Added security policy doc to index for use as Pylons security policy.
   Closes #91.
-  Improved the repr() of the c context object to show attributes.
-  Set environ[‘paste.testing\_variables'] whenever that key is
   available, not just in testing mode.
-  Added capability to have an action be a generator function.
-  Added introspection capability to XMLRPCController and signature
   checking.
-  Updated Controller to use additional arg lookup scheme so that the
   source of the function args for \_inspect\_call can be easily
   overridden.
-  Updated RPCController, renamed to XMLRPCController. XMLRPCController
   now functions properly and will automatically return proper xmlrpc
   responses.
-  Added test configuration ini file to default template. Closes #114.
-  Fixed problem with pylons.database.PackageHub.*get* raising errors
   other than AttributeError when the database isn't configured. Added
   new UnconfiguredConnectionError exception, instead of just KeyError
   or TypeError (depending on what part of the configuration failed).
-  Fixed default g init, since bare object has no init method. Reported
   by Ian Bicking.
-  Fixed issue with SQLObject method override having wrong name.
   Reported by climbus with patch. Fixes #133.
-  Moved log function to pylons.helpers and translation functions to
   pylons.i18n. using pylons.util purely for Pylons internal util
   functions.
-  WARNING: Removed 0.8.x legacy code and backwards compatibility
   functions.
-  PylonsApp now has option to not use Routes middleware, default
   resolving uses new wsgi.org routing\_args spec.
-  Refactored routes dispatching to use new Routes middleware.
-  Fixed paster shell command to properly acquire mapper object without
   relying on the template being configured in a specific manner.
-  Added keyword argument pool\_connection to
   pylons.database.PackageHub; if set to false then SQLObject
   connections won't use pooled database connections (a new connection
   will be opened for each request).

Many thanks to Phil Jenvey, Ian Bicking, James Gardner, and all the
other active members of the Pylons community!

Cheers,
Ben


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296346040/pylons-0-9-4-released
Pylons Related News for the 4th of July
=======================================

It's been a busy month for `Pylons <http://pylonshq.com/>`_, with lots
of changes for the big internal API change in 0.9. The great news for
those making Pylons apps right now with 0.8.2 is how **few** backwards
compatibility issues there are. Most of the big changes take place under
the hood and compatibility objects are present to mitigate the massive
breakage that I've seen happen in other framework upgrades.

This is going to remain a big focus on future development in Pylons too,
and the API in 0.9 is solid enough that I don't see anything but minor
tweaks in the future (1.0 and beyond). Pylons based apps will be easy to
maintain and upgrade thanks primarily to WSGI.

No `NIH Syndrome <http://en.wikipedia.org/wiki/Not_Invented_Here>`_ Here!
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

We've taken some cues from the `Django
project <http://www.djangoproject.com/>`_ that we believe make for a
cleaner request-cycle. In Pylons 0.9, controllers are expected to return
a ``response`` object, and for convenience a method is included that
renders a template to a new response object and returns it (This will
look very familiar to Djangonauts).

The command was integrated with a slightly more enhanced version of
`Buffet <http://projects.dowski.com/projects/buffet>`_ along with the
`Beaker Session/Caching middleware <http://beaker.groovie.org/>`_. The
end-result is a powerful command that not only can render templates in
any `Template-Plugin
compatible <http://www.turbogears.org/docs/plugins/template.html>`_
template language, but the rendered result can also be cached. It's a
great way to utilize template languages which might not be all that
quick by themselves.

Sample controller in Pylons 0.9:

::

    from myproj.lib.base import *

        class UserController(BaseController):
        def show(self, id):
            # Cache based on id in the URL, for 30 seconds
            return render_response('/user/show.myt', cache_key=id, cache_expire=30)

        def index(self):
            # Just for fun, use Kid to render the index
            return render_response('kid', 'user.index', cache_expire=15)

Being able to easily cache any template in any template language makes
it very easy to sprinkle in caching when you need to handle massive
loads yet stay dynamic.

Another new feature present in the latest
`Routes <http://routes.groovie.org/>`_ and Pylons is resource mappings,
which automatically generate routes for you with HTTP method
restrictions. This makes it easy to setup controllers and their actions
for specific HTTP verbs (aka, REST-ful URL's and web services). The
implementation of this feature was directly inspired by the `Simply
Restful <http://plugins.radrails.org/directory/show/69>`_ Rails plug-in
that was also demo'd by David Hansson in his `Resources on
Rails <http://www.loudthinking.com/arc/000593.html>`_ talk. Being able
to `discriminate valid routes based on HTTP
method <http://groups.google.com/group/pylons-discuss/browse_frm/thread/86f8abc048dd7ce7>`_
was brought up in the past and I'm happy to have seen an implementation
that solves the issues I originally had with the idea.

The one feature still in development is to easily discern the content
type requested, which was also inspired by Rails. Josh Triplett has
written some code that deals with the ugly task of parsing the HTTP
Accept headers, and I'm working on adding it into Paste for easy re-use
by all. Combined with Routes, it'll provide a clean and easy way to
setup web applications that can serve multiple forms of content from a
single action.

Conferences
^^^^^^^^^^^

Pylons was represented at `EuroPython <http://www.europython.org/>`_ by
the other lead developer of Pylons, James Gardner. For those still
trying to grasp WSGI, he gave a `talk on WSGI and
middleware <http://indico.cern.ch/materialDisplay.py?contribId=104&amp;sessionId=9&amp;materialId=slides&amp;confId=44>`_
that looks like it was quite interesting (I wasn't there unfortunately.)

Other talks involving Pylons at EuroPython:

-  Dr. Rob Collins gave a `presentation on Factory monitoring with
   Pylons, XML-RPC and
   SVG <http://indico.cern.ch/contributionDisplay.py?contribId=109&sessionId=50&confId=44>`_
-  James Gardner's `full talk on
   Pylons <http://indico.cern.ch/contributionDisplay.py?contribId=105&sessionId=9&confId=44>`_,
   and `slides of his Pylons
   talk <http://indico.cern.ch/materialDisplay.py?contribId=105&amp;sessionId=9&amp;materialId=slides&amp;confId=44>`_
-  Web Framework Shoot-out between Django, Zope, TurboGears, and Pylons
   (If more were covered, please let me know)

I'll be at `OSCON <http://conferences.oreillynet.com/os2006/>`_ for
those interested in chatting about Pylons, Python, or Python web
frameworks later this month.

Pylons 0.9 Release
^^^^^^^^^^^^^^^^^^

We're currently wrapping up new features in 0.9, to make sure the
resource mapping capability is present before a feature-freeze for
release. Hopefully the release will be out within the next 2 weeks, if
you haven't checked out Pylons before I'd highly suggest taking a look
at 0.9!


.. author:: default
.. categories:: Python, Code, Routes
.. comments::
   :url: http://be.groovie.org/post/296346174/pylons-related-news-for-the-4th-of-july
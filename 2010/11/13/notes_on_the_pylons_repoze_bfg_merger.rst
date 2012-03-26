Notes on the Pylons & repoze.bfg Merger
=======================================

Some folks might not have time to follow the Pylons-discuss mail list,
so this might be news to them, but I’m thrilled to announce that the
Pylons and repoze.bfg web frameworks are merging. If this is the first
you’ve heard about it, don’t worry, it was only announced a week ago now
on the Pylons mail list.

In the time since the announcement, I’ve heard a lot of varying
feedback. Some people took a look at Pyramid (the core package that will
be equivilant to ‘Pylons 2.0’) and were quick to respond, usually in a
knee-jerk type response. I think some of this was due to a
miscommunication, and partly because there was so much already done.
When other frameworks have merged in other languages, such as Rails
merging with Merb, the announcement was just that. There was no code at
the time to show, just a promise that when it was ready, it would be
awesome.

This merger in contrast already had a starting foundation for a huge
chunk of the core features. As a result, people assumed that what we had
was already ‘finished’, or close to it. The polish of much of the
documentation made it feel odd that there was no “Porting Pylons 1.0 to
Pyramid” guide done. In reality, Pyramid is **definitely not done**,
there is still quite a bit of work left before Pyramid will meet the
expectations that many Pylons users have. There’s still refinements to
be done to Pyramid, and additional packages that Pylons users will most
likely always use with it for the feature-set they’re accustomed to.

I’ve `summed up a few thoughts on when Pylons users should port to
Pyramid <http://docs.pylonshq.com/faq/pyramid.html#should-i-port-my-pylons-1-0-project-to-pyramid>`_
to try and help manage expectations better in the future. I’ll make more
announcements when packages are ready to ease the transition and a
“Porting Guide” is ready.

What is Pylons?
---------------

Many Pylons users don’t realize which features they enjoy come from the
package ‘pylons’ vs. the other packages that Pylons depends on. Contrary
to popular belief the majority of features present in Pylons actually
come from other packages. This mistaken belief that most of the features
come from the pylons package led some to think that because a lot of my
future development time will be spent on adding features/packages around
pyramid, Pylons is somehow *dead>*. This is not the case.

First, Pylons the web framework is mainly a small (~ 1000 LoC) glue
layer between Paste, PasteScript, PasteDeploy, WebOb, WebError, Routes,
WebHelpers, Mako, and SQLAlchemy. Some people usually end up swapping
out Mako/SQLAlchemy but by and large this is the common ‘Pylons Stack’.
Most of the new features in Pylons over the past several years actually
came from additions to WebHelpers, WebError, or Routes. All of these
packages continue to get the same development as they have, so no
‘death’ is occurring.

Second, for over the past 6 months now, there’s been very little in the
way of patches submitted, bugs reported, or other feature requests. In
many ways Pylons is ‘done’ regarding adding more feature to the core
package itself. As I `announced on the Pylons-discuss mail
list <http://groups.google.com/group/pylons-discuss/browse_thread/thread/97faa18a3429a28e#>`_,
the Pylons code-base hit some design issues. Adding the features I heard
requested from quite a few users (and needed myself) regarding
extensibility couldn’t be retro-fitted into the existing design. I
encourage anyone curious to read my prior entry on sub-classing for
extensibility to be a preview of some future blog posts. I’ll be writing
more about design patterns in Python that handle extensibility which
many popular Python web frameworks are also struggling to handle.

The Future
----------

I’m very excited about the future for the Pylons Project, which is the
new over-arching organization that will be developing Python web
framework technologies. The core will be Pyramid, with additional
features and functionality building around that. We’re already quickly
expanding the developer team with some long-time contributors and having
a combined team has definitely helped us progress rapidly.

One of my main goals is to encourage and ease contributions from the
community. To that extent I’ve been `filling in the contributing section
for the Pylons Project <http://docs.pylonshq.com/#contributing>`_ as
much as possible. I believe this is an area that will quickly set us
apart from other projects as we emphasize a higher standard of Python
development.

Django did a good job setting the bar high for its documentation of how
to `contribute to
Django <http://docs.djangoproject.com/en/dev/internals/contributing/>`_,
which deserves a lot of credit for clearly defining community policies.
Its missing a portion we considered extremely valuable which core
developers generally get very picky on when accepting patches… how to
**test your code**. The Pylons Project adapted the rather thorough
`testing dogma noted by Tres
Seaver <http://docs.pylonshq.com/community/testing.html>`_, which I
personally can’t recommend highly enough when it comes to writing unit
tests. It’d be nice to see more posts expand on exactly *how to test
your code*. Many developers (including myself) can write code that
passes 100% test coverage… but is it brittle test code? Prone to failure
if some overly clever macro it uses fail? Seeing a well written set of
examples on designing unit tests to avoid common gotcha’s is definitely
something anyone contributing (and developers in general) should be
familiar with.

For those wanting a gentler introduction to Pyramid (the docs are very
verbose and detailed, not at all opinionated), I’ll be blogging more
about new features and how to utilize them. Please be patient, I think a
lot of people are going to be excited at what’s in store.


.. author:: default
.. categories:: pylons, python
.. comments::
   :url: http://be.groovie.org/post/1558848023/notes-on-the-pylons-repoze-bfg-merger
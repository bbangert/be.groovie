Pylons 0.10 and 1.0 Beta 1 Released
===================================

Without further ado,

I’m pleased to announced that Pylons 0.10b1 and 1.0b1 are now out. I
have not put them on Cheeseshop to ensure they’re not downloaded
accidentally.

Upgrading / Installing
----------------------

I have updated upgrading instructions here:
`http://pylonshq.com/docs/en/1.0/upgrading/ <http://pylonshq.com/docs/en/1.0/upgrading/>`_

The instructions to install from scratch on Pylons 1.0b1:
`http://pylonshq.com/docs/en/1.0/gettingstarted/#installing <http://pylonshq.com/docs/en/1.0/gettingstarted/#installing>`_

The upgrading page covers the important upgrading instructions that Mike
Orr touched briefly on before.

Note that these are *beta* releases, intended for us to discover
remaining issues and continue updating any other documentation where
applicable. Very little has actually changed in Pylons since 0.9.7,
apart from 1.0 dropping all of the legacy functionality and a few
explicit clean-ups.

Updates
-------

Routes, Beaker, and WebHelpers however have been seeing quite a bit of
updates through the life of Pylons 0.9.7 so no one should think that the
developers working on Pylons and its related parts have been hanging out
doing nothing. :)

Since Pylons 0.9.7 was released on February 23, 2009, almost one year
ago now:

-  Routes 1.11 was released, and 1.12 with some great updates will be
   out shortly
-  Beaker has gone from 1.2.2 -> 1.5 with 3 major updates substantially
   increasing its ease of use and reliability
-  WebHelpers is now at 1.0b4 with major updates, core functions
   rewritten, and new docs up
-  SQLAlchemy has gone from 0.4 to 0.5 (with 0.6 in beta)

I believe this speaks a great deal about the benefits of keeping the
core Pylons functionality separate from other parts, as a variety of bug
fixes and features can be improved without requiring new Pylons releases
to quickly address bug reports.

How to Help!
------------

To bring Pylons to 1.0, many docs likely need very small changes. Also,
it would be great to take care of reference docs where people have
commented about problems/tips. Helping is fairly easy, especially if
you’re familiar with restructured text.

First: Clone the Pylons repository on Bitbucket:
`http://bitbucket.org/bbangert/pylons/ <http://bitbucket.org/bbangert/pylons/>`_

Then: Edit the documentation files under pylons/docs/en/ to read as
appropriate, commit the fix, and push it to bitbucket.

Finally: Issue a pull request on bitbucket so that we’ll know your fix
is ready. Ideally you should include a note in it about what your fix
remedies.

Bug Reports
-----------

Did your upgrade not go according to plan? Was there something missing
that you needed to do from the upgrading docs?

Let us know by filing a bug report (mark component as documentation, and
milestone as 0.10:
`http://pylonshq.com/project/pylonshq/newticket <http://pylonshq.com/project/pylonshq/newticket>`_

You’ll need to login to file a bug report, or feel free to reply to this
announcement with the issue.

Thanks (in alphabetical order) to Mike Bayer, Ian Bicking, Mike Burrows,
Graham Higgins, Phil Jenvey, Mike Orr, and anyone else I missed for all
their hard work on making Pylons and its various components what they
are today.


.. author:: default
.. categories:: Pylons, Python
.. comments::
   :url: http://be.groovie.org/post/373440559/pylons-0-10-and-1-0-beta-1-released
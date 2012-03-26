Most bizarre Git service and other stupid Rails powered "businesses"
====================================================================

I can't help but get totally baffled when I see a `business model like
this <http://github.com/plans>`_.

Yes, that's right, you can pay for the privilege of keeping a copy of
your **distributed** version control system (DVCS) **private**
repositories on someone else's machines. You also get to pay depending
on how many people you want to allow to collaborate on it.

Nevermind that one of the **entire points of a DVCS** is that you **do
NOT** need a central repository. Does anyone actually work at a “Large
Company” (as the page indicates) that would be stupid enough to pay
$100/month so they can put all their proprietary and very personal code
repositories on a third party web service?

So what are you paying for? Well, to start with, they have awesome
integration with `Lighthouse <http://lighthouseapp.com/>`_, since we all
know there's no decent free open-source issue tracking system… **cough**
`trac <http://trac.edgewall.org/>`_ **cough**
`roundup <http://roundup.sourceforge.net/>`_ **cough**. Oh wait, since
there's absolutely no simple web-based issue tracking systems, let's
have another `slick business
model <http://sera.lighthouseapp.com/plans>`_ to get people to pay for a
stripped down Trac (but this time with a really pretty UI)!

What do these sites have in common? Rails, “look ma, I can copy-paste
the business plan too” pricing models, and some good graphic designers
at the helm. There also seems to be an interesting amount of promotion
between these sites, as well as a nice `blog post from the Rails creator
himself <http://www.loudthinking.com/posts/24-gits-avalanche>`_
promoting GitHub. I'm sure no one who has read `this
rant <http://www.zedshaw.com/rants/rails_is_a_ghetto.html>`_ should be
surprised though.

I only hope that no one starts to believe that a DVCS actually requires
these “please pay” copies of their DVCS repo.

**Update (11/12/2008)**: This post is apparently popular enough to come
up on occasion several times now, so I thought I'd clarify a bit more.

Many people have suggested the obvious benefits of services like GitHUB,
and I've used one just like it myself,
`BitBucket <http://www.bitbucket.org/>`_. These sites are great for
open-source projects as many have rightfully pointed out, they make it
easy to collaborate and fork projects, and easy for maintainers to pull
patches from forks after looking them over.

Most of their social-network features become moot though when working on
company code thats not open-source, (note that this rant is directed
entirely at the paid service options which are for **private** repos).
None of the companies I've worked at would ever let their private source
code leave their own servers. Since you need to deploy a site anyways
(many times to a remote computer), which will generally require ssh
access, its trivial to use the modern DVCS's over ssh…. which makes it
seem very silly to me to be paying so much to another company for a
bunch of useless social features for a private repo.

Part of the original humor intended in this rant was that a
**centralized repo hub** has become one of the stronger selling points
for a **distributed** VCS system. Unfortunately many seemed to have
missed that point.


.. author:: default
.. categories:: Rants
.. comments::
   :url: http://be.groovie.org/post/296342818/most-bizarre-git-service-and-other-stupid-rails-powered
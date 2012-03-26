Followup to "Best of Breed Controllers"
=======================================

My prior post regarding `Best of Breed
Controllers <http://groovie.org/articles/2005/09/30/best-of-breed-controllers-for-mvc-web-frameworks>`_
got more notice than I had anticipated, I definitely didn't expect the
interesting discussion regarding `object
publishing <http://66.249.93.104/search?q=cache:31QtpwbEzvIJ:www.etsimo.uniovi.es/python/workshops/1996-11/papers/PythonObjectPublisher.html+pythonobjectpublisher&hl=de&lr=&client=firefox-a&strip=0>`_
history it spawned.

But first, some corrections:

-  `Kevin Dangoor <http://www.blueskyonmars.com/>`_ points out that
   `CherryPy <http://www.cherrypy.org/>`_ allows for computed URL
   traversal by having the parts of the URL passed into a default
   function with a function signature like
   ``def default(self, other, parts, of path):``. On a side-note, I
   believe `David Creemer <http://www.zachary.com/>`_ is using this
   aspect in his use of `Routes <http://routes.groovie.org/>`_
   `integration with
   CherryPy <http://www.zachary.com/s/blog/2005/10/01/integrating_cherrypy_and_routes>`_
   to some extent.
-  `Mike Watkins <http://mikewatkins.net/>`_ gives a `great
   overview <http://mikewatkins.net/categories/technical/about_quixote_part1.html>`_
   of `Quixote <http://www.mems-exchange.org/software/quixote/>`_ on his
   blog. He also shows how it fits into the categories I mentioned above
   and `points to a hello world web
   app <http://www.mems-exchange.org/software/quixote/Quixote-2.2.tar.gz/Quixote-2.2/demo/mini_demo.py>`_
   that again looks similar to the other frameworks.
-  `Adiran Holovaty <http://www.holovaty.com/>`_ notes that Django
   controllers can be callable's too, and that my example is somewhat
   misleading regarding the amount of code required for a basic
   controller. This is because the example I took from the Django
   documents was from a fairly advanced controller that was doing a lot
   of work.
-  Robert Brewer mentions that CherryPy controllers can be any callable
   that allows an “exposed” attribute to be set on it, though they tend
   to be class methods as its easier to hook them into the cherrypy.root
   handler tree. Also, CherryPy doesn't officially advocate any
   templating language.

In a way, Phillip J Eby's correction regarding the history could be in
the list above. However, it really wasn't my intention to get into a
discussion regarding object publishing history. For anyone considering
making YAPWF, I'd definitely advocate catching up on lessons learned in
the past as it makes no sense to repeat their mistakes. I think in
hindsight, a better heading for that section would've been **Who didn't
do it first** as the real intention of the section was so that people
wouldn't assume one of the frameworks I mentioned was the *first* to
come up with it.

For those interested in the history of Zope, its predecessor Principia
and Bobo, I'd highly suggest reading the above link to Object Publishing
along with `Phillip Eby's
comment <http://groovie.org/articles/2005/09/30/best-of-breed-controllers-for-mvc-web-frameworks#comment-49>`_
and `Paul Everitt's response <http://radio.weblogs.com/0116506/>`_. I've
found it all rather fascinating as most of the frameworks I showed
looked so similar to Bobo. So nice to know that an old Python ‘adage' I
read (probably on some comparison of Python and Ruby) seemed to hold up
here. *If you give the same task to a dozen Python programmers, the
solution is going to look quite similar.*


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296349674/followup-to-best-of-breed-controllers
Sacrificing readability for automated doc tests
===============================================

I've tried several times in the past to try out
`zc.buildout <http://pypi.python.org/pypi/zc.buildout>`_, a fairly neat
sounding package that automates the buildout process for a Python app.
The promise of fairly easy to write recipes that can setup external
processes like nginx in addition to ensuring my webapp is put together
with all the things it needs sounded great.

It occurred to me that the docs definitely didn't help at all. In fact,
they're noticeably bizarre unless you actually realize **why** they're
written the way they are. Here's a `sample of the zc.buildout
docs <http://pypi.python.org/pypi/zc.buildout#creating-new-buildouts-and-bootstrapping>`_
about how to make a new buildout and bootstrapping.

You'll notice that it almost looks like command line interactions of
some sort are occurring, yet the author of the docs is clearly at an
interactive Python prompt. Note that none of the commands shown there
will work if you copy them into your Python interpreter, nor is there
any indication what you would need to do to get such commands available.
As a user trying to follow the docs, that leaves me wondering… am I
supposed to be in a Python interpreter? What do these variables get
expanded to so that I can do that at my shell prompt? Why can't you just
give me the damn command line I'm supposed to run so I can copy/paste???

Yes, it definitely got me a bit frustrated. I believe the only logical
reason the docs were in this bizarre fashion is so that they could be
automatically doc-tested. Its a shame that the result of this is docs
that make me want to close the web page as soon as I stumble upon the
‘samples', since there's no way I can handle wading through the command
line abstractions.

Doctests can be useful, but turning command line interactions into a
Python interactive session is a massive readability issue. People know
and recognize command line interactions, lets stick with them please.


.. author:: default
.. categories:: Python, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296343007/sacrificing-readability-for-automated-doc-tests
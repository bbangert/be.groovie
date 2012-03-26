The Wacky World of Ruby
=======================

Ruby is a fairly interesting programming language, from the “expressive”
syntax to some of the `absolutely bizarre
documentation <http://poignantguide.net/ruby/>`_. For a Python
programmer, the lack of predictability and almost excessively concise
syntax (when just one more line would really make things **a lot
clearer**) can be a bit of a downer. Overall though, I'm rather enjoying
my experiences with Ruby but not enough that I'd want to use it
exclusively.

The “Wacky” bit I cite, comes from some of the strange directions the
language seems to go and wacky documentation and books available. Now,
the creator of Ruby is completely aware about some of the `ways in which
Ruby sucks <http://www.rubyist.net/~matz/slides/rc2003/mgp00004.html>`_
as he put it, and 3 of those are of particular importance to Python
programmers since we enjoy a concise (and not complex), predictable, and
consistent language. Ruby is `working to address these issues in the
upcoming 2.0 release <http://www.rubygarden.org/ruby?Rite>`_ which I'm
hoping will make it more pleasant to work with.

It is also somewhat wacky the way the Ruby community has `compared
themselves to other programming language
communities <http://www.martinfowler.com/bliki/RubyPeople.html>`_ to
which `this blogger has a fairly friendly
reply <http://ericburke.com/blog/2005/09/26/50>`_. Sometimes these
little jabs run into the printed documentation regarding Ruby as well,
which is a big turn-off for me, especially since I really disagree with
the reasons that are cited for insulting other languages.

Beyond Java?
^^^^^^^^^^^^

Take the `Beyond Java <http://www.oreilly.com/catalog/beyondjava/>`_
book for example. About half-way in it becomes very clear that the
author's view of what is Beyond Java…. is Ruby, and for web programming,
Ruby on Rails. The author then goes on to smash Perl, Python, and PHP
(ok, I agree with him on PHP :). He puts Ruby in the mix as well, but
the only bad thing he says about it is that its lacking commercial
backing (except for later on where a new reason emerges).

His comments regarding Python are truly wacky though, as he jumps back
to the very old “white-space reliance sucks” argument that hardly ever
comes up in the real world. I've been using Python for over a year now,
and have worked on quite a few collaborative projects, and have yet to
see a single error related to mismatched white-space. This is probably
because `coding standards are well
known <http://www.python.org/peps/pep-0008.html>`_ and Python
programmers **actually follow them for the most part**. It's hard to
express how wonderful this has made it when I've jumped into code
written by other people, and have been able to easily scan it and add
functionality after just a few minutes of looking it over.

When I've jumped into other people's Ruby code looking to make a
quick-fix, the syntax quickly became a massive chore to decipher as
Perl's motto of
`TMTOWTDI <http://catb.org/~esr/jargon/html/T/TMTOWTDI.html>`_ holds
very true in Ruby as well.

The Beyond Java book also cites Python's lack of a “killer app” when it
comes to web programming and specifically references `Ian Bicking's
article on web programming
frameworks <http://blog.ianbicking.org/why-web-programming-matters-most.html>`_.
Of course, since that article Ian has put out `Python
Paste <http://pythonpaste.org/>`_ which solves a host of problems he
mentioned there, and the Python web community's move to WSGI is helping
to standardize methods of running Python web applications.

Even more wacky, later in the Beyond Java book, in yet another
comparison of whats for and against the languages, a different reason
pops up for Ruby not doing so good. What is it this time?

*The biggest strike against Ruby right now is the lack of a strong
project that lets Ruby run on the JVM.* – Page 163

He goes on to cite how much support Ruby would get if Microsoft was able
to woo the Ruby founders over to .NET's CLR. On the very next page (165)
another for and against argument comes out for Python. Since the author
just mentioned the JVM and .Net CLR as major drawbacks to Ruby, I was
actually expecting him to mention `Jython <http://www.jython.org/>`_, or
even `IronPython <http://www.ironpython.com/>`_ which is actually being
developed by a programmer now at Microsoft. Amazingly enough, neither of
these projects is mentioned here, though Jython was mentioned back near
the beginning as being too slow (which IronPython apparently solves).

It gets even more wacky a few more pages in, as his reasons against Perl
come out.

*Perl does have a downside. When you look at overall productivity of a
language, you've also got to take things like maintenance and
readability into account. Perl tends to rate very poorly among experts
on a readability scale.* – Page 174

Who these experts are is never mentioned, and I've seen “experts” for
and against the Perl syntax. While Ruby is easier to read than Perl in
my personal opinion, its nowhere near as easy to read as Python.

Programming Ruby, The Pragmatic Programmers Guide
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I've been reading this book for awhile now, and the author's decision to
*do something different* is admirable but has really been a bane to
reading the book. I've also read the `Agile Web Development with
Rails <http://www.amazon.com/exec/obidos/redirect?path=ASIN/097669400X&link_code=as2&camp=1789&tag=groovie-20&creative=9325>`_
book, which I think was done in a most excellent manner (written by Dave
Thomas, the author of Programming Ruby). So this isn't an attack on
Dave, as I really enjoy his writing, I just believe this approach didn't
work so well.

The approach taken in Programming Ruby is to **breeze over high-level
uses of the language without actually explaining much about why things
acted as they do**. This quickly drove me nuts, and I stopped reading
the entire intro as seeing syntax for no reason wasn't helping me learn
anything. If you want to learn Ruby in the way most programming books
teach a language, by carefully and completely going over all the parts
then doing more advanced things; skip to page 317 in the **Ruby
Crystallized** Part.

Once I started reading here, everything fell into place very nicely and
the language really started to make sense. If the sections were reversed
as most programming books have it, I'd consider this book pretty much
perfect for a programming book. The thing I think Dave might have missed
here, is that most programming books follow this convention because it
works. Being different, just to be different, isn't very good unless
there's a real and practical reason for doing it.

The wackiness doesn't end though, and I have yet to complete the entire
book so I can't say how many more examples of this are there. Here's the
latest gem though, which actually prompted this entry (though I've been
thinking these thoughts for awhile).

On Page 330, going over the details of Variables and Constants, I came
across this:

*Ruby, unlike less flexible languages, lets you alter the value of a
constant, although this will generate a warning message.*

**HUH?** Errr, then **why the heck do they call it a Constant??**
Seriously, maybe its because I'm picky on language terms used but I
think they should've called it a semi-Constant, or a mostly-Constant
Constant. For me, this goes against the entire notion of what a Constant
is. Then, on top of that, it insults other “less flexible languages”
that (\_gasp\_) **don't let you change constants**.

It's a Wacky World
^^^^^^^^^^^^^^^^^^

There's many more examples of the wackiness present in the Ruby world.
Perhaps its because the language is from Japan, home to so many wacky
things by Western standards. Though the writers I mentioned are all
non-Japanese, so this explanation doesn't really cut it. To be fair, the
Beyond Java book is well written and the reasons cited in many of the
comparisons are valid to an extent.

Ruby in Rails also has its share of wackiness, though it seems so
abundant I'll have to save that for another post entirely. If you're
wondering after all this, why I'm still using Ruby… well, it's a wacky
world, and I do kind of like wacky (I think I've used up all allowed
uses of the word ‘wacky' by now). Ruby 2.0 looks to be quite appealing
and it'll be interesting to see how Rails adapts to so many breakage's
that 2.0 appears to introduce over 1.8.

Python isn't perfect either, and I'm not going to claim it is. There's
plenty of people in both the Python world and the Ruby world who are
very forthcoming about failures and successes of the language, so the
views expressed by the authors in these books should not be taken to
represent the whole. They are some of the most visible speakers though,
so I hope that they can someday be as forthcoming as Matz has been.


.. author:: default
.. categories:: Python, Rants, Ruby, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296349338/the-wacky-world-of-ruby
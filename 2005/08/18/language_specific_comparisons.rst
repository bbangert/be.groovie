Language Specific Comparisons
=============================

I've read quite a bit of `Paul Graham's <http://www.paulgraham.com/>`_
articles regarding Lisp, how awesome Lisp is, how much of a
`dufus <http://people.csail.mit.edu/gregs/ll1-discuss-archive-html/msg01477.html>`_
one might be for using a language programmed for dufuses.

Now, before I start, I should mention that these posts are quite old,
and **I don't really want to start a flame fest over this again**.
However, I couldn't help but notice today with a problem I had in my
code, how easy Python made the solution (Zach points out the Lisp
solution is quite succinct as well).

Without a doubt, Lisp excels at recursion, function/code generation, and
closures. This frequently leaves Lisp looking like a god when you see
how many lines of code other languages take to replicate the examples
Paul chooses to compare (which always revolve around the things Lisp
excels at as `Paul Prescod points
out <http://www.prescod.net/python/IsPythonLisp.html>`_)

Today, I came across a fairly common case, where I had a function taking
keyword arguments and collecting them all. That would look like this in
Python:

::

    def somefunc(**kargs):

Now, if I want to take two of those keyword being passed in, and set
some defaults so they're not required but will always have something set
in the function body, its rather easy:

::

    def somefunc(keyone='default', keytwo='anotherdefault', **kargs):

So in one line, I have now added two defaults that will be available in
my function body for use. [STRIKEOUT:How succinct is this in Lisp?] What
about in Ruby?

I cite two languages that came off very well in the `Accumulator
Generator <http://www.paulgraham.com/accgen.html>`_ shoot-off.
[STRIKEOUT:They] Ruby doesn't do quite as well in this case, which I've
actually encountered far more than the code generation cases Graham is
apt to cite. (I actually like Ruby and am now using it quite a bit, I'll
be quite happy when it has keyword args)

What's even worse is where in `this
thread <http://people.csail.mit.edu/gregs/ll1-discuss-archive-html/msg01477.html>`_
that I referenced above, Graham at the end says he has no clue how one
would create a basic class to handle accumulation in Lisp. [STRIKEOUT:I
find that rather disturbing that something so easy in Python has Graham
saying, “God only knows.” how to do it in Common Lisp] Richard points
out below that this is because PaulG is rather keen on macros, and not
so big on OO. That makes complete sense to me as Lisp did not start out
with OO features, those were added later when it was all the rage. When
working in an elegant functional language like Lisp I can see why one
would never have to consider OO.

That alone should indicate that many technical comparisons between
languages can be easily skewed towards a language by using examples that
heavily favor built-in abilities of the language one chooses to boast
about.

In the end, I'm left with the belief that different languages have
different applications. Claiming one language is the be-all, and is
**always** better for any task is about as false as claiming that a
language has no problems or issues.

Within certain realms it does make sense to compare languages, scripting
vs scripting, functional vs functional, etc. But leaping to a comparison
of functional/dynamic-typed vs non-functional/static-typed is typically
going to result in some strange claims.

Anyways, if you feel like commenting, try and come up with an example of
where Language X (that you use) has a very succinct solution compared to
Language Z (all the others). It'd be great to compare some examples and
see areas in which different languages fall flat on their face when it
comes to `succinctness <http://www.paulgraham.com/power.html>`_. (Ie, in
most dynamic languages, you'd have to add several lines of code to
ensure variables are the type you want. A feature/annoyance of
static-typed languages)

**Update**: An anonymous user kindly informs me that there's no
foundation for my claim that some languages are better in certain realms
than others, unfortunately the anonymous user fails to say why.

Ruby has no keyword arguments currently (`Ruby 2 will have them and
keyword
collectors <http://www.rubyist.net/~matz/slides/rc2003/mgp00026.html>`_
``**`` as Python does). To even approximate my Python example in Ruby,
you'd first need to declare the argument as optional which has the side
effect of packaging it into an ``Array``. Wheras in Python ``**kargs``
packages up the rest of the key/vals under a dictionary. If someone
would like to write out the full translation in Ruby, I'd be happy to
put it up here, but I doubt its going to be pretty (until Ruby 2).

Zach was helpful and provided an example showing that the specific task
I cited is fairly short in Lisp as well, looking like this:

::

    (defun somefunc (&rest kwargs
                     &key (keyone "default") (keytwo "anotherdefault")
                     &allow-other-keys)
                     ; ...
                     )

I would like to make it very clear that my point is **not that Python is
better**, but that **technical comparisons can be warped to favor
certain languages**. This is the same point Paul Prescod makes, and what
I'd actually like to see is more technical comparisons that make this
point obvious.


.. author:: default
.. categories:: Python, Thoughts, Code
.. comments::
   :url: http://be.groovie.org/post/296352439/language-specific-comparisons
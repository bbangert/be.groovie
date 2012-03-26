Is Rails a DSL? What is a DSL, and is it possible in Python?
============================================================

I keep seeing blogs and blog comments pop up with some very odd notions.
Many of these are summed up in this comment from a `recent post by Tim
on Ruby
books <http://radar.oreilly.com/archives/2005/12/ruby_book_sales_surpass_python.html>`_

“It's doubtful that the Python folks can come up with anything as
compelling (or elegant) as Rails. Why? Because Ruby is so good at
creating Domain Specific Langauges (DSLs). Ruby's anonymous code blocks
are a big part of what enables DSLs to be written so easily in the
language. Python doesn't have them. Python's lambda's (and closures in
general) are crippled as well, which also doesn't help Python's cause.”

What is a Domain Specific Language (DSL)?
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

I always like to carefully define my terms before actually talking about
them. So first I looked up several common definitions of a DSL. We have
Martin Fowler's `entry on a
DSL <http://www.martinfowler.com/bliki/DomainSpecificLanguage.html>`_
which describes it as:

“The basic idea of a domain specific language (DSL) is a computer
language that's targeted to a particular kind of problem, rather than a
general purpose language that's aimed at any kind of software problem.”

He further clarifies between two types of DSL:

“The most common unix-style approach is to define a language syntax and
then either use code generation to a general purpose language, or write
an interpreter for the DSL. Unix has many tools that make this easier. I
use the term **External DSL** to refer to this kind of DSL.”

“The lisp and smalltalk communities also have a strong tradition of
DSLs, but they tend to do it another way. Rather than define a new
language, they morph the general purpose language into the DSL. (Paul
Graham describes this well in `Programming
Bottom-Up <http://www.paulgraham.com/progbot.html>`_.) This **Internal
DSL** (also referred to as an embedded DSL) uses the constructs of the
programming language itself to define to DSL.”

To summarize, an Internal DSL satisfies one of the following:

-  Uses a general purpose language, then morphs it into a language to
   fit the domain
-  Adds functionality to a general purpose language such that solving a
   specific domains problem is easier

An External DSL:

-  Completely new language syntax
-  Typically requires code generation or interpreter for DSL

Martin Fowler `espouses on how very dynamic languages like Lisp,
Smalltalk, and Ruby are more conducive to internal
DSLs <http://www.martinfowler.com/articles/languageWorkbench.html#InternalDsl>`_
as the meta programming capabilities and dynamic nature make it easy to
extend and customize the functionality for your domain. I completely
agree with his contention that an Internal DSL is limited by the syntax
and structure of the language.

DSL's in Python and Ruby
^^^^^^^^^^^^^^^^^^^^^^^^

While the anonymous code blocks in Ruby are useful and syntactically
nice, similar functionality can be done in Python through the use of
generators and iterators (more powerful generator functionality similar
to Ruby's anonymous blocks are planned for Python 2.5).

Ruby also lets you extend built-in types, which is utilized by Rails to
add a few helper functions to core Ruby data types. Python and Ruby both
have closures that operate slightly differently, Ruby's closure is
definitely more “full featured”. However this typically isn't a problem
because of list comprehension's, generator expressions, and
generators/iterators.

Zope is a very clear example that its quite possible to build an
internal DSL in Python. Whether they built it in a clear, easy to use
way is up for someone else to debate. SQLObject makes dealing with
databases as easy as ActiveRecord, and there's many other examples of
internal DSL's built in Python (Take a look at
`twill <http://www.idyll.org/~t/www-tools/twill.html>`_, a web
application testing language implemented in Python).

Is Rails a DSL?
^^^^^^^^^^^^^^^

First, it should be obvious that if Rails is a DSL, its an Internal DSL.
The most noticeable strides towards being a web programming DSL in
Rails:

-  Over a dozen core Ruby classes are extended/modified
-  Dozens of helper functions
-  New classes (syntactic sugar) defining database access and web
   paradigms

Given how loose the definition of internal DSL is, I think its clear
that Rails qualifies, so does Django, TurboGears, Aquarium, etc.

If you prefer to be more strict about an internet DSL, and argue that a
lay programmer needs to be able to do a reasonable amount of ‘work'
without knowing the base language implementing it, Rails starts to move
apart. You can do a reasonably large amount of work in Rails without
knowing Ruby. A lot can also be done in Zope without knowing Python.

In either case, you can't really start to make advanced applications in
any of the frameworks without knowing the general purpose language its
built on. DSL's can and have been built in Python, and I believe if you
go out and start counting them up, you'll see more DSL's implemented in
Python than in Ruby.

Anyways, hopefully for people that run around re-iterating something
they heard somewhere about DSL's and Python vs. Ruby, this clarified
something. It's easy to create DSL's in Python, lots of people do, and
there's lots of them. Python and Ruby are both great for making them,
outside of Rails I don't know any other DSL's in Ruby. Perhaps someone
can compile a list of all the internal DSL's written in both Ruby and
Python?


.. author:: default
.. categories:: Python, Rails, Rants, Ruby, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296349003/is-rails-a-dsl-what-is-a-dsl-and-is-it-possible-in
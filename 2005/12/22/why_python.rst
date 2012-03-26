Why Python?
===========

I first heard about Python from a roommate about 5 or 6 years ago. He
was putting together a presentation for some Bio-informatics people, and
was going to go over the basics of Python programming as its very
popular in the scientific community. I didn't give it much though as I
was mainly using Perl at the time for any programming work, and the
white space was of course somewhat of a put-off.

Fast forward a few years… I had been programming rather heavily in Perl
at the time, and despite having used Perl literally for years, I still
felt like I hadn't achieved “mastery”. The effects of code in Perl would
jump out and surprise me every few days, and sometimes hunting down
weird bugs due to ambiguous syntax was rather time consuming. In short,
Perl just wasn't fun anymore.

I started looking around for other languages, and took a look at Ruby.
Back then, Ruby had the same things that were annoying me about Perl.
Implicit variables that seemingly came out of nowhere (@\_, $\_, etc),
inconsistencies, and since the community was so small it lacked the
vibrant and active development Perl had. Ruby also was missing so many
of the CPAN modules I had come to rely on. Then browsing through some of
Eric Raymond's writings, I came across an `article about Python he
wrote <http://www.linuxjournal.com/article/3882>`_ titled the same as
this blog entry.

White space and Mastery
^^^^^^^^^^^^^^^^^^^^^^^

My white space fears were removed rather quickly.

::

    Of course, this brought me face to face once again with Python's pons asinorum, the
    significance of whitespace. This time, however, I charged ahead and roughed out some
    code for a handful of sample GUI elements. Oddly enough, Python's use of whitespace
    stopped feeling unnatural after about twenty minutes. I just indented code, pretty
    much as I would have done in a C program anyway, and it worked.

But this wasn't what truly piqued my interest. As I mentioned, the
feeling that Perl was somehow beyond mastery. To me, mastery means that
I can write massive chunks of code with confidence it'll act exactly as
I intended it to. So seeing Raymonds next few paragraphs really got me
going.

::

    That was my first surprise. My second came a couple of hours into the project, when I 
    noticed (allowing for pauses needed to look up new features in Programming Python) I 
    was generating working code nearly as fast as I could type. When I realized this, I 
    was quite startled. An important measure of effort in coding is the frequency with 
    which you write something that doesn't actually match your mental representation of 
    the problem, and have to backtrack on realizing that what you just typed won't 
    actually tell the language to do what you're thinking. An important measure of good 
    language design is how rapidly the percentage of missteps of this kind falls as you 
    gain experience with the language.

This is all summed up very nicely,

::

    I wrote a working, usable fetchmailconf, with GUI, in six working days, of which 
    perhaps the equivalent of two days were spent learning Python itself. This reflects 
    another useful property of the language: it is compact--you can hold its entire 
    feature set (and at least a concept index of its libraries) in your head. C is a 
    famously compact language. Perl is notoriously not; one of the things the notion 
    ``There's more than one way to do it!'' costs Perl is the possibility of compactness.

Being **compact** is a valuable asset for Python. Not only does it make
writing large blocks of code without error possible, but it also means
the code is going to be easy to read. After opening up a few other
Python projects and scanning through the code, I was hooked and
proceeded to buy the Learning Python book (Though the online tutorials
would've been just fine as well).

Black Magic isn't so Black
^^^^^^^^^^^^^^^^^^^^^^^^^^

Since then, I've been using Python close to non-stop for just a little
over a year. In just the first week of using Python, I felt more
productive and wrote code I was positive would work (just as ESR said)
on the first try. A few months ago, interested in learning even deeper
“black magic” of Python, I went to a presentation by Alex Martelli on
Python's Black Magic, Meta-classes and Descriptors.

The most fascinating thing was that meta-classes got their behavior from
simple concepts I already knew. It was hard to believe things were so
easy. Eric Raymond also noticed this:

::

    It's remarkable enough when implementations of simple techniques work exactly as 
    expected the first time; but my first metaclass hack in a new language, six days from 
    a cold standing start? Even if we stipulate that I am a fairly talented hacker, this 
    is an amazing testament to Python's clarity and elegance of design.

Fields of Use
^^^^^^^^^^^^^

I have now written quite a few projects in Python, and on several of the
open-source ones heard, “I just wanted to add Feature X to this, and I
was actually able to figure it out just look at the code. I don't even
know Python!”

These projects span fields: shell scripts, network daemons, web
applications, computing, GUI's, and more. Learning Python is useful for
many fields, and I know people learning Python right now so they can
tackle problems in different fields with a compact language thats easy
to master.

The Choir
^^^^^^^^^

I realize that this entry, carried by Planet Python, is mostly preaching
to the choir. However, I felt something like this was needed. Partly
because some members of the Python community have gotten odd impressions
about what we should try and do in Python and what we should just “give
up” on, having lost some sort of war (bizarre, I know).

People come to Python for a variety of reasons, they stay for a variety
of reasons. Having compelling tools to make tasks easy in many fields is
great, and means there's no need to learn new languages solely to try
and make a task in one field slightly easier (Though its always healthy
to learn more).

It's definitely valuable knowledge to know **why** a task in one field
is easy using Language X, and for that alone its good to give it a spin.
Learn what was done right, and what was done wrong. In the end though,
if that language isn't a compact language like Python, I'm just not
going to enjoy it as much.

I didn't start learning Python because of Application/Framework Y, I
learned it because Python is exceptionally compelling by itself. Others
learn it for the same reason, and despite the bizarre claim that book
sales is equivalent to language usage/popularity, it should be obvious
by now that a book isn't needed to master Python.

For those demoralized because some other language is getting attention
due to a field its had a huge impact on, re-evaluate your feelings. This
isn't the first time its happened, and it won't be the last. Google uses
Python, ILM uses Python, thousands (yes, thousands) of major
corporations use Python.

Python doesn't need to be master of every field, it just needs something
compelling enough that you're as productive using it as you would be
using a different tool in a language that isn't so compact.


.. author:: default
.. categories:: Python, Thoughts
.. comments::
   :url: http://be.groovie.org/post/296346660/why-python
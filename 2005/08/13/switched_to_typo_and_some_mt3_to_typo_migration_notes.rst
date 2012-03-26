Switched to Typo and some MT3 to Typo Migration Notes
=====================================================

So tonight I took the plunge, and converted the blog to
`Typo <http://typo.leetsoft.com/>`_. It's totally slick, and I'm digging
it. Plus when I want to tweak stuff, I don't have to mess around with
Perl.

It's currently lacking a feature I had grown accustomed to, Technorati
auto-pinging. I'm thinking this would be a good thing to contribute, so
I'll start digging into the code and see what needs to be updated.

Migration was also a bit of a hassle, as it appears the MovableType 3
migration script only is happy if you use MySQL for your old and new
blog. Getting it migrated to Typo required dumping the MovableType
database using pg\_dump, and loading it into the Typo database. Then the
mt3.rb script needed to be edited to remove all the table prefixes.
After this, the script happily imported all my prior posts, comments,
and trackbacks.


.. author:: default
.. categories:: Code, Ruby, Rails
.. comments::
   :url: http://be.groovie.org/post/296352519/switched-to-typo-and-some-mt3-to-typo-migration-notes
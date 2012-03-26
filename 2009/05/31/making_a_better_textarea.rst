Making a better TextArea
========================

I've been working on some Javascript to enhance the TextArea elements on
the `PylonsHQ Snippets <http://pylonshq.com/snippets>`_ section, and
have noticed that… well, TextArea's suck.

The hack I've seen is to use one of the newer features of browsers, the
editable or ‘design' attribute's for div elements I believe. This lets
one build a very snazzy amount of features, such as syntax highlighting,
code completion, etc., but I don't think I needed to go that far.

I only have one main design goal, this TextArea is for the user to enter
RestructuredText so it'd be awesome if the TextArea acted in a way that
made rst a bit nicer. The obvious two things that came to mind:

#. Tab key indents 4-spaces
#. Hitting return on an indented line, will retain the indentation on
   the next line

I've actually gotten some Javascript, hobbled together from various
parts of the net, along with an ‘enter' key handler I wrote myself `on
bitbucket <http://bitbucket.org/bbangert/kai/src/d5b9875a9e64/kai/public/javascripts/rst_helpers.js>`_.

Course, it'd also be nice to have a button or key combo, that will
indent/unindent a selection in the TextArea as well.

Anyone else have any Javascript they've hobbled together in the past to
make TextArea a little nicer for restructured text?


.. author:: default
.. categories:: Python, Thoughts, Code
.. comments::
   :url: http://be.groovie.org/post/296328815/making-a-better-textarea
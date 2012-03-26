Routes 1.0 Released
===================

I've finally finished the documentation for
`Routes <http://routes.groovie.org/>`_ and as I `mentioned earlier
regarded
releases <http://groovie.org/articles/2005/10/20/routes-1-0-almost-ready>`_
am now ready for a 1.0 release. If you're curious about Routes and want
to get up to speed, I'd suggest jumping straight to the `Routes
Manual <http://routes.groovie.org/manual.html>`_.

Routes is currently used in `Myghty <http://www.myghty.org/>`_ with the
routes Paste template, and has been integrated for use both in
`Aquarium <http://aquarium.sourceforge.net/>`_ as well as
`CherryPy <http://www.cherrypy.org/>`_ (though CherryPy 2.2 should allow
better integration).

Now that Routes is feature-equivilant to the Rails version, its time to
start planning for new stuff. The first and most obvious is to allow for
more advanced configurability of URL's by allowing for a new separator.
This would allow you to get as creative as you like with URL's, so you
could do something like this:

::

    m.connect('archives/:(article)-:(page).html', controller='blog', action='view')
    m.connect('feeds/:section/:(format).xml', controller='feeds', 
              action='xml', format='atom')

This should make for a nice 1.1 feature. For those familiar with the
Rails system of Routes, has there been anything you've found lacking or
were just itching for?


.. author:: default
.. categories:: Python, Code, Routes
.. comments::
   :url: http://be.groovie.org/post/296349115/routes-1-0-released
How to Use Database Agnostic SQL in SQLObject
=============================================

One of the advantages to using `SQLObject <http://sqlobject.org/>`_ is
that the code you write in it can easily be constructed in a way that
ensures it'll work without a problem in all the databases SQLObject
supports. This is a tremendous advantage that is most useful when
writing web applications intended for wide-spread deployment on a
variety of systems.

The most common SQL expressions you'll likely want to use are Update,
Select, and Delete. You can directly issue all of these in SQLObject
using the connections sqlrepr method. The easiest way to see this is to
play with it on the interactive prompt.

Before we begin, let's setup a simple database layout using sqlite to
try out the examples with:

::

    from sqlobject import *from sqlobject.sqlbuilder import *from datetime import datetimeimport sys, os

        db_filename = os.path.abspath('data.db')if os.path.exists(db_filename):
        os.unlink(db_filename)connection = connectionForURI('sqlite:' + db_filename)sqlhub.processConnection = connection

        class Comments(SQLObject):
        name = StringCol(length=50)
        date = DateTimeCol(default=datetime.now)
        comment = StringCol()

        Comments.createTable()

        Create some boring comments
        Comments(name='fred', comment='Hello everyone')Comments(name='joe', comment='Hi fred')Comments(name='smith', comment='Good day')

SQLObject supplies a batch of classes for us that generate our database
agnostic SQL expressions. While there isn't too much documentation for
using these classes (the mailing lists help), you can get a good idea
where to start by looking at the help for them.

Using Select
^^^^^^^^^^^^

If we want to take a look at the documentation for the Select class
(which was imported above from sqlobject.sqlbuilder), we'll get the
following information:

::

    Help on class Select in module sqlobject.sqlbuilder:

        class Select(SQLExpression)
     |  Methods defined here:
     |  
     |  init(self, items, where=, groupBy=, having=, orderBy=, limit=)
     |  
     |  sqlrepr(self, db)

First, we need to pull the connection used for the class. We will then
use the connections ``sqlrepr`` method to construct our SQL, and the
connections ``query`` method to actually run it. Let's take a look at
getting all the names only from our Comments:

::

    conn = Comments._connectionnameselect = conn.sqlrepr(Select(Comments.q.name))results = conn.queryAll(nameselect)

         >>> results
            [('fred',), ('joe',), ('smith',)]
        

This will populate results with an array of tuples, one tuple for each
result with the tuple values in the order you specified for the select
(it'd be nice to have a way to get dicts instead…). Let's take a look at
a few more examples of using Select:

::

    fields = [Comments.q.name, Comments.q.date]namedateselect = conn.sqlrepr(Select(fields, where=(Comments.q.date results = conn.queryAll(namedateselect)

        >>> results
            [('fred', ), 
            ('joe', ), 
            ('smith', )]
        namedateselect = conn.sqlrepr(Select(fields, where=(Comments.q.date results = conn.queryAll(namedateselect)

        >>> results
            [('fred', ), 
            ('smith', )]
        

Joins, and additional fields can be specified using the normal Class.q
notation to let SQLObject generate the proper SQL necessary in the same
manner as the documentation explains.

Updating Fields
^^^^^^^^^^^^^^^

Doing a large update of a sub-set of fields is definitely something best
left to a manual Update command. First, let's take a look at what the
help for the Update indicates:

::

    Help on class Update in module sqlobject.sqlbuilder:

        class Update(SQLExpression)
     |  Methods defined here:
     |  
     |  init(self, table, values, template=, where=)
     |  
     |  sqlrepr(self, db)

I'll admit right now I'm not actually sure what template is for, nor
have I used that keyword argument. If someone would like to chime in on
the comments, that'd be appreciated greatly.

Updating the table gets a little tricky since we need to specify all of
the fields in a database agnostic manner. To avoid very long statements,
I've broken it down into sections to build the query.

Let's look at updating all the dates of our Comments table:

::

    datecol = Comments.q.date.fieldNameupdatedates = conn.sqlrepr(Update(Comments.q, {datecol:datetime.now()}))conn.debug = True    # So we can see the query executeconn.query(updatedates)conn.cache.clear()

        >>> conn.query(updatedates)
             1/Query   :  UPDATE comments SET date='2005-11-01 11:57:31'
             1/QueryR  :  UPDATE comments SET date='2005-11-01 11:57:31'
             1/COMMIT  :  auto
        

Updating multiple fields is just as easy, merely add more key/val's to
the dict you pass in for the values variable. To update values using the
original value of the field in the update, ie, adding something to the
existing field we specify that using the Class.q.field format used in
where clauses. Also, note that we need to clear the object cache after
running the update so that SQLObject fetches the row again before using
it.

::

    updatedates = conn.sqlrepr(Update(Comments.q, {datecol:Comments.q.date + 20}))conn.query(updatedates)conn.cache.clear()

         >>> conn.query(updatedates)
             1/Query   :  UPDATE comments SET date=(comments.date + 20)
             1/QueryR  :  UPDATE comments SET date=(comments.date + 20)
             1/COMMIT  :  auto
        

This adds 20 seconds to the existing dates for all the rows. Using the
.q notation with the class is necessary for the key value because we
need to ensures that Python doesn't try to add 20 to a string which is
what it would've tried if we had said ``{datecol:'date' + 20}``.

Deleting
^^^^^^^^

Issuing a Delete on the database is very similar to the update command,
the class help looks like this:

::

    class Delete(SQLExpression)
     |  To be safe, this will signal an error if there is no where clause,
     |  unless you pass in where=None to the constructor.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, table, where=<class sqlobject.sqlbuilder.NoDefault>)

By now, the signature for the init method should be fairly familiar as
well as what input's its expecting. Here's a quick example:

::

    delquery = conn.sqlrepr(Delete(Comments.q, where=(Comments.q.name == 'smith')))conn.query(delquery)

         >>> conn.query(delquery) 
             2/Query   :  DELETE FROM comments WHERE (comments.name = 'smith')
             2/QueryR  :  DELETE FROM comments WHERE (comments.name = 'smith')
             2/COMMIT  :  auto
        

That's pretty much all there is to deleting, probably the easiest
operation to do with a SQLExpression class.

Transactions, Notes, and Gotchas
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

When using these techniques in large programs, it can be tricky to
ensure that the object cache is cleared out and up to date. If you're
going to use a lot of these commands extensively it might be prudent to
turn cacheValues off, or wrap the commands in a function that calls the
cache.clear() command.

Using transactions (not all databases support it) can still be done if
you want to wrap a batch of these manual expressions into a single
transaction. You just need to start the transaction and commit it when
done:

::

    trans = conn.transaction()
    delquery = conn.sqlrepr(Delete(Comments.q, where=(Comments.q.name == 'smith')))
    conn.query(delquery)
    updatedates = conn.sqlrepr(Update(Comments.q, {datecol:Comments.q.date + 20}))
    conn.query(updatedates)
    trans.commit()

If you'd like to use database functions (bottom of `the SQLBuilder
docs <http://sqlobject.org/SQLBuilder.html>`_), this is easy to pass in
as well but since they're more database specific you begin to lose
portability.

Please feel free to contribute any experiences or further examples of
working with SQLObject expressions in a manual fashion as I've described
here.


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296349259/how-to-use-database-agnostic-sql-in-sqlobject
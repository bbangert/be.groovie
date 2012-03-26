Handling Form data with Formencode + SQLObject
==============================================

Two of my favorite and most often-used Python packges are
`formencode <http://formencode.org/>`_ and
`sqlobject <http://sqlobject.org/>`_. Using these packages together is
done fairly often, but I've rarely seen any documentation describing a
full form display, validation, and insert into a database of new data
from said form.

In this example, I've tried to wean down the code as much as possible to
get a very concise snippet (only 12 lines of web page Controller code)
that will:

#. Display a new form to the user
#. Handle form submission
#. Validate the form
#. Coerce form values into the proper types for the database
#. Insert the form data to the database, or
#. Display the form with error messages, and maintain their values

The nice thing about using formencode, is that 3 of the 6 steps I listed
above are handled by it in a fairly automatic way. Formencode will check
the data given a form schema, coerce the values into the Python types
you ask for, fill in errors should they occur, and maintain the existing
values.

I'll be using `Myghty <http://www.myghty.org/>`_ for this, but since all
I'm really pulling from it is the request args, it should be pretty
obvious what to change for whatever web framework makes you happy.

formencode
^^^^^^^^^^

First, lets take a look at our basic form:

::

    # myform.myt
    <html>
    <head><title>basic form</title></head>
    <body>
    <form action="/mypage" method="post">
    Username: <input type="text" name="username" size="26" />
                <form:error name="username">
    Age: <input type="text" name="age" size="3" />
                <form:error name="age">
    <input type="submit" value="Send it" />
    </form></body></html>

To validate this, we'll setup a formencode form schema to run this
through. I should note at this point, that the formencode web
documentation kind of sucks. However, the doc strings are plentiful, and
extremely useful for figuring out which validator to use in addition to
having examples of each. To keep things organized, I usually place
related form schema classes under the same module and import it as
needed.

The other thing you might notice about the form, is that it has
``form:error`` fields. These are used by the formencode parser to put in
the error message that the validation triggers. This lets us put the
error messages right under the boxes they occured in. The drawback is
that we have to process the form before first displaying it to strip out
the ``form:error`` fields.

Here's our simple schema to validate the above form:

::

    from formencode import schema, validatorsclass UserInfoSchema(schema.Schema):
        allow_extra_fields = True
        filter_extra_fields = True

        username = validators.String(not_empty = True, max = 50)
        age = validators.Int(not_empty = True)

Hopefully the above should look pretty obvious. The
``allow_extra_fields`` bit is needed so that we can pass the entire
request argument dict into formencode without it tripping up if there's
“extra” keys it didn't expect (like the submit button). Since we're
going to be passing the dict we get back from formencode directly to
sqlobject, we include ``filter_extra_fields`` to remove anything that
our sqlobject isn't going to like.

The form schema needs to include all the fields the database is going to
take, since we're stripping off anything it doesn't mention. The Int
validator not only ensures that the value is an int, but will change it
into a Python integer in the process.

sqlobject
^^^^^^^^^

Now that we've handled validation and value coercion, lets have a look
at the sqlobject class. I'm going to “cheat”, and assume your database
for this was created like so (in
`Postgresql <http://www.postgresql.org/>`_):

::

    create table user_info (
        id serial primary key,
        username varchar(50),
        age int(2)
    );

Since I'm feeling lazy, we'll rely on SQLObject to pull the table info
from the database giving us a SQLObject class like so:

::

    from sqlobject import *
    class UserInfo(SQLObject):
        class sqlmeta:
            fromDatabase = True
    </pre>

        Personally, I think if you just leave the whole thing empty and put pass in for the body, it should assume you want it populated from the database…. but the above will do the trick. Please note I'm using the sqlmeta class to define this, which is used in the recent svn builds of sqlobject. If you use the release on the site, you could replace those two lines with _fromDatabase = True instead.

        Putting It All Together

        Now that our form, validation, and sqlobject schema is all done its time for the meat of the matter… the web page controller. Getting this function called will vary depending on your web framework, so I'll just assume you can figure out how to get it called, here's what it looks like in Myghty using implicit module components:from formencode import htmlformfrom ourschema import UserInfoSchemafrom oursqlstuff import UserInfo

        def mypage(m):
        html = m.scomp('/myform.myt')   # load the form into a string
        form = htmlform.HTMLForm(html, UserInfoSchema())
        if m.request_args:
            form_result, errors = form.validate(m.request_args)
            if errors:
                errorForm = form.render(m.request_args, errors)
                m.write(errorForm)
            else:
                UserInfo(**form_result)  # database insert
                m.subexec('/thankyou.myt')
        else:
            m.write(form.render())

        

And there you have it. In a brief 12 lines, we handle displaying a new
form to a user, and handle form submission, validation, and database
insertion while ensuring that the string values are coerced as needed
before database insertion. This task is done quite often in web sites,
so making this task as painless as possible is a real time saver.

Hopefully this will help out anyone out there, who was wondering about
quicker and easier ways to handle cases like this. If you have any
thoughts/suggestions on how to streamline this further, be sure to leave
a comment.


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296352278/handling-form-data-with-formencode-sqlobject
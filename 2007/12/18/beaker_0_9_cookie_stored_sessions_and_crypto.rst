Beaker 0.9, cookie-stored sessions, and crypto
==============================================

In the latest 0.9 release of `Beaker <http://beaker.groovie.org/>`_,
I've finally added `cookie-side session
storage <http://wiki.pylonshq.com/display/beaker/Cookie-Only+Sessions>`_.
I was a little bit moved to finally do this by seeing that Rails 2.0 had
added cookie-side session storage, and heck if I was going to miss out!

A few changes from how Rails 2 did it though, I was definitely not
content to store all the data in an end-user visible form in the cookie.
That only left encryption as the next logical choice, and that quickly
led me down a path of quite a bit of cryptography research.

The world of cryptography is a constantly evolving and rapidly
progressing field. New papers are coming out all the time with new
research on ways to break, or ‘wound' a particular encryption scheme.
Providing a weak form of encryption in Beaker would be worse then not
having it at all, since it'd lead someone to falsely believe the session
data was secure.

After initially going with an RC4 cipher implementation, I got ahold of
some crypto people that are actually in the field, and the unanimous
opinion was to use AES encryption in Counter Mode, also referred to as
AES-CTR along with a signature to prevent tampering (you'd be amazed
what you can do to encrypted data, and it'd still technically decrypt).
This led to a slight increase in requirements unfortunately, as pure
Python based AES encryption is a bit slow. This means that using
cookie-based sessions in Beaker requires the installation of PyCrypto,
which includes a C extension (making cookie-based sessions faster than
file-based, memcached, and db-based sessions).

The final solution in Beaker uses 256-bit AES-CTR with a 256-bit HMAC
for authentication purposes. It's **fast, secure, and scales** across a
cluster without a problem. It's not for everyone of course, cookies are
rather severely limited in size, so if you're just storing a few small
tidbits of information in a session, for example:

-  a user id
-  some flags about the users status (logged in, etc)
-  a flash message

Then cookie-stored sessions might be perfect for you.

**Update**: Forgot to mention, in the future, Beaker will probably use
pycryptopp instead of PyCrypto since the PyCrypto library's AES-CTR
implementation isn't as efficient as it could be, and will be using
VMAC's instead of HMAC's for even more speed. Plus, apparently Andrew
Kuchling isn't maintaining PyCrypto, as there's quite a few patches for
it sitting unanswered on the sourceforge and launchpad bug trackers.


.. author:: default
.. categories:: Code, Python
.. comments::
   :url: http://be.groovie.org/post/296343680/beaker-0-9-cookie-stored-sessions-and-crypto
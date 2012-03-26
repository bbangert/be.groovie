Sending RSS items to Growl via AppleScript / NetNewsWire
========================================================

A friend alerted me the other day to some useful sites for tracking
packages via RSS. There's one for
`FedEx <http://www.benhammersley.com/tools/fedex_package_tracking_in_rss.html>`_
and one for
`UPS <http://www.young-technologies.com/Utilities/PackageTracking/>`_.

While these are quite cool, and nice to have in NetNewsWire, the same
friend told me its even cooler to have updates to the feeds sent to
`Growl <http://growl.info/>`_. That way you get a nice little pop-up
window when one of your packages has moved on.

He wrote a `Python script that sent RSS updates over the LAN to
Growl </files/growlrss.py>`_ (Note: The Python script requires
`netgrowl.py <http://the.taoofmac.com/space/Projects/netgrowl.py>`_).
While that was cool, his method of adding feeds to watch (editing a text
file on a remote machine) didn't seem that cool. It was about that time
that I started thinking, well, why not have Net News Wire manage the
feeds? That is what its for after all… so I started looking to see how I
could tie this togther.

Searching through ranchero.com quickly led me to a `page on calling
scripts as
subscriptions <http://ranchero.com/netnewswire/features/scriptSubscriptions.php>`_.
So I figure, if I write an AppleScript, that searches a NetNewsWire
(NNW) folder for unread items then `sends them to Growl via the
Applescript
interface <http://growl.info/documentation/applescript-support.php>`_,
that should do the trick.

So without further ado, here's my little Applescript, based on Brent
Simmons Folder Watch example, that searches a NNW folder for unread
items, sends them to Growl, then marks them as read.

Installing
^^^^^^^^^^

`GrowlRSS.scpt: <http://www.groovie.org/files/GrowlRSS.scpt>`_

Download this where desired, add it as a script in NNW using the File
menu -> New Special Subscription -> Script. Then locate the GrowlRSS
script, it will then open the Show Info window. Expand the Script
Settings option, and put the name of the NNW folder to watch as the
Args. Close, and hit refresh, and it should send any unread items in
that folder to Growl.

Caveat
^^^^^^

You should have `Growl 0.6 from
svn <http://growl.info/documentation/growl-source-install.php>`_
installed. It's possible it'll work with 0.5, but I haven't tested that.


.. author:: default
.. categories:: AppleScript, Code
.. comments::
   :url: http://be.groovie.org/post/296355018/sending-rss-items-to-growl-via-applescript
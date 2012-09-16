Building A SmartOS Server
=========================

I've been reading about SmartOS_ for awhile now and have wanted to
build a home server that would let me run VM's with ZFS_ for the main
file-system. Getting rid of my home theater PC and wireless router
(which has been annoying me with its flakiness for months) was also a
goal. Running something like pfsense_ in a VM would give me more
options and theoretically be more stable than the fairly crappy
software that seems to plague home consumer-grade wireless routers.

So after a month or so of research in my spare time, it seemed like
SmartOS_ was going to be the best bet. Even though its generally
intended for use in the datacenter, it had all the features I wanted
(which I'll blog about separately in my next post). Now I just needed a
parts list that had already been verified to work with SmartOS_, which
is a bit pickier on hardware than the linux/BSD distributions.

Equipment
---------

Here's what I ended up with:

- **CPU**: Intel Xeon E3-1230 V2
- **Motherboard**: SUPERMICRO MBD-X9SCL-F-O
- **Case**: NORCO RPC-2212 Black 2U Rackmount Server Case with 12 Hot-Swappable
  SATA/SAS Drive Bays
- **HBA**: LSI Internal SATA/SAS 9211-8i (Hooks up to 2 of the back-plane
  connectors in the case for 8 drives)
- **RAM**: 16GB ECC (The 8 GB unbuffered sticks were unfortunately not around
  at the time or I would've gotten two of those to begin with)

I already had a 2TB and 3TB drive, so I bought one more of each so that I
could run a ZFS storage pool with 2 vdev mirrors as `Constantin Gonzalez
blogs about regarding RAID vs. mirrors <http://constantin.glez.de/blog/2010/01/home-server-raid-greed-and-why-mirroring-still-best>`_.

In retrospect, and after reading a bit more, I think I would've gotten one of
the larger Norco 4U cases. Not because I need or want 20+ hot-swap bays, but
because you can easily use a 'desktop' grade 80+ Titanium rated power supply.
Finding a 2U 80+ PSU is difficult, a 80+ Titanium rated that puts all its power
out on a single 5v rail is almost impossible. The cost savings in getting a
good desktop-grade PSU with the Norco 4U case is about the same as the one I
got with the more expensive 2U PSU.

I also bought a rack to put the server in along with my other home
networking gear, so that it'd all be nicely packed away in a corner of
the garage. Here's a photo of the completed setup:

.. image:: /_static/garage_server.jpg
    :align: center
    :alt: My home-server rack

I have one of the cheaper Cisco SG300-10 switches which conveniently
came with rack-mounts, and monoprice had a very affordable patch panel
and blank plates to make it look tidy.

Overall cost: **~$2200**

That includes the nice `Tripp Lite SR12UB 12U Rack Enclosure <http://www.amazon.com/Tripp-Lite-Enclosure-Cabinet-33-Inch/dp/B0043WF9E8/ref=pd_cp_e_1>`_ which I've found
handy to lock to ensure my toddler doesn't yank out hard drives (he figured out
how to pull out the hot-swap drive in all of 20 seconds when I was assembling
it). Not that I let him run around the garage, but keeping everything locked
is handy just in case.

OS Choice
---------

When I was assembling and preparing to install SmartOS_, some people on IRC
mentioned that OpenIndiana_ might be a better choice for a home server. Suffice
it to say it didn't work out well, while SmartOS_ has been flawless now and
running smoothly for the past two months.

My next post will have a lot more details on my OpenIndiana_ experience as well
as how I have the SmartOS_ box setup.


.. _OpenIndiana: http://openindiana.org/
.. _pfsense: http://www.pfsense.org/
.. _SmartOS: http://smartos.org/
.. _ZFS: http://en.wikipedia.org/wiki/ZFS

.. author:: default
.. categories:: SmartOS
.. comments::

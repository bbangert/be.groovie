Trying out SmartOS and OpenIndiana
==================================

After :ref:`building my new server <building_smartos_server>` capable
of running SmartOS_, it was time to give it a spin!

If you've only built desktop machines, its hard to express how awesome
IPMI KVM is. No longer do you need to grab another keyboard / video
monitor / mouse (the KVM), you just plug in the IPMI Ethernet port on
the motherboard to your switch and hit the web-server its running. It
then lets you remotely access the machine as if you had it hooked up
directly. You can get into the BIOS, boot from ISO's on your local
machine, hard reset, power down, power up, etc. It's very slick and
means I can stick the computer in the rack without needing to go near
it to do everything that used to require a portable set of additional
physical hardware.

.. note::

    This post assumes some basic knowledge of OS virtualization. In
    this case `QEMU <http://wiki.qemu.org/Main_Page>`_, KVM_ (which was
    ported by Joyent to run on SmartOS_), and `Zones
    <http://en.wikipedia.org/wiki/Solaris_Containers>`_. I generally
    refer to them as VM's and will differentiate when I add a Zone_ vs.
    a KVM_ instance.

First Go at SmartOS
-------------------

**Installation is ridiculously easy, there is none**. You download
SmartOS_, put it on a USB stick or CD-ROM, and boot the computer from
it. I was feeling especially lazy and used the motherboards IPMI KVM
interface to remotely mount the ISO image directly from my Mac.

Once SmartOS_ booted, it asked me to setup the main ZFS_ pool, and it
was done. SmartOS_ runs a lot like a VMWare ESXI hyper-visor, with the
assumption that the machine will only be booting VM's. So the entire
ZFS_ pool is just for your VM's, which I appreciate greatly. After
playing with it a little bit, it almost felt.... too easy.

I had really allocated at least a week or two of my spare time to
fiddle around with the OS before I wanted it to *just work*, and having
it running so quickly was almost disappointing.

The only bit that was slightly annoying was that retaining settings in
the GZ (Global Zone) is kind of a pain. You have to drop in a service
file (which is XML, joy!) on a path which SmartOS_ will then load and
run on startup. This was mildly annoying, and some folks on the IRC
channel suggested I give OpenIndiana_ a spin, which is aimed more at a
home server / desktop scenario. There was also a suggestion that I give
`Sophos UTM`_ a spin instead of pfsense_ for the firewall / router VM.

OpenIndiana
-----------

Since OpenIndiana_ has SmartOS_'s QEMU/KVM functionality (needed to run
other OS's like Linux/BSD/Windows under an illumos based distro), it
seemed worth giving a go. It actually installs itself on the system
unlike SmartOS_, so I figured it'd take a little more space. No big
deal. Until I installed it.

Then I saw that the ZFS_ boot pool can't have disks in it larger than
2TB (well, it can, but it only lets you use 2TB of the space). Doh.
After chatting with some IRC folks again, its common to use two small
disks in a mirror as a ZFS_ boot pool and then have the much larger
storage pool. Luckily I had a 250GB drive around so I could give this a
spin, though I was bummed to have to use one of my drive bays just for
a boot disk.

Installation went smoothly, but upon trying to fire up a KVM instance I
was struck by how clunky it is in comparison to SmartOS_. Again, this
difference comes down to SmartOS_ optimizing the heck out of its major
use-case.... virtualizing in the data-center. In SmartOS_ there's a
handy `imgadm <http://wiki.smartos.org/display/DOC/Managing+Images>`_
tool to manage available images, and `vmadm
<http://wiki.smartos.org/display/DOC/Using
+vmadm+to+manage+virtual+machines>`_ to manage VM's. These don't seem
to exist for OpenIndiana_ (maybe as an add-on package?), so you have to
use the less friendly QEMU/KVM tools directly.

Then the KVM failed to start. Apparently the QEMU/KVM support in
OpenIndiana_ (at least for my Sandy Bridge based motherboard) has been
`broken in the latest 3 OpenIndiana releases for the past 5 months
<https://www.illumos.org/issues/2626>`_. There's a work-around to
install a specific set of packages, but to claim QEMU/KVM support with
such a glaring bug in a fairly prominent motherboard chip-set isn't a
good first start.

My first try to install the specific packages failed as my server
kernel-panicked halfway through the QEMU/KVM package installation. Upon
restarting, the package index was apparently corrupted. The only way to
fix it is to re-install OpenIndiana_... or rollback the boot
environment (a feature utilizing ZFS_ thus including snapshots). Boot
environments and the `beadm` tool to manage them are a bit beyond the
scope of this entry, but the short version is that it let me roll-back
the boot file-system including the package index to a non-mangled state
(Very cool!).

With QEMU / KVM finally installed and working, I installed and
configured `Sophos UTM`_ in a KVM and was off and running. Except it
seemed to run abysmally slow... oh well, I was about to go on vacation
anyways. I set the KVM to load at boot-time and restarted.

Upon loading the KVM at boot, the machine halted. This issue is
apparently related to the broken QEMU / KVM packages. It was about time
for my vacation, and I had now played with an OS with some rather rough
edges in my spare time for a week. So I powered it off, took out the
boot drive, and went on my vacation.

Back to SmartOS
---------------

When I got back from my vacation, I was no longer in the mood to deal
with failures in the OS distribution. I rather like the OpenIndiana_
community, but now I just wanted my server to work. SmartOS_ fit the
bill, and didn't require boot drives which was greatly appreciated. It
also has a working QEMU / KVM, since its rather important to Joyent. :)

In just a day, I went from a blank slate to a smoothly running SmartOS_
machine. As before, installation was dead simple, and my main ZFS_
pool `zones` (named as such by SmartOS_) was ready for VM's. Before I
added a VM I figured I should have an easy way to access the ZFS_
file-system. I turned on NFS for the file-systems I wanted to access
and gave my computer's IP write privilege and the rest of the LAN
read-only. This is insanely easy in ZFS_:

.. code-block:: bash

    zfs set sharenfs=rw=MYIP,ro=192.168.2.0 zones/media/Audio

To say the least, *I love ZFS*. Every other file-system / volume
manager feels like a relic of the past in comparison. Mounting NFS
file-systems on OSX used to suck, but `now its a breeze
<http://www.motionfxdesign.com/2012/02/automatic-nfs-mount-on-osx-
lion/>`_. They work fast and reliably (thus far at least).

Setting Up the Router KVM
-------------------------

First, I needed my router / firewall KVM_. I have a DSL connection, so
I figured I'd wire that into one NIC, and have the other NIC on the
motherboard go to the LAN. SmartOS_ virtualizes these so that each VM
gets its own Virtual NIC (VNIC), this is part of the Solaris feature-
set called `Crossbow
<http://hub.opensolaris.org/bin/view/Project+crossbow/>`_. `Setting up
the new KVM <http://wiki.smartos.org/display/DOC/How+to+create+a+Virtua
l+Machine+in+SmartOS>`_ instance for `Sophos UTM`_ was simple, I gave
it a VNIC on the physical interface connected to the DSL modem and
another on the physical interface connected to my switch.

Besides for the fact that the VM was working without any issues like I
had in OpenIndiana_, I noticed it was much faster as well.
Unfortunately for some reason it wasn't actually routing my traffic. It
took me about an hour (and clearing the head while walking the dog) to
see that I was missing several important `VNIC config options
<https://github.com/joyent/smartos-
live/blob/master/src/vm/man/vmadm.1m.md>`_, such as `dhcp_server`,
`allow_ip_spoofing`, `allow_dhcp_spoofing`, and
`allow_restricted_traffic`.

These settings are needed for a VM that intends to act as a router so
that it can move the packets and NAT them as appropriate across the
VNICs. Once I set those everything ran smoothly.

So far, this only took me about 3 hours and was rather simple so I
decided to keep going and get a nice network backup for the two OSX
machines in the house.

Setting Up Network Backups
--------------------------

After some research I found out the latest version of `netatalk
<http://sourceforge.net/projects/netatalk/>`_ would work quite nicely
for network Time Machine backups. I created a `zones/tmbackups` ZFS_
file-system, and two nested file-systems under that for my wifes'
Macbook and my own Mac Mini. Then I told ZFS_ that `zones/tmbackups`
should have compression enabled (Time Machine doesn't actually compress
its backups, transparent ZFS_ file compression FTW!) and I set quota's
on each nested file-system to prevent Time Machine from expanding
forever.

Next I created a Zone_ with a `SmartOS Standard dataset <http://wiki.sm
artos.org/display/DOC/How+to+create+a+zone+%28+OS+virtualized+machine+%
29+in+SmartOS>`_. Technically, the KVM_ instances run in a Zone_ for
additional resource constraints and security, while I wanted to use
just a plain Zone_ for the network backups. This was mainly because I
wanted to make the `zones/tmbackups` file-system directly available to
it without having to NFS mount it into a KVM_.

If you've ever compiled anything from source in Solaris, you're
probably thinking about how many days I spent to get netatalk running
in a Zone_ right now. Thankfully Joyent has done an awesome job
bringing a lot of the common GNU compiler toolchain to SmartOS_. It
only took me about an hour to get netatalk running and recognized by
both macs as a valid network Time Machine backup volume.

Unfortunately I can't remember how exactly I set it up, but here are
the pages that gave me the guidance I needed:

- http://www.trollop.org/2011/07/23/os-x-10-7-lion-time-machine-netatalk-2-2/
- http://wiki.openindiana.org/oi/Netatalk
- http://marcoschuh.de/wp/?p=839

I've heard that netatalk 3.x is faster, and will likely upgrade that
one of these days.

Setting Up the Media Server KVM
-------------------------------

One of the physical machines I wanted to get rid of was the home
theater PC I had built a few years back. It was rarely used, not very
energy efficient, and XBMC_ was nowhere near spouse-friendly enough for
my wife. We have an AppleTV and Roku_, and I figured I'd give Plex_ a
try on the Roku_ since the UI was so simple.

I setup a KVM_ instance and installed Ubuntu 12.04 server on it. Then I
added the Plex_ repo's and installed their Media Server packages. Fired
it up and pointed Plex_ at my Video folders and it was ready to go. The
Roku_ interface is slick and makes it a breeze to navigate. Being based
on XBMC_ means that it can play all the same media and trans-codes it as
necessary for the other network devices that want to play it.

At first Plex_ ran into CPU problems in the KVM_... which I quickly
realized was because I hadn't changed the default resource constraints.
The poor thing only had a single virtual CPU... after giving it a few
more it easily had enough CPU allocated to do the video trans-coding.

While KVM_ runs CPU-bound tasks at bare-metal speed, disk I/O is
virtualized. To reduce this problem I have Plex_ writing its trans-
coded files to the ZFS_ file-system directly via an NFS mount. The
media folders are also NFS mounted into the Media Server KVM.

I threw some other useful apps onto this KVM_ that I was running on the
home theater PC and left it alone.

SmartOS Rocks
-------------

I now have a nice little home SmartOS_ server setup running that does a
great job taking on jobs previously done by 2 other pieces of hardware.
I still need to setup a base Ubuntu image to use for other development
KVM's, which I'll blog about when I get that going. Despite being
intended for the data-center, SmartOS_ works great for a home NAS /
Media Server / Router system. I'm sure I'll be even happier as I start
to ramp up my use of development VM's.

OpenIndiana_ is a small community taking on a big job. It's a great
community and people are very friendly. But you should expect to be
hacking on things very early on if you use it, rather than playing with
the other components. The SmartOS_ community is doing great too, and
there's more than a few forks that add some additional home-centric
type functionality. So far I haven't needed any of those enough to get
me to try them out.

Anything else I should blog about regarding SmartOS_ or the rest of my
setup?

.. _XBMC: http://xbmc.org
.. _Roku: http://www.roku.com/
.. _Plex: http://www.plexapp.com/
.. _Zone: http://en.wikipedia.org/wiki/Solaris_Containers
.. _KVM: http://www.linux-kvm.org/page/Main_Page
.. _Sophos UTM: http://www.sophos.com/en-us/products/free-tools/sophos-utm-home-edition.aspx
.. _OpenIndiana: http://openindiana.org/
.. _pfsense: http://www.pfsense.org/
.. _SmartOS: http://smartos.org/
.. _ZFS: http://en.wikipedia.org/wiki/ZFS

.. author:: default
.. categories:: SmartOS, OpenIndiana
.. tags:: none
.. comments::

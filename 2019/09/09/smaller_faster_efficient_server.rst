A Smaller, Faster, and More Efficient Home Server
=================================================

.. note::

    This is Part 1 in a series of more. I don't know how much more yet
    as this is primarily written to document my setup so I can refer to
    it later when I wonder why/how I did something.

A few years ago I built a home NAS and virtualization server. While I moved
past SmartOS after a year or two to FreeNAS, the hard drives are aging and
I realized it isn't very efficient compared to what's available now. From my prior
post, the hard drives were replaced with 6 4TB drives in a ZRAID-2. This ended
up giving me vastly more space than I had any need for and as I now have a 1Gbps
fiber line I don't feel the need to store 16 TB locally.

Given my Internet connectivity and increased focus in my spare time on containerized
applications using Kubernetes, I figured it might be a good time to 'downsize' in
power consumption while increasing my virtualization capabilities. The new server
configuration I ended up with is a fraction of the size (half-length 1U vs full-length 2U)
and power (190w idle vs 40w idle), while having 4x the cores and over 8x the memory
capacity. 7 years has definitely helped on what you get for the same price!

System Specs
------------

It took awhile before Epyc embedded processors and vendors 1U systems started to hit
the market, but the 8-core/16-thread Epyc 3251 in a nice half-length 1U
is now widely available. `Serve The Home did a great review of this system
<https://www.servethehome.com/supermicro-as-5019d-ftn4-review-a-1u-amd-epyc-3251-server/>`_
which helped convince me to purchase one.

Here are specs for this build:

- **CPU/Motherboard**: AMD Epyc Embedded 3251 (8-core / 16-thread) on Supermicro M11SDV-8C-LN4F
- **Case**: Supermicro AS 5019D-FTN4
- **RAM**: Supermicro DDR4-2666 64 GB ECC LRDIMM x2 (128 GB total)
- **NVMe Drive**: Samsung 970 Evo Plus 1TB
- **SATA Drive**: Sandisk Ultra 3D 2TB

.. image:: /_static/garage_server_2019.jpg
    :align: center
    :alt: My 2019 Home virtualization server

Overall cost: **~$2100**

This is a bit more than the last buuild, but is 100% SSD storage without any redundancy. I'm
relying on cloud backups and accepting that I will have some downtime if a part fails. I
consider this an acceptable trade-off to keep costs lower with the hope that once a SSD has
proven itself for a few months it should last much longer than a spinning platter drive as
I don't anticipate heavy read/write loads that would wear out the drives.

.. note::

    In the event an SSD fails, I'm only a 10min drive from a Best Buy where I got both the
    SSD's. I consider this a more likely failure scenario than the PSU, CPU, memory, or
    motherboard failing in my experience (I already ran a memtest suite against the memory
    before installing proxmox, which comes with memtest on their live ISO).

If I really go nuts with VM's and containers I still have 2 DIMM slots free for another
128 GB of memory. I've found that for personal use containers usually run into RAM
pressure much earlier than CPU pressure.

OS Choice
---------

I've been reading a lot of `Serve the Home`_, and their glowing review of Proxmox VE
convinced me to give it a try. I've been enjoying it so far and it's easy to get started
with and makes running KVM a breeze.

**ProxMox VE** it is!

I grabbed the ISO for installing ProxMox 6.0, based on a buster debian distro. Using
the ISO directly from my computer was rather easy from the Supermicro IPMI Java
interface. While the ikvm HTML5 interface is more convenient, the Java-based console
makes it a breeze to attach local .iso files as a CD/DVD drive to the server.

I'm running the community edition, which requires you to edit the
``/etc/apt/sources.list`` to include the `non-enterprise deb <https://pve.proxmox.com/wiki/Package_Repositories#_proxmox_ve_no_subscription_repository>`_::

    deb http://download.proxmox.com/debian/pve buster pve-no-subscription

Additional steps:

1. From the shell in the web UI::

       apt-get update
       apt-get dist-upgrade -y
       reboot

2. Add the additional drive as a new lvm-thin pool

.. note::

  I have set all the VM hard drives under the default lvm-thin pool which
  is on the NVMe SSD for performance. The SATA SSD is to be used for persistent
  data volumes for containers.

AWS Storage Apppliance
----------------------

The first thing I wanted to try was utilizing hybrid storage in AWS with their Storage
Appliance. Unfortunately AWS only provides a VMWare image. I found a few articles online
that indicated this was rather easy to convert to a raw disk image for use in Proxmox, and
got it working rather quickly.

1. Download the AWS Storage Gateway zipfile
2. Unzip the zipfile (resulting in an ``.ova`` file)
3. ``tar xf AWS-Appliance-2019-07-24-1563990364.ova`` (Filename dependent on time it was d/l)
4. ``qemu-img info AWS-Appliance-2019-07-24-1563990364-disk1.vmdk`` and record the virtual size
   to use when provisioning a proxmox KVM
5. Provision a Proxmox VM with the given size disk, using an IDE disk emulation target. I gave
   my VM 16GB of memory, as I wasn't sure how much it would want.
6. Determine the location of the LVM disk used by the new VM (something like ``/dev/pve/vm-100-disk-0``).
7. Convert the vmware disk image to the raw::

       qemu-img convert -f vmdk -O raw AWS-Appliance-2019-07-24-1563990364-disk1.vmdk /dev/pve/vm-100-disk-0

8. Edit the VM hardware to add the LVM-thin drive resource. I added a 150Gb
   hard drive as another IDE resource per AWS recommendations for local cache size.
9. Start the VM.
10. Look at the console in proxmox to determine the IP, and change it as desired for a static
    IP.
11. Finish setup in the AWS Console for the Storage Gateway, your computer will need to be
    able to talk directly to the VM running the appliance VM. You will be asked to set a
    cache drive, select the additiona 150Gb drive.

Pros
~~~~

- Fast access to frequently accessed files that fit within the cache
- Everything backed by S3 reliability
- As much storage as you want to pay for
- It's fun to see that your SMB share has 7.99 Exabytes free

Cons
~~~~

- Unavailable when the Internet is out
- Slower access than a NAS
- SMB requires an Active Directory server for user based permissions or a single
  guest account with read/write access to all SMB shares.
- NFS shares have similarly odd restrictions

RancherOS
---------

I followed `these directions <https://gist.github.com/mow4cash/a57e893fc640ccf3720e99fc6b3b879a#install-rancheros>`_
to install RancherOS under ProxMox VE. Reproduced here with a fix to the ``cloud-config.yml`` as the
example didn't validate.

1. Download RancherOS ISO
2. Upload the iso to (local)pve
3. Setup a VM with RancherOS ISO as CD. Give it at least 3gb ram to start. Rancher Server failed with low ram
4. Boot
5. From Console change password

   * sudo bash
   * passwd rancher

6. SSH to rancher@
7. prepare your ssh keys with putty gen or local ssh key-gen

   * vi cloud-config.yml

8. paste the cloud config edited with your settings, make sure the pasted data is pated correctly, add your key in a single line
9. press exit exit :wq to save

  ::

    #cloud-config

        rancher:
          network:
            interfaces:
              eth0:
                address: 10.68.69.92/24
                gateway: 10.68.69.1
                mtu: 1500
                dhcp: false
            dns:
              nameservers:
              - 1.1.1.1
              - 8.8.4.4

        ssh_authorized_keys:
          - ssh-rsa <YOUR KEY>

* ``sudo ros config validate -i cloud-config.yml``
* ``sudo ros install -c cloud-config.yml -d /dev/sda``

10. Remove CD Image from VM, and then reboot.
11. SSH back into RancherOS (rancher@) using your new ssh private key

Rancher
-------

With RancherOS running happilly, its time to install Rancher on the VM. This is
relatively easy, from the RancherOS VM shell, just run::

  sudo docker run -d --restart=unless-stopped -p 8080:80 -p 8443:443 -v rancher:/var/lib/rancher rancher/rancher:stable

Mapping port 80/443 to different local ports is to avoid intereference from the
ingress proxy which will be running on this same node.

Once Rancher is available on port ``8443``:

1. Add a cluster, of custom type.
2. Name it, and hit next.
3. Select all three node options (etcd, Control Plane, Wokrer)
4. Copy the command shown and run it in the RancherOS shell.
5. Click Done in the Rancher UX.
6. The cluster will become available.

Setup the SATA SSD
~~~~~~~~~~~~~~~~~~

I want to use the SATA SSD for persistent volumes for the containers:

1. Add a hard drive in Proxmox VE to RancherOS VM
2. Choose a sufficient size (I choose 400 GB)
3. Start the RancherOS VM (or restart it)
4. Verify additional hard drive appears in ``fdisk -l``
5. Format the hard drive with ``fdisk /dev/sdb``
6. Choose new partition, primary, select default start/end values
7. Format the partition with ``mkfs.ext4 /dev/sdb``
8. Set it to load at start in RancherOS::

     ros config set mounts '[["/dev/sdb","/mnt/data","ext4",""]]'

9. Reboot and verify ``/mnt/data`` is a volume mount.

Fin
---

That's it for a first day of configuring things. Next up I'll need
to setup MetalLB_ so that my Kubernetes containers I start with Rancher
get LAN IP's rather than shuttling everything through the default nginx
ingress.

.. _MetalLB: https://metallb.universe.tf/
.. _Serve the Home: https://www.servethehome.com/

.. author:: default
.. categories:: none
.. tags:: none
.. comments::

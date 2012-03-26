XML-RPC interface for Growl
===========================

`Growl <http://growl.info/>`_ is a rather spiffy little notifier for OS
X I've started using lately. Currently however, it's lacking a nice way
to send messages over the network. Since `a
project <http://www.hellanzb.com/>`_ I'm working on would be even
slicker with a way to communicate updates, I quickly tacked a Python
XML-RPC Server onto Growl using Growl's Python bindings.

In the future, Growl will have its own network interface, I've heard.
Until then, this does the job quite nicely.

Please note: You will need to install the `latest svn of
Growl <http://growl.info/documentation/growl-source-install.php>`_, the
`PyObjC bridge <http://pyobjc.sourceforge.net/>`_, and have `Xcode
1.5 <http://developer.apple.com/tools/download/>`_ to get this working.
Everything in ALL\_CAPS should be changed as needed, this also assumes
you want to use icons and they're in a myIcons dir.

::

    #!/usr/bin/python

        import Growlimport SimpleXMLRPCServerfrom AppKit import NSImageimport sys, os.path

        iconPath = 'myIcons/'Icons = { 'MESSAGE_1' : 'MESSAGE_1.tiff', \
              'MESSAGE_2' : 'MESSAGE_2.tiff' }

        class MemberFunctions:
        def init(self,Icons):
            gn = Growl.GrowlNotifier()
            gn.applicationName = 'YOUR_APP_NAME'
            gn.applicationIcon = Icons['appIcon']
            gn.notifications = ['MESSAGE_1','MESSAGE_2']
            gn.register()
            self.gn = gn
            self.Icons = Icons

        def notify(self, ntype, title, description, sticky):
            gn = self.gn
            Icons = self.Icons
            nIcon = Icons['appIcon']
            if ntype  'MESSAGE_1':
                nIcon = Icons['MESSAGE_1']
            elif ntype  'MESSAGE_2':
                nIcon = Icons['MESSAGE_2']
            gn.notify(noteType=ntype,title=title,description=description,
                icon=nIcon, sticky=sticky)
            return 1

        def loadIcons(icons):
        global iconPath
        for icon in icons.keys():
            filename = icons[icon]
            nImagePath = os.path.abspath(iconPath+filename)
            nIcon = NSImage.alloc().initWithContentsOfFile_(nImagePath).autorelease()
            if not nIcon:
                sys.stderr.write(“Couldn't load file %s\n” % nImagePath)
            icons[icon] = nIcon
        return icons

        Icons = loadIcons(Icons)

        Make our XMLRPC Server, create our instance, and assign it
        server = SimpleXMLRPCServer.SimpleXMLRPCServer((“IP_TO_BIND_TO”, 7300))memfun = MemberFunctions(Icons)server.register_function(memfun.notify)

         Start the server
        server.serve_forever()

If you'd like to see a running example of this, check out
`hellagrowler.py <http://www.hellanzb.com/trac.cgi/file/trunk/hellagrowler.py>`_
that this example is based heavily on.


.. author:: default
.. categories:: Python, Code
.. comments::
   :url: http://be.groovie.org/post/296355142/xml-rpc-interface-for-growl
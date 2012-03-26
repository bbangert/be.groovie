Fast CGI with HTML::Mason
=========================

I decided the other day for a variety of reasons, to switch from the
mod\_perl web-app style to using Fast CGI with HTML::Mason. I only found
one application out there that uses `Mason <http://www.masonhq.com/>`_
with `Fast CGI <http://www.fastcgi.com/>`_, which was the `RT Ticket
tracking <http://www.bestpractical.com/rt/>`_ system. However, the way
it was setup didn't match my requirements, nor the way their handler was
configured.

After scouring the Internet some more, I hobbled together a working
config section for my Apache+mod\_fastcgi along with a template for the
mason handler. Since I haven't seen anything going over these basic
steps anywhere else, here's how I did it.

First, the things you should have installed on your system (which I'm
assuming is \*nix):

-  HTML::Mason
-  CGI::Fast
-  Apache w/mod\_fastcgi

Fast CGI runs your CGI application for you, and handles connections
between your application, and the webserver. To configure your
application, you just use one of the Fast CGI development kits for the
response event loop within which your application will process requests.

Since we're using Perl, there's already a handy module available from
CPAN that I chose to use called CGI::Fast. Then we just wrap our Mason
call within a CGI::Fast loop to handle requests. This Perl script will
be kept running persistently so that you get the advantage of not having
to startup the Perl interpreter on every web page request.

Why Fast CGI instead of mod\_perl?

-  You can use the connection feature of Fast CGI to run your app on a
   different machine than the webserver
-  Your application takes up only as much ram as Perl + your modules
-  It's more portable, you don't even need to use Apache, any webserver
   supporting Fast CGI will work
-  Less configuration files to maintain

Before showing my standard handler template, you should be aware of how
I organize a Mason site using Fast CGI. Here's what my directory
structure looks like under the fictional GroovieWebapp:

-  GroovieWebapp/

   -  site/
   -  modules/
   -  libs/
   -  mdata/
   -  mason-handler.fcgi

Site is where all of our Mason code (and images, css, etc.) is going to
go. Modules is for putting any of your own Perl modules into that you
made specifically for this webapp. libs for Mason libs, mdata for your
Mason data dir, and finally the handler itself. This structure puts your
whole webapp under one directory which is also useful under version
control systems like `Subversion <http://subversion.tigris.org/>`_.

Here's what my standard handler template looks like
(mason-handler.fcgi):

::

    #!/usr/bin/perluse FindBin qw($Bin);use lib “$Bin/modules”;

        use strict;use HTML::Mason::CGIHandler;use MIME::Lite;  # Need this to e-mail the error

        Enter CGI::Fast mode, which should also work as a vanilla CGI script.
        require CGI::Fast;

        my $h;my $show_error = 1;  # Should we e-mail the error, or dump to the web?

        if ($show_error) {
        $h = HTML::Mason::CGIHandler->new
            ( comp_root => [
                  [main => “/usr/local/www/GroovieWebapp/site”],
                  [libs => “/usr/local/www/GroovieWebapp/libs”]
              ],
              data_dir => “/usr/local/www/GroovieWebapp/mdata”,
              allow_globals => [qw($Schema $Session)]
            );} else {
        $h = HTML::Mason::CGIHandler->new
            ( comp_root => [
                  [main => “/usr/local/www/GroovieWebapp/site”],
                  [libs => “/usr/local/www/GroovieWebapp/libs”]
              ],
              data_dir => “/usr/local/www/GroovieWebapp/mdata”,
              error_format => 'text',
              error_mode => 'fatal',
              allow_globals => [qw($Schema $Session)]
            );}

        Setup our global vars for the request, preload our modules
        { package HTML::Mason::Commands;
      use Apache::Session::File ();    # My favorite for session tracking
      use CGI::Cookie;                 # Also for session tracking
      use DBI;   # It's nice to load and establish our db connection in advance
      DBI->install_driver(“mysql”);  # Put in whatever connection you use, etc.

      # This allows our $Schema variable to be accessed from anywhere in our Mason site
      our $Schema = DBI->connect_cached(“dbi:mysql:DB_NAME”,“DB_USER”, “DB_PASSWORD” );
    }

         These two subroutines add Mason functionality that was lost by using CGIHandler instead
            of the ApacheHandler.
        sub HTML::Mason::FakeApache::document_root {
        my $self = shift;
        return $ENV{'DOCUMENT_ROOT'};}sub HTML::Mason::FakeApache::param {
        my $self = shift;
        my $key = shift;
        my %args = HTML::Mason::Utils::cgi_request_args($self->query,$self->query->request_method);
        my @keys = (keys %args);

        if ($key) {
            return $args{$key};
        } else {
            return @keys;
        }
    }

        For e-mailing the error
        sub send_email {
        my $error = shift;
        my $cgi = shift;
        my $site = $cgi->virtual_host();
        my $time = localtime;
        my $body = “————————————————————\n”;
        $body   .= “———— ERROR OCCURRED\n”;
        $body   .= “————————————————————\n”;
        $body   .= “\n\n”;
        $body   .= “WEBSITE INFO\n”;
        $body   .= “Site: $site\n”;
        $body   .= “Full URI Request: “.$ENV{'REQUEST_URI'}.”\n”;
        $body   .= “Time: $time\n”;
        $body   .= “\n\n”;
        $body   .= “USER INFO\n”;
        $body   .= “Referrer: “.$cgi->referer().”\n”;
        $body   .= “User-agent: “.$cgi->user_agent().”\n”;
        $body   .= “IP Address: “.$cgi->remote_host().”\n”;
        $body   .= “Cookie info: “.$cgi->raw_cookie().”\n”;
        $body   .= “\n\n”;
        $body   .= “MASON ERROR\n”;
        $body   .= $error;

        my $msg = MIME::Lite->new( From    => 'YOUR SITE ',
                                   To      => 'YOUR_EMAIL_ADDRESS',
                                   Subject => “$site Mason Website Error occured at $time”,
                                   Data    => $body,
                                 );
        $msg->send('smtp','YOUR_SMTP_SERVER');
    }

        while (my $cgi = new CGI::Fast) {
        # the whole point of fastcgi requires the env to get reset here..
        # So we must squash it again (This was copied from RT's Fast CGI handler)
        $ENV{'PATH'}   = ‘bin:/usr/bin';
        $ENV{'CDPATH'} = '' if defined $ENV{'CDPATH'};
        $ENV{'SHELL'}  = ‘bin/sh' if defined $ENV{'SHELL'};
        $ENV{'ENV'}    = '' if defined $ENV{'ENV'};
        $ENV{'IFS'}    = '' if defined $ENV{'IFS'};

        # The Mason $r->uri includes the script name unless we do this
        $ENV{'SCRIPT_NAME'} = '';

        # This deals with someone entering yoursite.com/ to make sure it serves index.html
        if ( ( !$h->interp->comp_exists( $cgi->path_info ) )
            && ( $h->interp->comp_exists( $cgi->path_info . “index.html” ) ) ) {
            $cgi->path_info( $cgi->path_info . “index.html” );
        }
        #$cgi->header(-charset=>'utf-8');  # If your site uses utf-8 characters

        # Ping our db handle
        $HTML::Mason::Commands::Schema->ping;

        # Lets try and handle this…
        eval {
            $h->handle_cgi_object($cgi);
        };

        # Something happened, if it couldn't find the component, don't fatal
        # we'll re-process as a 404
        if ($@) {
            if ($@ =~ /could not find component/) {
                # If you want Mason to handle the error so you can keep your site appearence,
                # this will call Mason to display your error page. If the error was in the
                # code that is called on every page, this will cause trouble.
                $cgi->path_info('/errordocs/404.html');
                $h->handle_cgi_object($cgi);
            } else {
                send_email($@,$cgi);
            }
        }
    }

This template has the option of either showing the Mason debugging
output to the screen, or capturing the error, displaying a pretty 404 of
your desire, and e-mailing you the error that occured.

Now for the Apache httpd.conf:

::

        Tell FastCGI to put its temporary files somewhere sane.
        FastCgiIpcDir /tmp

        Increases processes if you have heavy loads to deal with
        FastCgiServer /usr/local/www/GroovieWebapp/mason-handler.fcgi -idle-timeout 120 -processes 2 

        
        ServerAdmin webmaster@YOUR_SERVER
        ServerName YOUR_SERVER_NAME

        AddHandler fastcgi-script fcgi
        ScriptAliasMatch (.*\.html$) /usr/local/www/GroovieWebapp/mason-handler.fcgi$1
        ScriptAliasMatch (.*\/$) /usr/local/www/GroovieWebapp/mason-handler.fcgi$1

        DocumentRoot /usr/local/www/GroovieWebapp

Restart apache, and check apache's error\_log to see that Fast CGI
started up your application properly. Obviously, tailor these samples as
needed. Another useful trick when running your webapp this way, is that
if you kill the perl processes the apache Fast CGI process manager
starts for you, it'll re-spawn them. I find this a quick way to re-load
individual webapps if I made changes to a module they're using.

**Enjoy!**


.. author:: default
.. categories:: Perl, Code
.. comments::
   :url: http://be.groovie.org/post/296355060/fast-cgi-with-html-mason
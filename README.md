Gandi.net API in Python & Command Line Client
=============================================

This is a command line client for the [Gandi HTTP API](http://doc.rpc.gandi.net/).

For now, only a couple of DNS related functions are implemented. Pull requests
are certainly welcome. It's straightforward to extend.

Usage
-----

DNS.

These work with the default zone:

    $ gandi dns example.org add
    $ gandi dns example.org delete
    $ gandi dns example.org list

Or you can use zones explicitly (not implemented):

    $ gandi zone VERSION_ID add
    $ gandi domain example.org set-zone

What is Thingdom?
=================

    `Thingdom <https://thingdom.io>`_ allows you to mobile-enable your product in four lines of code with no need
    to develop the iOS and Android apps or create scalable cloud infrastructure.

    `Get Started Now! <https://thingdom.io/sign-up>`_.


Installation
============

    pip install thingdom


Ideas for Module Usage
======================

1. Programmatically trigger push notifications, feed messages, and real-time status updates from your Python app.
2. Remotely monitor any interaction with your Python application.
3. With our quick drop-in integration and simple API calls you can mobile-enable your Python application in a matter of hours, even customizing the mobile experience for your end-users.


Getting Started
===============

    ::

        from thingdom import Thingdom

        # instantiate Thingdom object and authenticate
        thingdom = Thingdom( 'YOUR_API_SECRET' )

        # look-up Thing and get back object
        thing = thingdom.get_thing( 'YOUR_THING_NAME' )

        # send a feed message
        thing.feed( 'FEED_CATEGORY', 'MESSAGE' )

        # send a status update
        thing.status( 'KEY', 'VALUE' )

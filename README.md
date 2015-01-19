Thingdom Python Module
===========

The official Python wrapper for the [Thingdom API](https://thingdom.io/).

## What is Thingdom?

[Thingdom](https://thingdom.io) allows you to mobile-enable your product in four lines of code with no need to develop the iOS and Android apps or create scalable cloud infrastructure. [Get Started Now!](https://thingdom.io/sign-up)

<p align="center">

<img src="https://thingdom.io/images/profile/5.png?raw=true" height="400px" />

<img src="https://thingdom.io/images/profile/2.png?raw=true" height="400px" />

</p>

## Installation
```

```

## Getting Started
```
require 'thingdom'

# instantiate Thingdom object and authenticate
thingdom = Thingdom( 'YOUR_API_SECRET' )

# look-up Thing and get back object
thing = thingdom.get_thing( 'YOUR_THING_NAME' )

# send a feed message
thing.feed( 'FEED_CATEGORY', 'MESSAGE' )

# send a status update
thing.status( 'KEY', 'VALUE' )

```

## Ideas for Module Usage

1. Programmatically trigger push notifications, feed messages, and real-time status updates from your Python app.
2. Remotely monitor any interaction with your Python application.
3. With our quick drop-in integration and simple API calls you can mobile-enable your Python application in a matter of hours, even customizing the mobile experience for your end-users.

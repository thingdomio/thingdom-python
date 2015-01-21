#
# A class that provides the web services needed by the Python wrapper.
#
from httpHelper import HttpHelper


class WebService:
    #
    # The constructor method WebService.  Save the application secret and initialize
    # other local variables.
    #
    def __init__(self, secret):
        self._httpHelper = HttpHelper()
        self._secret = secret
        self._applicationToken = ''
        self._deviceSecret = 'none'

    #
    # Ping the Thingdom server.
    #
    # Returns a dictionary containing the fields in the ping response.
    #
    def ping_server(self):
        print 'Pinging from web service'
        response = self._httpHelper.get_data('ping')
        return response

    #
    # Authorize this application by sending the application secret to Thingdom.  If valid, Thingdom will send back a
    # token which must be used in subsequent communications.
    #
    # Returns a dictionary containing the common request response fields plus these for authorization:
    #     application_token - The token used in subsequent communications with Thingdom.
    #     expires_in - The number of seconds remaining before the above token expires.
    #     device_secret - A unique identifier for the device running this application.
    #                    (always "none" for the Python wrapper)
    #
    def get_authorization(self):
        data = {
            'api_secret': self._secret,
            'device_secret': self._deviceSecret
        }
        response = self._httpHelper.post_data('token', data)
        self._applicationToken = response['application_token']
        return response

    #
    # Retrieve a thing.  If it doesn't exist, then add it.
    #
    # thing - The thing to get or add.
    # Returns a dictionary containing the common request response fields plus these for thing:
    #     thing_id - The id of the thing.
    #     code - The thing code that is used to subscribe to the thing via the mobile app (i.e. allows the mobile
    #            app user to see the feeds and status updates for the thing).
    #
    def add_thing(self, thing):
        data = {
            'token': self._applicationToken,
            'name': thing.name,
            'display_name': thing.display_name
        }
        if len(thing.product_type) > 0:
            data['product_type'] = thing.product_type

        response = self._httpHelper.post_data('thing', data)
        return response

    #
    # Add or update a status item for a thing.
    #
    # thing - The thing to which the status item is associated.
    # statusArray - An array of status item updates (name, value, unit)
    # Returns a dictionary containing the common request response fields.
    #
    def add_status(self, thing, statusArray):
        data = {
            'token': self._applicationToken,
            'thing_id': thing.id,
            'id': 'null',
            'status_array': statusArray
        }
        response = self._httpHelper.post_data('status', data)
        return response

    #
    # Add a feed message to a thing.
    #
    # thing - The thing associated with the feed message.
    # category - The feed category.
    # message -  The feed message.
    # feedOptions - Additional feed options (icon, progress bar, etc).
    # Returns a dictionary containing the common request response fields.
    #
    def add_feed(self, thing, category, message, feedOptions):
        data = {
            'token': self._applicationToken,
            'thing_id': thing.id,
            'feed_category': category,
            'message': message,
            'options': feedOptions
        }
        response = self._httpHelper.post_data('feed', data)
        return response
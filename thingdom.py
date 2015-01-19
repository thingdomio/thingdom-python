#
# The top level class that provides the Thingdom API
#
import constants
from webService import WebService
from thing import Thing


class Thingdom:

    #
    # Constructor method for Thingdom that accepts an application secret.
    #
    def __init__(self, appSecret):
        #
        # Create the web service.
        #
        self._web = WebService(appSecret)
        self._applicationToken = ''
        #
        # Authenticate the application using the application secret.  If successful, save the application token that
        # is returned for all subsequent communications with Thingdom.  Otherwise, raise an exception using the
        # returned error message.
        #
        response = self._web.get_authorization()
        result = response[constants.RESPONSE] != 'error' and \
                 response['application_token'] is not None and \
                 len(response['application_token']) > 0
        if result:
            self._applicationToken = response['application_token']
        else:
            raise Exception(response[constants.MSG])

    #
    # Get a thing. If it doesn't exist, then create it.
    #
    # name - The thing name.
    # productType - The thing's product type.
    # displayName - The thing's display name.
    # Returns a thing object.
    #
    def get_thing(self, name, productType='', displayName=''):
        thing = Thing(self._web, name, productType, displayName)
        return thing
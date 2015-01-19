#
# A class that represents a Thing.
#
import constants
import sys
sys.path.append('./tasks')

from thingTask import ThingTask
from feedTask import FeedTask
from statusTask import StatusTask


class Thing:
    #
    # Constructor method for Thing that accepts a web service instance, name,
    # product type and display name.
    #
    def __init__(self, webService, name, product_type = '', display_name = ''):
        self._web = webService
        self.id = ''
        self.name = name
        self.product_type = product_type
        self.display_name = display_name
        self.code = ''
        self.last_error = ''
        #
        # Perform task to get/create thing.
        #
        thingTask = ThingTask(webService, self)
        response = thingTask.perform()
        #
        # If successful, update the thing id and code.
        #
        if response[constants.RESPONSE] == 'success':
            self.id = response['thing_id']
            self.code = response['code']

    #
    #
    #
    def feed(self, category, message, feedOptions=None):
        feedTask = FeedTask(self._web, self, category, message, feedOptions)
        response = feedTask.perform()
        return response

    #
    #
    #
    def status(self, *args):
        statusTask = StatusTask(self._web, self, *args)
        response = statusTask.perform()
        return response

    # *************************************************************************
    # Thing Properties
    # *************************************************************************

    #
    # Thing id property.
    #
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    #
    # Thing name property.
    #
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    #
    # Thing product type property.
    #
    @property
    def product_type(self):
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        self._product_type = product_type

    #
    # Thing display name property.
    #
    @property
    def display_name(self):
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        self._display_name = display_name

    #
    # Thing code property.
    #
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    #
    # Thing last error property.
    #
    @property
    def last_error(self):
        return self._last_error

    @last_error.setter
    def last_error(self, last_error):
        self._last_error = last_error
#
# A class that handles all HTTP communication with Thingdom.
#
import urllib2
import json


class HttpHelper:
    #
    # Constructor method.  Initialize local data.
    #
    def __init__(self):
        self._uri = 'https://api.thingdom.io/1.1'
        self._request_counter = 0

    #
    # Perform a HTTP Get request.
    #
    # requestPath - a string containing the path and optional query parameters (e.g. path/to/somewhere?param1=1&param2=2)
    # Returns a dictionary representing the request response
    #
    def get_data(self, requestPath):
        response = self._do_request(requestPath, None)
        return response

    #
    # Perform a HTTP Post request.
    #
    # requestPath - a string containing the path to where data will be posted (e.g. path/to/post/endpoint)
    # data - a dictionary containing the data that will be posted.
    # Returns a dictionary representing the request response.
    #
    def post_data(self, requestPath, data=None):
        self._request_counter += 1
        data['counter'] = str(self._request_counter)
        data['time'] = '2015/01/15 09:30:00'
        response = self._do_request(requestPath, data)
        return response

    # *************************************************************************
    # Helper Methods
    # *************************************************************************

    #
    # Perform HTTP request.
    #
    # requestPath - a string containing the path to where data will be retrieved or posted.
    # data - a dictionary containing the data that will be posted.
    # Returns a dictionary representing the request response.
    #
    def _do_request(self, requestPath, data):
        url = self._uri + '/' + requestPath
        request = urllib2.Request(url)
        if data is not None:
            request.add_header('Content-Type', 'application/json')
            request.add_data(json.dumps(data))
        response = urllib2.urlopen(request)
        responseJson = json.load(response)
        return responseJson


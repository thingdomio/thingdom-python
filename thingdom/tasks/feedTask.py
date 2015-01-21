#
# A class that does the work for adding a feed to a thing.
#
from baseTask import BaseTask


class FeedTask(BaseTask):
    #
    # Constructor method for feed task that accepts a web service instance, a thing object, feed category,
    # feed message and additional feed options.
    #
    def __init__( self, webService, thing, category, message, feedOptions ):
        super(FeedTask, self).__init__(webService, thing, False)
        self._category = category
        self._message = message
        self._feedOptions = feedOptions

    #
    # Do the work for the feed task
    #
    def do_task_work(self):
        response = self._web.add_feed(self._thing, self._category, self._message, self._feedOptions)
        return response
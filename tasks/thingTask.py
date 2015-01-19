#
# A class the does the work for creating or retrieving a thing.
#
from baseTask import BaseTask


class ThingTask(BaseTask):

    #
    # Constructor method for ThingTask that accepts a web service instance and a thing object.
    #
    def __init__(self, webService, thing):
        super(ThingTask, self).__init__(webService, thing, True)

    #
    # Do the work for the thing task.
    #
    def do_task_work(self):
        response = self._web.add_thing(self._thing)
        return response
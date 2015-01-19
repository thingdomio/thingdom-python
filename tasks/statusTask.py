#
# A class that does the work for updating the status for a thing.
#
from baseTask import BaseTask


class StatusTask(BaseTask):

    #
    # Constructor method for StatusTask that accepts a web service instance, a thing object and either a single
    # status update or an array of status updates.
    #
    def __init__(self, webService, thing, *args ):
        super(StatusTask, self).__init__(webService, thing, False)
        self._statusUpdates = self._statusArgsToList(*args)

    #
    # Do the work for the status task.
    #
    def do_task_work(self):
        response = self._web.add_status(self._thing, self._statusUpdates)
        return response

    # *************************************************************************
    # Helper methods.
    # *************************************************************************

    #
    # Convert status args int a list of dictionaries (actually a list containing one dictionary).
    #
    # args - A tuple containing a single status update arguments (name, value, unit) or
    #        a list of status updates.
    # Returns either the original list, or a list containing a dictionary for the single update.
    #
    def _statusArgsToList(self, *args):
        dataList = []
        #
        # If only one argument, then assume it is already a list.
        #
        if len(args) == 1:
            dataList = args[0]
        #
        # Otherwise, take the individual arguments, create a dictionary and insert into list.
        #
        elif len(args) >= 2:
            data = { 'name': args[0], 'value': args[1] }
            if len(args) == 3:
                data['unit'] = args[2]
            dataList.append(data)
        #
        # Return the result.
        #
        return dataList



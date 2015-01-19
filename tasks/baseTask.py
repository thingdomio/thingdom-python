#
# A pseudo abstract class that provides common functionality for performing tasks on a thing.  These
# are:  retrieving or creating a thing, updating status and sending a feed.
#
import constants


class BaseTask(object):
    #
    # Constructor method for base class that accepts a web service instance, a thing object and a flag that
    # indicates if the task is for getting/adding a Thing.
    #
    def __init__(self, webService, thing, isThingTask):
        self._web = webService
        self._thing = thing
        self._isThingTask = isThingTask

    #
    # Perform the task.
    #
    def perform(self):
        response = {}
        #
        # Make sure thing is valid (id and code exist) before doing any work.  The exception of course is if we
        # are creating or retrieving a thing, in which case, id and code will not exist.
        #
        if (len(str(self._thing.id)) > 0 and len(self._thing.code) > 0) or self._isThingTask:
            #
            # Do the task work
            #
            try:
                response = self.do_task_work()
                if response[constants.RESPONSE] == 'token_expired':
                    self._web.get_authorization()
                    response = self.do_task_work()
            #
            # On any exception, return an error response with the exception description in the message.
            #
            except Exception as e:
                response[constants.RESPONSE] = 'error'
                response[constants.MSG] = e.message
                self._thing.last_error = e.message
        #
        # Thing has not been created.  Return the appropriate error and message.
        #
        else:
            response[constants.RESPONSE] = 'error'
            response[constants.MSG] = 'Thing ' + self._thing.name + ' has not been created.'

        return response

    #
    # This method should be overridden by the subclass and does the specific task work.
    #
    def do_task_work(self):
        return { constants.RESPONSE: 'error', constants.MSG: 'Task work method not implemented.' }


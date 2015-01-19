from thingdom import Thingdom

results = 'Success'
try:
    thingdom = Thingdom('2nhbhDbbjDRTcsCKdkWwjwgCHFRCqCnRwPe8QvYPwjrfybyEpZxMRHP2VvPxjKsPdc7jFGMvvQqzRbSjvFeXYpuGvFjC8fwNTGgc')
except Exception as e:
    results = e.message
print 'Results of Thingdom Initialization: ' + results

thing = thingdom.get_thing('whiskers', 'cat', 'Whiskers')

updates = [{'name': 'hungry', 'value': True}, {'name': 'awake', 'value': False}]
result = thing.status(updates)
print 'Results of Status Update: ' + result['response']

result = thing.feed('activity', 'Snoozing')
print 'Results of Feed: ' + result['response']

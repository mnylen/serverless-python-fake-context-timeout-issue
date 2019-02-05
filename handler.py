def hello(event, context):
    print("context.timeout: %d" % context.timeout)
    print("context.get_remaining_time_in_millis(): %d" % context.get_remaining_time_in_millis())


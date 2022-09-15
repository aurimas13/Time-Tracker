def get_task_values(query):
    """
    This is the method for transforming values from SQL database to HTML-readable values.

    A query of two modules is provided. The function extracts the information
    into task and actual_time dictionaries while returning an updated list - tasks.
    It loops through all these dictionaries.
    First if loops remove irrelevant key/value pairs while other if loops update
    actual_time and actual_times_sum values.

    args:
        query (list of tuples of Task, TaskActualTimes)
    return:
        tasks(list)
    """
    tasks = {}
    for row in query:
        task = row[0].__dict__
        actual_time = row[1].__dict__
        key_id = task['task_id']

        if '_sa_instance_state' in task:
            del task['_sa_instance_state']
        if '_sa_instance_state' in actual_time:
            del actual_time['_sa_instance_state']

        if key_id in tasks:
            if actual_time['actual_time']:
                tasks[key_id]['actual_times'].append(actual_time)
                tasks[key_id]['actual_times_sum'] += actual_time['actual_time']
        else:
            tasks[key_id] = task
            if actual_time['actual_time']:
                tasks[key_id]['actual_times'] = [actual_time]
                tasks[key_id]['actual_times_sum'] = actual_time['actual_time']
            else:
                tasks[key_id]['actual_times'] = []
                tasks[key_id]['actual_times_sum'] = 0
    tasks = list(tasks.values())
    return tasks
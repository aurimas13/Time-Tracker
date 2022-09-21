def summarize_developers(query):
    """
    This is the method for transforming values from SQL database to HTML-readable values.

    A query of three modules is provided. The function extracts the information into
    task, actual_time and developer dictionaries while returning an updated list - developers.
    For loop loops through all these dictionaries.
    First if loops remove irrelevant key/value pairs while other if loop checks for the existence of value
    and update actual_time and actual_times_sum values.

    args:
        query (list of tuples of Task, TaskActualTimes, Developer)

    return:
        developers(list)
    """
    developers = {}
    tasks_ids = []
    for row in query:
        task = row[0].__dict__
        task['estimated_points'] = task['estimated_points'] if task['estimated_points'] else 0
        actual_time = row[1].__dict__
        actual_time['actual_time'] = actual_time['actual_time'] if actual_time['actual_time'] else 0
        developer = row[2].__dict__
        dev_id = developer['id']
        task_idx = task['task_id']

        if '_sa_instance_state' in task:
            del task['_sa_instance_state']
        if '_sa_instance_state' in actual_time:
            del actual_time['_sa_instance_state']
        if '_sa_instance_state' in developer:
            del developer['_sa_instance_state']

        if dev_id in developers:
            if task_idx not in tasks_ids:
                tasks_ids.append(task_idx)
                developers[dev_id]['estimated_points'] += task['estimated_points']
            developers[dev_id]['actual_times_sum'] += actual_time['actual_time']

        else:
            tasks_ids.append(task_idx)

            developers[dev_id] = developer
            developers[dev_id]['estimated_points'] = task['estimated_points']
            developers[dev_id]['actual_times_sum'] = actual_time['actual_time']

    developers = list(developers.values())
    return developers

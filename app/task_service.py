def get_task_values(query):
    tasks = {}
    story_actual_time = 0
    for row in query:
        task = row[0].__dict__
        actual_time = row[1].__dict__
        key_id = task['task_id']
        story_id = task['story_id']
        if key_id in tasks:
            if actual_time['actual_time']:
                tasks[key_id]['actual_times'].append(actual_time)
                tasks[key_id]['actual_times_sum'] += actual_time['actual_time']
                # story_actual_time += actual_time['actual_time']
        else:
            tasks[key_id] = task
            if actual_time['actual_time']:
                tasks[key_id]['actual_times'] = [actual_time]
                tasks[key_id]['actual_times_sum'] = actual_time['actual_time']
            else:
                tasks[key_id]['actual_times'] = []
                tasks[key_id]['actual_times_sum'] = 0
    tasks = tasks.values()
    return tasks
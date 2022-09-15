def summarize_developers(query):
    developers = {}
    for row in query:
        task = row[0].__dict__
        task['estimated_points'] = task['estimated_points'] if task['estimated_points'] else 0
        # print(row[0].dict)
        actual_time = row[1].__dict__
        actual_time['actual_time'] = actual_time['actual_time'] if actual_time['actual_time'] else 0
        # print(row[1].dict)
        developer = row[2].__dict__
        dev_id = developer['id']
        if '_sa_instance_state' in developer:
            del developer['_sa_instance_state']

        if dev_id in developers:
            developers[dev_id]['estimated_points'] += task['estimated_points']
            developers[dev_id]['actual_times_sum'] += actual_time['actual_time']

        else:
            developers[dev_id] = developer
            developers[dev_id]['estimated_points'] = task['estimated_points']
            developers[dev_id]['actual_times_sum'] = actual_time['actual_time']


    developers = list(developers.values())
    print(developers)
    return developers

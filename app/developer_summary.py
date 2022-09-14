def summarize_developers(query):
    developers = {}
    for row in query:
        task = row[0].__dict__
        task['estimated_points'] = task['estimated_points'] if task['estimated_points'] else 0
        # print(row[0].__dict__)
        actual_time = row[1].__dict__
        # print(row[1].__dict__)
        developer = row[2].__dict__
        # print(row[2].__dict__)
        dev_id = developer['id']
        if dev_id in developers:
            if actual_time['actual_time']:
                developers[dev_id]['actual_times_sum'] += actual_time['actual_time']
                developers[dev_id]['estimated_points'] += task['estimated_points']
        else:
            developers[dev_id] = developer
            if actual_time['actual_time']:
                developers[dev_id]['actual_times_sum'] = actual_time['actual_time']
                developers[dev_id]['estimated_points'] = task['estimated_points']
            else:
                developers[dev_id]['actual_times_sum'] = 0
                developers[dev_id]['estimated_points'] = 0

    developers = developers.values()
    print(developers)
    return developers
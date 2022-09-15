def get_story_values(query):
    stories = {}
    for row in query:
        story = row[0].__dict__

        if '_sa_instance_state' in story:
            del story['_sa_instance_state']

        if row[2]:
            task = row[1].__dict__
            actual_time = row[2].__dict__
            story_id = story['id']
            # print(row[0], row[1], row[2])

            if '_sa_instance_state' in task:
                del task['_sa_instance_state']
            if '_sa_instance_state' in actual_time:
                del actual_time['_sa_instance_state']

            if story_id in stories:
                if actual_time['actual_time']:
                    stories[story_id]['actual_times_sum'] += actual_time['actual_time']
            else:
                stories[story_id] = story
                if actual_time['actual_time']:
                    stories[story_id]['actual_times_sum'] = actual_time['actual_time']
                else:
                    stories[story_id]['actual_times_sum'] = 0
        else:
            story_id = story['id']
            stories[story_id] = story
            stories[story_id]['actual_times_sum'] = 'Unknown'
    stories = list(stories.values())
    print(stories)
    return stories
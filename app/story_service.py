def get_story_values(query):
    stories = {}
    for row in query:
        story = row[0].__dict__
        if row[2]:
            task = row[1].__dict__
            actual_time = row[2].__dict__
            story_id = story['id']
            if story_id in stories:
                if actual_time['actual_time']:
                    stories[story_id]['actual_times_sum'] += actual_time['actual_time']
                    stories[story_id]['estimated_time'] = story['estimated_time']
            else:
                stories[story_id] = story
                if actual_time['actual_time']:
                    stories[story_id]['actual_times_sum'] = actual_time['actual_time']
                    stories[story_id]['estimated_time'] = story['estimated_time']
                else:
                    stories[story_id]['actual_times_sum'] = 0
                    stories[story_id]['estimated_time'] = 0
        else:
            story_id = story['id']
            stories[story_id] = story
            stories[story_id]['actual_times_sum'] = 'Unknown'
    stories = stories.values()
    return stories
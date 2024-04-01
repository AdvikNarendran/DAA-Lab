def activity_selection(activities):
    activities.sort(key=lambda x: x[1])    
    selected_activities = [activities[0]]
    last_activity_finish_time = activities[0][1]
    
    for activity in activities[1:]:
        start_time, finish_time = activity
        if start_time >= last_activity_finish_time:
            selected_activities.append(activity)
            last_activity_finish_time = finish_time
    
    return selected_activities


activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
selected_activities = activity_selection(activities)
print("Maximum number of activities performed:", len(selected_activities))
print("Selected activities:", selected_activities)

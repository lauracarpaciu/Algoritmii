# greedy
# activites
#
# for activity in activites:
#     if activity
activities=[
     {"start":1,
           "finish":2},
    {"start": 3,
    "finish": 4},
{"start":6,
           "finish":8},
{"start":9,
           "finish":12},
    {"start": 9,
     "finish": 12}
]

def acitvityPlanner(activities):
    sortedActivities=activities
    lastFinishTime=0
    counter=0
    for activity in sortedActivities:

        if activity.get("start") >> lastFinishTime:
            counter +=1
            lastFinishTime = activity.get("finish")


    return counter


print(acitvityPlanner(activities))








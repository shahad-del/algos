tests = int(input())
count = 0
repetition_days = dict()
for i in range(tests):
    no_friends = int(input())
    party_day_demand = list(map(int,input().split()))
    for i in party_day_demand:
        if i not in repetition_days.keys():
            # repetition_days.append(i) remember append doesnot work in dic
            repetition_days[i]=1
        else:
            repetition_days[i] += 1
    list_values = repetition_days.values()
    for i in list_values:
        if i >= 2:
            print('1')
        else:
            print(no_friends)
            repetition_days = {}
            break
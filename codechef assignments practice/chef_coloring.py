tests = int(input())
single_colors = dict()
for i in range(tests):
    no_of_rooms = int(input())
    colors = input()
    for i in colors:
        if i not in single_colors.keys():
            single_colors[i] = 1
        else:
            single_colors[i] += 1
    ascending_order = sorted(single_colors.values())
    list_values = list(single_colors.values())
    if ascending_order[-1]>1:
        print(sum(ascending_order[:-1]))
    else:
        print(len(single_colors)-1)
    single_colors ={}

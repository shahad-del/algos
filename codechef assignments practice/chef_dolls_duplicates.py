test = int(input())
results ={}
count = 0
for i in range(test):
    number_dolls = int(input())
    types_dolls = list (map(int,input().split(' ')))
    for i in types_dolls:
        if i not in results.keys():
            results[i] = 1
        else:
            results[i] = results[i]+1
key_list = list(results.keys())
val_list = list(results.values())
for i in val_list:
    if i % 2 != 0:
        position = val_list.index(i)
        print(key_list[position])
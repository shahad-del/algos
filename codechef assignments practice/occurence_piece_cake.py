test = int(input())
letters = dict()
output = []
for i in range(test):
    # results = []
    str1 = input()
    for i in str1:
        if i not in letters.keys():
            letters[i] = 1
        else:
            letters[i] += 1
    values = sorted(letters.values())
    if values[-1] == sum(values[:-1]):
        output.append('yes')
    else:
        output.append('no')
    letters.clear()
        # output.append(results)
for  i in output:
        print(i)


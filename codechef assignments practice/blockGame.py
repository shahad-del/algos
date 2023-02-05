tests = int(input())
results = []
for i in range(tests):
    n = input('your no.:')
    k = n[::-1]
    if n == k:
        results.append('wins')
    else:
        results.append('loses')
# print(results)
for i in results:
    print(i)
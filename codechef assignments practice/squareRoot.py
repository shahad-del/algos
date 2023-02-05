import math
tests = int(input())
results = []
for i in range(tests):
# n = 25 ** 0.5
# print(n)
    n = int(input())
    k = math.sqrt(n)
    results.append(k)
for results in results:
    print(results)
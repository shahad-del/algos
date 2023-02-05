tests = int(input())
results = []
for i in range(tests):
    a,b = map(int,input().split())
    if 1 <= tests <= 1000 and 1 <= a <= 10000 and 1 <= b <= 10000:
    #   if 1 <= a,b <= 10000:
        x = a % b
        results.append(x)
    else:
        break
for results in results:
    print(results)

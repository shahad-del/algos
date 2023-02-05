tests = int(input())
results = []
for i in range(tests):
    n = int(input())
    digits = [int(x) for x in str(n)]
    m = (sum(digits))
    results.append(m)
for results in results:
    print(results)

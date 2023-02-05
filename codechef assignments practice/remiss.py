tests = int(input())
results = []
for i in range(tests):
    guard1,guard2 = map(int,input().split())
    soln = []
    if guard1< guard2:
        soln.append(guard1)
    else:
        soln.append(guard2)
    max_times = guard1+guard2
    soln.append(max_times)
    results.append(soln)
for x in results:
    
    print(f'{x[0]} {x[1]}')
    # print(x)

print(results)
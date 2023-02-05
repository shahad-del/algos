tests = int(input())
results = []
for i in range(tests):
    a,b,c = map(int,input().split())
    if a + b + c == 180:
       ans = 'yes'
       results.append(ans)
    else:
        ans = 'no'
        results.append(ans)
for x in results:
    print(x)
        
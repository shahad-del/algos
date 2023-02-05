tests = int(input())
results = []
for i in range(tests):
    factorial = 0
    collection = []
    times,number = map(int,input().split())
   
    for i in range(times):
        for i in range(1,int(number+1)):
            factorial = factorial +i
            collection.append(factorial)
        # print(collection[-1])
        number = (collection[-1])
        factorial = 0
    results.append(number)
for i in results:
     print(i)
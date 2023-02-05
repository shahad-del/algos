tests = int(input())
results = []
for i in range(tests):
    numbers = input('type your number')
    some = '4' 
    count = numbers.count(some)
    # print(count)
    results.append(count)
for results in results:
    print(results)
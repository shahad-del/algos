tests = int(input())
results = []
for i in range(tests):
    number_of_numbers = int(input())
    numbers = map(int,input().split())
    y = sorted(numbers)
    z = y[0]+ y[1]
    # print(y)
    # print(z)
    results.append(z)
for i in results:
    print(i)
tests = int(input())
results = []
second_largest = []
for i in range(tests):
    numbers = map(int,input().split())
    k = sorted(numbers, reverse = True)
    second_largest.append(k[1])
    results.extend(numbers) #append both is applicable
for ans in second_largest:
    print(ans)
    
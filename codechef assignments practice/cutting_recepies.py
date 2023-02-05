tests = int(input())
results = []
for i in range(tests):
    numbers = map(int,input().split())
z = list(numbers)    
y = sorted(z[1:])
x = y[0]
print(y)
all_numbers_divisible =True
for i in y:   
    if i % x != 0:
        all_numbers_divisible = False
        break
if all_numbers_divisible:
    for i in y:
        print(i//x, end = ' ')
        # print(output)
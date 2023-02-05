tests = int(input())
count = 0
results = []
square_numbers = []
for i in range(tests):
    numbers = int(input())
    for i in range(1,numbers+1):
        if i * i<= numbers:
            square_numbers.append(i * i)
        else:
            break
    for i in range(1,len(square_numbers)+1): 
        if numbers - square_numbers[-i]>= 0:
            count += 1
            numbers = numbers - square_numbers[-i]
            if numbers == 0:
                break
    results.append(count)
    count = 0
for i in results:
    print(i)

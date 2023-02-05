count = 0
tests = int(input())
for i in range(10):

    for i in range(tests):
        user_number = int(input())
        if user_number % 10 == 0:
            print(count)
        elif (user_number *2)% 10 == 0:
            count +=1
            print(count)
        else:
            print('-1')

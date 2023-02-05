tests = int(input())
count = 0
numbers = 0
str2 = []
for i in range(tests):
    str1 = input()
    for i in str1:
        if i == '0':
            count += 1
        else:
            numbers += 1
    for i in str1:
        if count == numbers:
            # if i == '0':
            #     i = '1' 
            print('no')
            
            break
        elif numbers == 1:
            # if i == '1':
            #     i = '0'
                print('yes')
                print(str1)
                
                break
        elif count == 1 :
            print('yes')
            break
        else:
            print('no')
            break
    count = 0
    numbers = 0

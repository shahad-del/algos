
def getMaxAlternatingLength(cur_sign, nums):
    count = 1
    for n in nums:
        if(cur_sign == 'p'):
            if n < 0:
                count+= 1
                cur_sign = 'n'
            else:
                break
        elif(cur_sign == 'n'):
            if n >= 0:
                count+= 1
                cur_sign = 'p'
            else:
                break
    return count

tests = int(input())
count = 0
for i in range(tests):
    number_of_int = int(input())
    numbers = list(map(int,input().split()))

    answers = []
    for pos,digit in enumerate(numbers):
        cur_sign = 'p' if digit >= 0 else 'n'
        if(pos == len(numbers)-1):
            answers.append(1)
        else:
            answers.append(getMaxAlternatingLength(cur_sign, numbers[pos+1:]))

    for n in answers:
        print(n, end=' ')

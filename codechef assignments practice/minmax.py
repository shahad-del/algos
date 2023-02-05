tests = int(input())
num_to_add= []
result = []
for i in range(tests):
    no_of_int= int(input())
    numbers= list(map(int,input().split()))
    arrange = sorted(numbers)
    for i in range(1,len(numbers)):
        num_to_add.append(arrange[0])
    result.append(sum(num_to_add))
    num_to_add = []
for i in result:
    print(i)

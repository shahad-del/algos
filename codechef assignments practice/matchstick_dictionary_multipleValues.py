number_sticks = {7:[6,8],6:[0,9],5:[2,3,5],4:[4],3:[7],2:[1]}
tests = int(input())
final_result= []
for i in range(tests):
    a,b = map(int,input().split())
    add = a+b
    z = [int(i) for i in str(add)]
    another_sticks_list = []
    for i in z:
        for key,val in number_sticks.items():
            if i in val:
                another_sticks_list.append(key)
    count = 0
    for i in another_sticks_list:
        add_it = i + count
        count = add_it
    final_result.append(count)
for i in final_result:
    print(i)




    
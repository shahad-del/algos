tests = int(input())
results = []
for i in range(tests):
    n,k = map(int,input().split())
    amounts_withdrawl = list(map(int,input().split()))
    output =[]
   
    for i in amounts_withdrawl:
        if (k - i) >= 0:
            remaining_money = k -i
            x ='1'
            output.append(x)
            k = remaining_money
        elif (k - i) < 0 :
            y ='0'
            output.append(y)
    results.append(output)

for i in results:
    print(*i,sep ='')

tests = int(input())
for i in range(tests):
    x,y= map(int,input().split())
    curNum = x + y
    while True:
        isvalid = True

        for i in range(2,int(curNum)):
            if curNum % i == 0:
                isvalid = False
                break

        if isvalid:
            break
        
        curNum = curNum+1

print('no. to add',curNum - (x+y), curNum)
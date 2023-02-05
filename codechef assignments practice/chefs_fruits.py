tests = int(input())

for i in range(tests):
    a,o, g = list(map(int,input().split()))
    if g >= 1:
           currentNo = 'a' if a < o else 'o'
           for i in range(g,0,-1):
               if currentNo == 'a':
                   a = a+1
                   currentNo = 'o'
               else:
                   o = o+1
                   currentNo = 'a'
           print(a-o)

                



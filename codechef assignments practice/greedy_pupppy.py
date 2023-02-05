tests = int(input())
for i in range(tests):
   coins,people = map(int,input().split())
   print(coins % people)
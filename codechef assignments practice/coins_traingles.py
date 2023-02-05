# tests = int(input())
# n = int(input())
# for i in range(tests):
#     for i in range(n):
#         x =print(i * '*')
#     if n<6:
#         print('2')
#     elif n>=6 and n<10:
#         print('3') 
    
try:
    t=int(input())
    for i in range(t):
            n = int(input())
            count=0
            i=1
            while(count<=n):
                   count=i*(i+1)//2
                   i+=1
            print(i-2)
except EOFError:
    pass
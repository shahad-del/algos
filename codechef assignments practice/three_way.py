from math import sqrt
tests = int(input())
for i in range(tests):
    R = int(input())
    x , y = map(int,input().split()) #location of chef
    x1,y1 = map(int,input().split()) #location of head server
    x2,y2 = map(int,input().split()) #location of sous-chef
    a = sqrt(abs(x-x1)**2 +abs(y - y1)**2)
    b = sqrt(abs(x -x2)**2 +abs(y-y2)**2)
    c = sqrt(abs(x1 -x2)**2+abs(y1-y2)**2)
    if (a<=R and b>R and c>R) or (a>R and b<=R and c>R) or (a>R and b>R and c<=R) or (a>R and b>R and c>R) :
        print(("no"))
    else:
        print("yes")
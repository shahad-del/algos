tests = int(input())
for i in range(tests):
    a, b, c,d= map(int,input().split())
    if a == b and c == d or(a == c and b ==d) or (b ==c and a ==d):
        print('yes')
    else:
        print('no')
            
tests = int(input())
RESULTS = []
for i in range(tests):
    A,B,N = list(map(int,input().split()))
    for i  in range(1,N+1):
        if i % 2 != 0:
           A = A*2
        else:
            B = B*2
    if A >B:
        RESULTS.append(A//B)
    else:
        RESULTS.append(B//A)
for items in RESULTS:
    print(items)
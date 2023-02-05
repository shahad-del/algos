tests = int(input())
for i in range(tests):
    limak,bob = map(int,input().split())
    greater =limak if limak>bob else bob
    eaten_limak = []
    eaten_bob = []
    for i in range(1,greater + 2):
        if i % 2 != 0:
            eaten_limak.append(i)
        else:
                eaten_bob.append(i)
        if sum(eaten_limak)>limak:
            print('bob wins')
            break
        elif sum (eaten_bob)>bob:
            print('limak wins')
            break
        
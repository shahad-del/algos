while True:    
    soldiers = int(input())
    # for i in range(soldiers):
    weapons = map(int,input().split())
    k = list(weapons)
    even = []
    odd = []
    for i in k:
        
        if i % 2 == 0:
            even.append(i)
        elif i % 2 != 0:
            odd.append(i)
    # print(even)
    # print(odd)  
    if i == even:
        print('READY FOR BATTLE')
    elif i == odd:
        print('NOT READY FOR BATTLE')
    elif len(even)>len(odd):
        print('READY FOR BATTLE') 
    # elif sum(even)<sum(odd):
    elif len(even)<len(odd):
        print('NOT READY FOR BATTLE')
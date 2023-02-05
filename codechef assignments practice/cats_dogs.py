tests = int(input())
for i in range(tests):
    cats,dogs,legs= map(int,input().split())
    if (cats*4) + (dogs*4)== legs:
       print('yes')
    elif (cats == dogs or cats == dogs*2) and legs == dogs *4:
        print('yes')
    elif (dogs*2>cats)  and legs == dogs *4:
        print('yes')
    # elif dogs*2>cats:
    #     print('yes')
    
    else:
        print('no')
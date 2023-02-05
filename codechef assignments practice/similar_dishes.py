tests = int(input())
count = 0
for i in range(tests):
    ingredients_first_dish= list(map(str,input().split()))
    ingredients_second_dish= list(map(str,input().split()))
    for i in ingredients_first_dish:
        if i in ingredients_second_dish:
            count += 1
    if count>=2:
        print('similar')
    else:
        print('dissimilar')
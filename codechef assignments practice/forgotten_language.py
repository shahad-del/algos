tests = int(input())
result =[]
for i in range(tests):
    output = []
    Collection_modern_words = list()
    no_forgotten_words,no_modern = map(int,input().split())
    forgotten_words = input().split(' ')
    for i in range(no_modern):
        modern_words = input().split(' ')
        Collection_modern_words.append(modern_words)
    flat_list = []
    for sublist in Collection_modern_words:
        for item in sublist:
            flat_list.append(item)
    for i in forgotten_words:
        if i in flat_list[1:]:
            output.append('yes')
        else:
            output.append('no')
    result.append(output)
for i in result:
    print(*i)
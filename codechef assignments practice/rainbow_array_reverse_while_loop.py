tests = int(input())
collection=[]

for i in range(tests):
    no_int = int(input())
    array = list(map(int,input().split()))
    for i in array:
        if i == 7:
            index_7 = array.index(7)
            cut=array[:index_7+1]
            collection = cut
            break
        else:
            print('no')
# i = len(collection) - 1
# while i >= 0 :
#     print(collection[i]) 
#     i -= 1
another_collection = collection[::-1]
print(another_collection)
for final_list in another_collection[1:]:
    collection.append(final_list)
print(*collection)
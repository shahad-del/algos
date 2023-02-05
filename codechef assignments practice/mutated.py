tests = int(input())
no_of_dolls,characteristics = map(int,input().split())
dna_dolls = map(int,input().split())
last_list = []
count = 0
for i in range(tests):
    for i in  dna_dolls:
        new_list =characteristics + i 
        last_list.append(new_list)
for i in last_list:
    if i % 7 == 0:
        count += 1
print(count)
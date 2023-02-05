rounds = int(input())
# winner = []
leadp1 = []
leadp2 = []
for i in range(rounds):
    p1,p2 = map(int,input().split())
    if p1>p2:
        k = p1 - p2
        leadp1.append(k)
    else:
        l = p2 - p1
        leadp2.append(l)
if leadp1>leadp2:
    print('p1',sum(leadp1))
else:
    print('p2',sum(leadp2))       

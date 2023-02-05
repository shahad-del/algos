tests = int(input())
# area_rectangle= []
final_result = []
for i in range(tests):
    area_rectangle= []
    no_tab,budget = list(map(int,input().split()))
    # h,w,p=list(map(int,input().split()))
    for i in range(no_tab):
        h,w,price=list(map(int,input().split()))
        if price<=budget:
            area_rectangle.append(h*w)
    if len(area_rectangle)>0:
        arrange_ascending_order = sorted(area_rectangle)
        final_result.append(arrange_ascending_order[-1])
    else:
        final_result.append('no tablet')
    area_rectangle = []
for i in final_result:
    print(i)



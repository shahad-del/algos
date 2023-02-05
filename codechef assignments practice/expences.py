tests = int(input())
final_amount = []
for i in range(tests):
    quantity,expenses = map(int,input().split())
    if quantity > 1000:
        total_bill = quantity * expenses
        discount = total_bill - (total_bill * (10/100))
        final_amount.append(discount)
    else:
        total_bill = quantity * expenses
        final_amount.append(total_bill)
for x in final_amount:
    print(x)
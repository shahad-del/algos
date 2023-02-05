tests = int(input())
Available_currencies = [1, 2, 5, 10, 50, 100][::-1]
total_no_notes = []
for i in range(tests):
    smallest_notes = []
    customers_cash = int(input())
    for notes in Available_currencies:
        if customers_cash % notes == 0:
            x =(customers_cash // notes)
            smallest_notes.append(x)
            break
        elif customers_cash % notes != 0:
            x = customers_cash // notes
            y = customers_cash % notes
            customers_cash = y
            smallest_notes.append(x)
    rs = 0
    for i in smallest_notes:
        rs += i
    total_no_notes.append(rs)


for min_notes in total_no_notes:
    print(min_notes)    
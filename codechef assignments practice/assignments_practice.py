charge = 0.50
while True:
    Amount = int(input('your balance is:'))
    withdrawl = int(input('Amount you want to withdraw '))
    if withdrawl <= Amount and withdrawl > 0:
        isvalid = False
        if withdrawl % 5 == 0:
                new_amount = (Amount - (withdrawl + charge))
                new_amount == Amount
                isvalid = True
                print(new_amount)
                # break
     
        else:
            print(Amount)
            break
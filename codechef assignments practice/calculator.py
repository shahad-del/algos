while True:
    number_a = int(input())
    number_b = int(input())
    operator = input()
    if operator == '/':
        print(number_a/number_b)
    elif operator == '*':
        print(number_a*number_b)
    elif operator == '+':
        print(number_a+number_b)
    elif operator == '-':
        print(number_a-number_b)
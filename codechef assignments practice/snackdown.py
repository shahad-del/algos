tests = int(input())
snackdown = ['2010','2015','2016','2016','2017','2019']
for i in range(tests):
    user_input = input()
    if user_input in snackdown:
        print('hosted')
    else:
        print('not hosted')
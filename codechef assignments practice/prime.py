tests = int(input())
results = []
for i in range(tests):
    number = int(input())
    isPrime = True 
    for  i in range(2,number):
      if number % i == 0:
        isPrime = False
        break

    if isPrime:
      print('Prime')
    else:
      print('not prime')
    
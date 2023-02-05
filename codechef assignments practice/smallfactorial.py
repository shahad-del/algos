results = []
tests = int(input())
for i in range(tests):
        n = input("Enter a number: ")
        factorial = 1
        if int(n) >= 1:
            for i in range (1,int(n)+1):
                factorial = factorial * i
            print("Factorail of ",n , " is : ",factorial)
            results.append(factorial)
for results in results:
    print(results)
# print(results)
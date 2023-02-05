
# def numbers(x,y):
#     if x < y:
#         small = x
#     else:
#         small = y
#     for i in range(1, small + 1):
#         if ((x % i == 0) and (y % i == 0)):
#             hcf = i
#     return hcf
# print(numbers(24,28))

def number(x,y):
    if x>y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x == 0) and (greater % y == 0)):  
          lcm = greater
          break
        greater += 1
    return lcm
print(number(12,14))
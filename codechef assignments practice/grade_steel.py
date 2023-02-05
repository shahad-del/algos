hardness, carbon_content, tensile_strength = map(float,input().split())
x =hardness>50 
y = carbon_content<0.7 
z = tensile_strength>5600
is_valid = True
# for i in range(2):
if all((x,y,z)):
    is_valid = False
    print('10')
elif x and y == True and z == False:
    # is_valid = False
    print('9')
elif y and z == True and x == False:
    print('8')
elif x and z == True and y == False:
    print('7')
elif x == True or y == True or z == True:
    print('6')
elif (x,y,z) != True:
    print('5')





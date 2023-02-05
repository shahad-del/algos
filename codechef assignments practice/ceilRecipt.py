# # def menu_price():
# eel_flavored = 	1
# eel_bones =	2
# eel_livers = 4
# grated_radish =	8
# egg_custard_eel = 16
# eel_fried_small = 32
# eel_fried_large = 64
# grilled_eel = 128
# eel_curry= 256
# grilled_eel_rice = 512
# deluxe_grilled =1024
# eel_course=	2048
menu=[2048,1024,512,256,128,64,32,16,8,4,2,1] [::-1]
print(menu)
trials = int(input())
for i in range(trials):
    favorite_int = int(input())
    if favorite_int in menu:
        print(menu.count(favorite_int))
    elif favorite_int == any
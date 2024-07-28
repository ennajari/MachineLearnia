import random
my_list = [chr(i) for i in range(ord('A'), ord('I')+1)]

x = input("ⵙⴽⴻⵛⵎ ⴰⵙⴻⴽⴽⵉⵍ ⴳⴰⵔ A ⴷ ⵏ :")
while True:
    if random.choice(my_list) != x:
        print("ⵎⴰⵞⵞⵉ ⴷ ⴰⵡⴰⴷⴻⵎⵏⵏⵉ")
        x = input("ⵙⴽⴻⵛⵎ ⴰⵙⴻⴽⴽⵉⵍ ⴳⴰⵔ A ⴷ ⵏ: ")
    else:
        print("ⴰⵢⵓⵣ! ⵜⴻⵔⴱⴻⵃⴻⴹ!")
        break
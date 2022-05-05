myfoodOrder = []
counter = 0

product_list = ['Cappuccino', 'Latte', 'Moccalatte', 'Frappuccino', 'Green tea']

print("Welcome to Joe's Coffee Shop")
print("Here is a list of items we currently have:", product_list, end = "\n")
print('''Press [1] for main menu options
         Press [0] to exit 
''')



order = input("Please can i take your order? ").lower()
if order == "no":
    exit()

else:
    print("Thank you")

nextOrder = True

while nextOrder == True:
    foodOrder = input("Please choose an item: ").title()
    if foodOrder == "Cappuccino":
        myfoodOrder.append(product_list[0])
        counter += 1

    elif foodOrder == "Latte":
        myfoodOrder.append(product_list[1])
        counter += 1

    elif foodOrder == "Moccalatte":
        myfoodOrder.append(product_list[2])
        counter += 1

    elif foodOrder == "Frappuccino":
        myfoodOrder.append(product_list[3])
        counter += 1

    elif foodOrder == "Green Tea":
        myfoodOrder.append(product_list[4])
        counter += 1
    else:
        print("Not in the menu")

    finished = input("Have you finished ordering (yes/no): ").lower()
    if finished == "no":
        nextOrder = True
    else:
        nextOrder = False
    
y = 0

print("Here is your order", end = "\n")
print(" ")
print("*******************")

while y < counter:
    print(myfoodOrder[y])
    y += 1
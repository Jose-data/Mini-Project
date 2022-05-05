print("Welcome to Joe's Coffee Shop")

product_menu = [" Product list: [1] Cappuccino, [2] Latte, [3] Mocca, [4] Frappuccino"]

main_menu = ["For product list press [1], Other options press [2] "]

def exit():
    while True:
        customer_input = int(input("Enter 1 for [Main menu] or 0 to exit app: "))
        if customer_input == 1:
            pass
            print(main_menu)
            
        else:
            break
exit()

def add_new_product():
    add_product = 0
    for add_product in range(2):
        add_product = input("Add new products to the list: ")
        product_menu.append(add_product)
    print("Added products include: ", product_menu)

def product_menu():
    while True:
        print(product_menu)
        choice = int(input("Choose the products that you want: "))
        if choice == 1:
            print("You picked: Cappuccino")

        elif choice == 2:
            print("You picked: Latte")

        elif choice == 3:
            print("You picked: Mocca")

        elif choice == 4:
            print("You picked: Frappuccino")

        else:
            print("Item not found!")
        
        more_items = (input("Do you want to order more items?")).lower()
        if more_items == 'yes':
            pass
        else:
            break
#product_menu()



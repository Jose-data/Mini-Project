demo_list = ["Banana","Mango", "Apple"]
product_list = ["1. product list", "2. Add item", "3 Update item", "4. Delete item"]
mainMenu = ['0. Exit App', '1. Product Menu','2. Couriers menu']
courier_list = []

def display(arg_list):
    for i,product in enumerate(arg_list):
         print(product)

def remove_product():
    selected_product = int(input("Please select the product to delete: "))
    demo_list.pop(selected_product)
    print(demo_list)

def update_list():
    selected_product = int(input("Please select the product to update: "))
    update_user_input = input("Enter updated item: ")
    demo_list[selected_product] = update_user_input
    display(demo_list)

def Start():
    display(mainMenu)
    
    main_menu_choice = input("Enter choice from 0 to 2: ")
    if main_menu_choice in ("0","1","2"):
        if main_menu_choice == "0":
            print("Exiting App")

        elif main_menu_choice == "1":
            main_menu()

        elif main_menu_choice == "2":
            print(courier_list)

def main_menu():
    while True:
        display(product_list)
        choice = input("Enter choice from 0 to 4: ")
        if choice in ('0','1', '2', '3', '4'):
            if choice == '0':
                break
            elif choice == '1':
                display(demo_list)
            
            elif choice == '2':
              add_product = input("Please add product: ")
              demo_list.append(add_product)
            
            elif choice == '3':
                update_list()
            
            elif choice == '4':
                remove_product()
            
            elif choice == '5':
                display(courier_list)
            
        else:
            print("Invalid Input")
Start()


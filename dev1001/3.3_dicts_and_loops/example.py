shopping_list = []

while True:
    option = input("""
1. Add Item 
2. View List  
3. Mark Item as Purchased  
4. exit
: """)

    match option:
        case "1":
            add_item = input("Enter item to add to shopping list: ").lower()
            if add_item in shopping_list:
                print("item already in list")
            else:
                shopping_list.append(add_item)
            input("Hit enter to view options again")
        case "2":
            if len(shopping_list) == 0:
                print("Your shopping list is empty")
                input("Hit enter to view options again")
            else:
                for x, i in enumerate(shopping_list):
                    print(f"{x + 1}. {i}")
                input("Hit enter to view options again")
        case "3": 
            purchased = input("Enter shopping list item to mark as purchased: ").lower()
            while purchased not in shopping_list:
                purchased = input("Please enter a valid item: ").lower()
            shopping_list.remove(purchased)
            input("Hit enter to view options again")
        case "4":
            print("Goodbye!")
            break
        case _:
            print("Invalid option, please try again")
            input("Hit enter to view options again")
shopping_list = []

while True:
    print("\n")
    print("1. Add item")
    print("2. View list")
    print("3. Mark item as purchased (remove)")
    print("4. Exit")

    choice = input("Enter your choice (1, 2, 3, or 4): \n")

    match choice:

        case '1':
            item = input("What item would you like to add to list: " + "\n")
            if item not in shopping_list:
                shopping_list.append(item)
                print("Item added!")
            else: 
                print("Item already in list, please try again!")
        case '2':
            if not shopping_list:
                print("Your shopping list is empty.")
            else:
                print("Your list:")
                print("-" * 30 + "\n")
                for index, item in enumerate(shopping_list):
                    print(f"{index + 1}. {item}")
        case '3':
            if not shopping_list:
                print("List is empty, nothing to remove")
            else:
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
                removed = input("Which item would you like to remove?: \n")
                if removed in shopping_list:
                    shopping_list.remove(removed)
                    print(f"{removed} has been removed from your list!")
                # removed = int(input("Which number would you like to remove: \n")) #This is for removing by number
                # if (removed-1) in range(len(shopping_list)):
                #     del shopping_list[removed-1]
                #     print("Item removed!")
                else: 
                    print(f"{removed} not in list. Please try again.")
        case '4':
            print("Goodbye!")
            break
        case _: 
            print("Invalid choice, please try again.\n")
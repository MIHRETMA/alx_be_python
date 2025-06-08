def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice == '1':
            int(choice)
            item = input("Enter item name: ").strip()
            shopping_list.append(item)
            pass
        elif choice == '2':
            int(choice)
            item = input("Enter item name: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item is not available in shopping list")
            pass
        elif choice == '3':
            int(choice)
            print(shopping_list)
            pass
        elif choice == '4':
            int(choice)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

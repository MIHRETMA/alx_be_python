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
        choice = input("Enter your choice: ")

        # Validate input
        if not choice.isdigit():
            print("Invalid choice. Please enter a number.")
            continue

        choice = int(choice)

        if choice == 1:
            item = input("Enter item name: ")
            shopping_list.append(item)
        elif choice == 2:
            item = input("Enter item name: ")
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item is not available in shopping list")
        elif choice == 3:
            print(shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

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

        # Validate if choice is a number
        if not choice.isdigit():
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item name: ").strip()
            if item:
                shopping_list.append(item)
        elif choice == 2:
            item = input("Enter item name: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                print("Item is not available in shopping list")
        elif choice == 3:
            print("Shopping List:", shopping_list)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

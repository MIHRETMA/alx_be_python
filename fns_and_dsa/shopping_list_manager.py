def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        # Validate if choice is a number and within the expected range
        try:
            choice = int(choice)  # Convert input to integer
            if choice < 1 or choice > 4:
                print("Invalid choice. Please enter a number between 1 and 4.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter item name: ").strip()
            if item:
                shopping_list.append(item)
                print(f'"{item}" added to the shopping list.')
        elif choice == 2:
            item = input("Enter item name: ").strip()
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'"{item}" removed from the shopping list.')
            else:
                print("Item not found in the shopping list.")
        elif choice == 3:
            print("Shopping List:", shopping_list if shopping_list else "Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()

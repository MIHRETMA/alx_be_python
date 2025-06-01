num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

oper = input("Choose the operation (+, -, *, /):")


add = num1 + num2
diff = num1 - num2
prod = num1 * num2
quo = num1 / num2

match oper:
    case '+':
        print(f"The result is {add}")
    case '-':
        print(f"The result is {diff}")
    case '*':
        print(f"The result is {prod}")
    case '/':
        if num2 != 0:
            print(f"The result is {quo}")
        else:
            print("Cannot divide by zero.")
    case _:
        print("Invalid operation")
  

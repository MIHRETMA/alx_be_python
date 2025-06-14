def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        den = float(denominator)
        if den == 0:
            print("Error: Cannot divide by zero.")
        else:
            print(f"The result of the division is {num / den}.")
    except ValueError:
        print("Error: Please enter numeric values only.")

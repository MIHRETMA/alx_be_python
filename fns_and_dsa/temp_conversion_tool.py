FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

temp = int(input("Enter the temperature to convert: "))
spec = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")


def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32)*FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius)*CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit




if spec == 'F':
    c = convert_to_celsius(temp)
    print(f"{temp}°F is {c}°C")
elif spec == 'C':
    f = convert_to_fahrenheit(temp)
    print(f"{temp}°C is {f}°F")
else:
    print("Invalid temperature. Please enter a numeric value.")

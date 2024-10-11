#FUNCTIONS AND LOOPS
#FUNCTION DEFINITIONS
def sum(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Number cannot be divided by 0."
    return x / y

#DISPLAY MENU FOR FUNCTIONS
print("CALCULATOR:")
print("Select function:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#INPUT FOR FUNCTION
choice = input("Enter function number: ")

#INPUT FOR NUMBERS
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#FUNCTION CALLING
if choice == '1':
    print(f"The result is: {sum(num1, num2)}")
elif choice == '2':
    print(f"The result is: {subtract(num1, num2)}")
elif choice == '3':
    print(f"The result is: {multiply(num1, num2)}")
elif choice == '4':
    print(f"The result is: {divide(num1, num2)}")
else:
    print("PLEASE CHOOSE A NUMBER BETWEEN 1 AND 4")

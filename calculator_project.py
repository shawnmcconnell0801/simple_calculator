import cmath

history = []

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def square(a):
    return a ** 2

def cube(a):
    return a ** 3

def sqrt(a):
    return cmath.sqrt(a)

print("=" * 35)
print("         CALCULATOR")
print("=" * 35)

while True:

    print("\nMenu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Square Root")
    print("8. View History")
    print("9. Clear History")
    print("10. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice.")
        continue

    if choice == 1:
        try:
            x, y = map(float, input("Enter two numbers: ").split())
            result = add(x, y)
            print(f"Result: {result}")
            history.append(f"{x} + {y} = {result}")
        except ValueError:
            print("Invalid input.")

    elif choice == 2:
        try:
            x, y = map(float, input("Enter two numbers: ").split())
            result = subtract(x, y)
            print(f"Result: {result}")
            history.append(f"{x} - {y} = {result}")
        except ValueError:
            print("Invalid input.")

    elif choice == 3:
        try:
            x, y = map(float, input("Enter two numbers: ").split())
            result = multiply(x, y)
            print(f"Result: {result}")
            history.append(f"{x} × {y} = {result}")
        except ValueError:
            print("Invalid input.")

    elif choice == 4:
        try:
            x, y = map(float, input("Enter two numbers: ").split())

            if y == 0:
                print("Cannot divide by zero.")
            else:
                result = divide(x, y)
                print(f"Result: {result}")
                history.append(f"{x} ÷ {y} = {result}")

        except ValueError:
            print("Invalid input.")

    elif choice == 5:
        try:
            x = float(input("Enter a number: "))
            result = square(x)
            print(f"Result: {result}")
            history.append(f"{x}² = {result}")
        except ValueError:
            print("Invalid input.")

    elif choice == 6:
        try:
            x = float(input("Enter a number: "))
            result = cube(x)
            print(f"Result: {result}")
            history.append(f"{x}³ = {result}")
        except ValueError:
            print("Invalid input.")

    elif choice == 7:
        try:
            x = float(input("Enter a number: "))
            result = sqrt(x)
            print(f"Result: {result}")
            history.append(f"√{x} = {result}")
        except ValueError:
            print("Invalid input.")

    elif choice == 8:

        if len(history) == 0:
            print("No calculations yet.")

        else:
            print("\nCalculation History")
            print("-" * 25)

            for calculation in history:
                print(calculation)

    elif choice == 9:
        history.clear()
        print("History cleared.")

    elif choice == 10:
        print("Exiting calculator. Goodbye!")
        break

    else:
        print("Invalid choice.")

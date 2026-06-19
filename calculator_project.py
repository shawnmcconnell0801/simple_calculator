import cmath
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
def square(a):
    return a ** 2
def cube(a):
    return a ** 3
def sqrt(a):
        return cmath.sqrt(a)

#menu block
print("CALCULATOR")

while True:
    print("Menu")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square")
    print("6. Cube")
    print("7. Square Root")
    print("8. Exit")
    
    try:
        choice=int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice.")
        continue
    
    
    if choice==1:
        x, y = map(int, input("Enter the numbers with a space: ").split())
        print(add(x, y))

    elif choice==2:
        x, y = map(int, input("Enter the numbers with a space: ").split())
        print(subtract(x, y))
    
    elif choice==3:
        x, y = map(int, input("Enter the numbers with a space: ").split())
        print(multiply(x,y))
    
    elif choice==4:
        x, y = map(int, input("Enter the numbers with a space: ").split())
        print(divide(x,y))
    
    elif choice==5:
        x=int(input("Enter the number"))
        print(square(x))
    
    elif choice==6:
        x=int(input("Enter the number"))
        print(cube(x))
    
    elif choice==7:
        x=int(input("Enter the number"))
        print(sqrt(x))

    elif choice==8:
        print("Exiting calculator. Goodbye!")
        break
    
    else:
        print("Invalid Choice")
    

    



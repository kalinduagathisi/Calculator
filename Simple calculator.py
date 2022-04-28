def add (x,y):
    return(x+y)

def sub (x,y):
    return(x-y)

def mul (x,y):
    return(x*y)

def div (x,y):
    return(x/y)

def mod (x,y):
    return (x%y)

print("Welcome to the calculator program..")
print()
print("Please select from the following menu which operation do you want to access..")
print("Enter (1) for addition")
print("Enter (2) for subtraction")
print("Enter (3) for multiplication")
print("Enter (4) for division")
print("Enter (5) for modulus")
print("Enter (6) to quit")
print()

while True:

    option = input("Please select from the above menu-> ")
    print()

    if option == "1":
        num_1 = float(input("Enter number 01: "))
        num_2 = float(input("Enter number 02: "))
        print(num_1, "+", num_2, "=", add(num_1,num_2))
        print()
        
    elif option == "2":
        num_1 = float(input("Enter number 01: "))
        num_2 = float(input("Enter number 02: "))
        print(num_1, "-", num_2, "=", sub(num_1,num_2))
        print()
        
    elif option == "3":
        num_1 = float(input("Enter number 01: "))
        num_2 = float(input("Enter number 02: "))
        print(num_1, "*", num_2, "=", mul(num_1,num_2))
        print()
        
    elif option == "4":
        num_1 = float(input("Enter number 01: "))
        num_2 = float(input("Enter number 02: "))
        print(num_1, "/", num_2, "=", div(num_1,num_2))
        print()
        
    elif option == "5":
        num_1 = float(input("Enter number 01: "))
        num_2 = float(input("Enter number 02: "))
        print(num_1, "%", num_2, "=", mod(num_1,num_2))
        print()
        
    elif option == "6":
        break
        
    else:
        print("Invalid choise entered..!")
        print()
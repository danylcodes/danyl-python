def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b


print("Simple Python Calculator")
print("Operations:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n5. Exit")

while True:
    key=int(input("Enter the operation number:"))
    if key>=1 and key <=5:
        if key==1:
            print("\nAddition:")
            a=int(input("Enter first value:"))
            b=int(input("Enter second value:"))
            print(f"{a}+{b}={add(a,b)}\n")
        if key==2:
            print("\nSubtraction:")
            a=int(input("Enter first value:"))
            b=int(input("Enter second value:"))
            print(f"{a}-{b}={sub(a,b)}\n")
        if key==3:
            print("\nMultiplication:")
            a=int(input("Enter first value:"))
            b=int(input("Enter second value:"))
            print(f"{a}*{b}={mul(a,b)}\n")  
        if key==4:
            print("\nDivision:")
            a=int(input("Enter first value:"))
            b=int(input("Enter second value:"))
            if b==0:
                print("Cannot divide by zero.\n")
            else:
                print(f"{a}/{b}={div(a,b)}\n")
        if key==5:
            print("\nExiting Calculator...")
            break
    else:
        print("Please enter a valid choice.")

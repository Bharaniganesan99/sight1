

def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y

def div(x,y):
    return x/y

print("select option")
print("1.Add")
print("2.Subtract")
print("3.Multiplication")
print("4.Division")

while True:
    choice = input("Enter the choice (1/2/3/4):")

    if choice in ('1','2','3','4'):
        num1=float(input("enter the first number:"))
        num2=float(input("enter the second number"))

    if choice == '1':
        print(num1,"+",num2,"=",add(num1,num2))

    elif choice == '2':
        print(num1,"-",num2,"=",sub(num1,num2))

    elif choice == '3':
        print(num1,"*",num2,"=",mul(num1,num2))

    elif choice == '4':
        print(num1,"/",num2,"=",div(num1,num2))
    else:
        print("Invalid input")
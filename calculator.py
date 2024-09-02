a=int(input("Enter the 1st number:"))
b=int(input("Enter the 2nd number:"))
print("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n")
while(True):
    choice=int(input("Enter your choice:"))
    if choice==1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice==3:
        print(a*b)
    elif choice==4:
        if b!=0:
            print(a/b)
        else:
            print("Denominator should not be zero")
    else:
        print("Invalid choice")

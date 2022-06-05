age1=int(input("Enter the age of 1st person: "))
age2=int(input("Enter the age of 2nd person: "))
age3=int(input("Enter the age of 3rd person: "))
if age1>age2:
    if age1>age3:
        print("age1 is youngest ")
    else:
        print("age1 is older ")
elif age2>age3:
    if  age2>age1:
        print("age2 is youngest ")
    else:
        print("age2 is older ")

elif age3>age1:
    if age3>age2:
        print("age3 is youngest")
    else :
        print("age3 is older")

# making matrix by concating two list:

M=[]
l1=[]
for i in range(4):
    x=int(input("Enter the elements->"))
    l1.append(x)


l2=[]
for j in range(4):
    x=int(input("Enter the elements->"))
    l2.append(x)
    
M=l1+l2
print("matrix will be",M)

    
#making matrix by using loop-----------------------------------------------------------                                  



M=[]
for i in range(2):
    l1=[]
    for i in range(4):
        x=int(input("Enter the elements->"))
        l1.append(x)
    M.append(l1)
print(M)




                                 

#perfect program for user defined matrix:-------------------------------------
M=[]
rows=int(input("enter the no of rows:"))
cols=int(input("enter the no of columns:"))
for i in range(rows):
    print("nEW Row")
    l1=[]
    for i in range(cols):
        x=int(input("Enter the elements->"))
        l1.append(x)
    M.append(l1)
print(M)

for i in range(rows):
    for j in range(cols):
        print(M[i][j],end="   ")
    print()    

#transpose of the matrix:---------------------------------------------------

M=[]
rows=int(input("enter the no of rows:"))
cols=int(input("enter the no of columns:"))
for i in range(rows):
    print("nEW Row")
    l1=[]
    for i in range(cols):
        x=int(input("Enter the elements->"))
        l1.append(x)
    M.append(l1)
print(M)

for i in range(rows):
    for j in range(cols):
        print(M[i][j],end="   ")
    print()

print("Transpose of the matrix")
for i in range(cols):
    for j in range(rows):
        print(M[j][i],end="     ")
    print()    
    


















                                   
        

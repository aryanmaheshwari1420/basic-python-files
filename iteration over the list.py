'''L=[10,12,13,11,25,52]
index=int(input("enter the index:"))
s=0
for i in range(len(L)):
    if i<=index:
        s=s+L[i]
print(s)        



L=[10,12,13,11,25,52]
value=int(input("enter the value upto which u want to sum:"))
s=0
for i in range(len(L)):
    if L[i]!=value:
        s=s+L[i]
    else:
        break
print(s)


m=[]
for i in range(2):
    l=[]
    for i in range(4):
        x=int(input())
        l.append(x)
    m.append(l)
print(m)    

m=[]
rows=int(input("enter the no of rows:"))
columns=int(input("enter the no of columns:"))
for i in range(rows):
    l=[]
    for i in range(columns):
        x=int(input("enter the elments u want ot put:"))
        l.append(x)
    m.append(l)
print(m)    

'''
m1=[]
rows=int(input("enter the no fo rows:"))
columns=int(input("enter the no of columns:"))
for i in range(rows):
    l1=[]
    for j in range(columns):
        x=int(input())
        l1.append(x)
    m1.append(l1)
print(m1)

m2=[]
rows=int(input("enter the no fo rows:"))
columns=int(input("enter the no of columns:"))
for i in range(rows):
    l2=[]
    for j in range(columns):
        x=int(input())
        l2.append(x)
    m2.append(l2)
print(m2)

for i in range(rows):
    for j in range(columns):
        print(m1[i][j+m2[i][j],end=" ")
    print()    
        






























    

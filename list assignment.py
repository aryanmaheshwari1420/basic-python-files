#1

'''lst=["welcome","freshers",2020,1,"sem"]
for i in range(len(lst)):
    print(lst[i],i,sep=",")


    

#2

l1=list(map(int, input("Enter a multiple value: ").split(",")))
c=0
for i in range(l1+1):
    if i%2==0:
        c=c+i
        print("sum of even is",c )


#3

l=[1,2,3,1,2,4,5]
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print(l2)


#5

l1=['a',3,'i','g','l','a','u',2,1]
for j in l1:
    if j=='a' or j=='e' or j=='i' or j=='o' or j=='u':
        l1.remove(j)
print(l1)


#6
l = [1,2,3,4,5,6]
for i in range(len(l)):
    print(l[i], end=',')
     

#ans is - 1,2,3,4,5,6

#7

l = [1,2,3,4,5,6]
for i in range(len(l)):
     print(l[i], end=',')
     if(l[i]==4):
         break

#ans - 1,2,3,4

        
#8
        
l = [1,2,3,4,5,6]
for i in range(len(l)):
    if(l[i]==4):
        break
    print(l[i], end=',')

#ans- 1,2,3    



#9

    
l = [1,2,3,4,5,6]
for i in range(len(l)):
    if(l[i]==4):
        continue
    print(l[i], end=',')'''


#ans- 1,2,3,5,6


#10

for i in range(10):
    pass
    print(I, end='')    
      
#ans- error 
     















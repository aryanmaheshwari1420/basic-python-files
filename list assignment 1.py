#1

l1=[1,2,5,7,8]
sum1=0
for i in l1:
    sum1=sum1+i
print("THE SUM IS :",sum1)






#2


a1=[1,5,8,"HElLO","bye"]
k=a1*3
print(k)



#3


l=[1,8,7,1,9,11,15]
k=max(l)
print(k)




#4

l=[1,8,1,8,4,8,4,]
k=min(l)
print(k)



#5

l1=[1,2,8,1,5,1,5,1,6,9,2,]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)
print(l2)


#6

l=[]
if not l:
    print("list is empty")


#7

original_list=[10,5,2,1,0,5]
new_list=list(original_list)
print(original_list)
print(new_list)


#8


l1=[10,20,30,40,50]
l2=[50,60,70,80,90]
for i in l1:
    for j in l2:
        if i==j:
            print("true")
        else:
            print("false")
    


#9


l1=[4,5,8,1,6,9,1,6]
l2=[]
for i in l1:
    if i%2!=0:
        l2.append(i)
print("New list is--> ",l2)



#10
ls=[]
for i in range(1,31):
    ls.append(i**2)    
print("the first 5 elements of the list is-->",ls[:5])
print("the last 5 elements of the list is-->",ls[-5:])



#11
ls=[]
for i in range(1,31):
    ls.append(i**2)
print("square of list except the first 5 elements:--->",ls[5:])    





#12


ls=[5,8,12,15,"Hello","BYE"]
for i in range(len(ls)):
    print(i ,end=" ")
    print(ls[i])


#13


l1=[1,5,4,8,1,6]
l2=[1,4,8,1,5,4]
final_list=l1+l2
print(final_list)


#14

l=[10,20,4,45,99]
l.sort()
print("largest second number is:",l[-2])



#15


list1=[1,5,10,5,10,10,2]
frequency=int(input("enter number to find the frequency : "))
count=0
for i in list1:
    if (i==frequency):
        count=count+1
print("frequency=",count)

                 or
                 
list1=[1,5,10,5,10,10,2]
frequency=int(input("enter number to find the frequency : "))
k=list1.count(frequency)
print("frequency=",k)

#16

a=[1,5,4,8,7,9]
lower_range=int(input("enter the lower range:"))
upper_range=int(input("enter the upper range:"))
count=0
for i in a:
    if lower_range<i and i<upper_range:
        
        count+=1
print(count)        
  
#17

ls1=[1,5,6,"hello","bye"]
ls2=[5,9,2,6,"hello","tata"]
for i in ls1:
    if i in ls2:
        print(i)


#18

lst=[11,33,50]
for i in lst:
    print(i,end="")


#19

list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']    
for i in list1:
    if i not in list2:
        print("missing values in list second",i)
for i in list2:
    if i not in list1:
        print("additional values in second list",i)

  


#20

ls1=["red","orange","green","blue","white"]
ls2=["black","yellow","green","blue"]
for i in ls1:
    if i not in ls2:
        print("color1-color2",i,end=",")
for i in ls2:
    if i not in ls1:
        print("color2-color1",i,end=",")

  
#21

ls1=[1,3,5,7,9,10]
ls2=[2,4,6,8]
ls1[-1:]=ls2
print(ls1)

#22

element=int(input("enter the element-->"))
ls=list(map(int,input().split()))
if element in ls:
    print("yes element is exists")
else:
    print("no element do not exists")

#25

num=int(input("enter the number:"))
ls=[7,1,9,8,7,3,9,2,]
for i in ls:
    if i>num:
        print(i,end="")
        
     
#26

ls1=[1,1,2,3,4,4,5,1]
x=int(input("enter the index of that element u want to escape"))
k=ls1.pop(x)
print(k)
print(ls1)

                or
                

ls1=[1,1,2,3,4,4,5,1]
k=int(input("enter the kth element"))
for i in range(len(ls1)):
    if i==k:
        ls1.remove(ls1[i])
print(ls1)


#27

l1=[1,1,2,3,4,4,5,1]
index=int(input("enter the index:"))
element=int(input("enter the element:"))
l1.insert(index,element)
print(l1)



#28


l1=['red', 'black', 'white', 'green', 'orange']
ls_1=[]
ls_1.append(l1[::2])
print(ls_1)


#29


new_list=[]
product=1
ls=[10, 20, 30, 40, 20, 50, 60, 40]
for i in ls:
    if i not in new_list:
        new_list.append(i)
for i in new_list:
    product*=i
print(product)



#30

l1=[2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]
lr=int(input("enter the lower range:"))
lb=int(input("enter the upper range:"))
sum=0
for i in l1:
    if lr<=i and i<lb:
        print(i)
        sum+=i
print(sum)        

    
#31


ls=[1, 3, 5, 7, 4, 1, 6, 8]
result=[]
for i in ls:
    if i%2==0:
        
        result.append(i)
        break
for j in ls:
    
    if j%2!=0:
        
        result.append(j)
        break
print(result)    








    

    


        

        


    
    





        
     

        
        
        
        




     

  
    
 



    
    













        







    


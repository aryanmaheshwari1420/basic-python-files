'''#1.wap to create empty list and add all all the natural nos from 1 to n
l=[]
n=int(input("enter the no upto which u want to add"))
for i in range(1,n+1):
            l.append(i)
print(l)

#2. WAP ot create an empty list and add all the even no from 2 to 50
l=[]
n=int(input("enter the no upto which u want to add"))
for i in range(1,n+1):
    if i%2==0:
        l.append(i)
print(l)

#3. WAP to create an empty list and add all the odd numbers from 1 to 49

l=[]
n=int(input("enter the no upto which u want to add"))
for i in range(1,n+1):
    if i%2!=0:
        l.append(i)
print(l)

#4. WAP to create an empty list and add all the palindrome numbers from 100 to 1000

l=[]
n=int(input("Enter the number: "))
for n in range(n,1000):
    t=n
    s=0
    while n>0:
        rem=n%10
        s=s*10+rem
        n=n//10
    if t==s:
        print(t)
        l.append(t)
print(l)

#5 WAP to create an empty list and add all the armstrong numbers from 100 to 50000

l=[]

print(l)

# WAP to create an empy list and add all the prime numbers from 1 to 100

l=[]
for i in range(101):
    if i

# WAP to create the list of n integers taken from user.

lst=[]
n=int(input("enter the number upto which want to :"))
for i in range(1,n+1):
    ele=int(input())
    lst.append(ele)
print(lst)    

# WAP to create the list of n elements (heterogeneous) taken from user.
'''

lst=[]
n=int(input("enter the number upto which want to :"))
for i in range(1,n+1):
    ele=input()
    lst.append(ele)
print(lst)

    























        

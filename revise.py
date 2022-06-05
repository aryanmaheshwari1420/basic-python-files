'''t=(1,5,7,1,6,6,1,6)
print("old tuple",t)
s=list(t)
new_tuple=[]
for i in s:
    if i not in new_tuple:
        new_tuple.append(i)
t=tuple(new_tuple)
print("new_tuple",t)
        


i=1
while i<11:
    print(i)
i=i+1


l=[4,5,61,0,2]
element=int(input("Enter the element:"))
if element in l:
    print("found")
    k=l.index(element)
    print("At index",element,k)
else:
    print("not found")

'''
s="python"
for i in range(len(s)):
    print(i,s[i])

l=["gla","mathura","university"]

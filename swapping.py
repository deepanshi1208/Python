list=[]
num=int(input("Enter the no of elements: "))
for i in range(1,num+1):
   n=int(input("Enter the element: "))
   list.append(n)
a=int(input("Enter the location of. to be swapped:"))
b=int(input("Enter the location it needs to be swapped with:"))

temp=list[a]
list[a]=list[b]
list[b]=temp
print(list)
list=[]
x=int(input("Enter the number of elements:"))
for i in range(1,x+1):
   n=int(input("enter elements:"))
   list.append(n)
   print("ORIGINAL LIST", list)
list.reverse()
print("REVERSED LIST:",list)
x=int(input("Enter the starting value: \n"))
y=int(input("Enter the end value: \n"))

for val in range(x,y+1):
   if val>1:
      for n in range(2,val):
         if (val%n)==0:
            break
      else:
       print(val)
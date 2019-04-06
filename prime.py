n=int(input("Enter a number: \n"))
for i in range(2,n):
   if n%i==0:
     print("The number is a NOT a PRIME NO")
     break
else:
   print("The number is a PRIME NO.")
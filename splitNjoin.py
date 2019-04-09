m=input("ENTER A STRING: ")
d=m.split()
print (d)
n=int(input("Enter the location where the list needs to start from"))

for i in range(0,n):
    first=d[0]
    for j in range (0,len(d)-1):
      d[j]=d[j+1]
    d[len(d)-1]=first
f=" ".join(d)
print(f)
arr=[1,2,3,4,5]
print(arr)
d =int(input("Enter the number by which it is to be rotated:"))


for i in range (0,d):
    first=arr[0]
    for j in range (0,len(arr)-1):
        arr[j]=arr[j+1]
    arr[len(arr)-1]=first

print("NEW ARRAY IS: ",arr)
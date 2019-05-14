def bubble(list):
    for i in range(len(list)-1,0,-1):
        for j in range (i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=[5,23,65,7,9,4,2]
bubble(list)
print(list)
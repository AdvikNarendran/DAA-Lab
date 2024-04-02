arr = [10,1,2,4,13, 9, 5] 
l=[]
s=0
for i in range(len(arr)-1):
    for j in range(0, len(arr)-1-i):
        if arr[j]>arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
            l.append((arr[j+1],arr[j]))
            s+=1
print(arr)
print(l)
print(s)

arr = [1, 7, 4, 2, 8, 6, 3, 9, 5] 
for i in range(len(arr)-1):
    for j in range(0, len(arr)-1-i):
        if arr[j]>arr[j+1]:
            t=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=t
print(arr)
print("The maximum product is ",(int(arr[len(arr)-1])*int(arr[len(arr)-2])))

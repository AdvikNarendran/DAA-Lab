def logn(arr, K):
    n = len(arr)
    flag=False
    for i in range(n):
        for j in range(i,n):
            
            if arr[i] + arr[j] == K:
                print((arr[i],arr[j]))
                flag=True
    return flag

def nlogn(arr, K):
    arr.sort()
    n=len(arr)

    for i in range(n):
        for j in range(i,n):
            if arr[i] + arr[j] == K:
                print((arr[i],arr[j]))
                flag=True
    return flag

arr=[8,4,1,6]
K=12
print("LogN solution")
if not logn(arr, K):
    print("no sum")
print("NLogN solution")
if not nlogn(arr, K):
    print("no sum")
import time
import matplotlib.pyplot as plt
import random

def bin(a,l,h,s):
    flag=0
    while(l<=h):
        mid=int((l+h)/2)
        print(mid)
        if(a[mid]==s):
            flag=1
            break
        elif(a[mid]<s):
            l=mid+1
        elif(a[mid]>s):
            h=mid-1
    if(flag!=1):
        return(-1,time.time())
    else:
        return(mid,time.time())

def lin(a,s):
    tic=time.time()
    flag=0
    for i in range(len(a)):
        if a[i]==s:
            flag=1
            break
    if(flag==1):
        return(i,time.time())
    else:
        return(-1,time.time())    
    

a=[random.randint(1, 10000) for iter in range(1000)]
print(a)


X=[]
X1=[]
Y1=[]
Y=[]
for i in range(0,5):
    tic=time.time()
    s=int(input("Enter the number to be searched : "))
    x,y=bin(sorted(a),0,len(a),s)
    [print("element is present at ",x, " of sorted array") if x!=-1 else print("Element not present")]

    x1,y1=lin(a,s)
    [print("element is present at ",x1," of unsorted array") if x1!=-1 else print("Element not present")]
    Y.append(y-tic)
    Y1.append(y1-tic)

print(X,Y,X1,Y1,sep="\n")

plt.plot([1,2,3,4,5], Y)

plt.xlabel("N")
plt.ylabel("Time")
plt.title("Binary Search")
plt.show()

plt.plot([1,2,3,4,5], Y1)
plt.title("Linear")
plt.xlabel("N")
plt.ylabel("Time")
plt.show()

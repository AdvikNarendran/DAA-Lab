import time
import matplotlib.pyplot as plt

def sumrec(n):
    if n>1:
        n1,y=sumrec(n-1)
        return n+n1, y
    else:
        return 1,time.time()
def sum(n):
    tic=time.time()
    s=0
    for i in range(1,n+1):
        s+=i
    toc=time.time()
    print(toc-tic)
    print(toc)
    print(tic)
    return s, (toc-tic) 
X=[]
X1=[]
Y=[]
Y1=[]
for i in range(10,100,10):
    tic=time.time()
    x,y=sumrec(i)
    X.append(i)
    Y.append(y)
    print("sum by recursion with N as ",i," is ",x," with a time of ",(tic-y))
    x,y=sum(i)
    X1.append(i)
    Y1.append(y)
    print("sum with N as ",i," is ",x," with a time of ",(y))

plt.plot(X, Y, label="Recursion")
plt.plot(X1, Y1, label="Iterative")
plt.xlabel("N")
plt.ylabel("Time")
plt.title("Performance Comparison")
plt.legend()
plt.show()

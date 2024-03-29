n=input("enter a number\t")
s=""
k=1
f=0
for i in range(len(n)-1,-1,-1):
    
    if(k==4 and f==0):
        s=','+s
        k=0
        f=1
    elif(k==3 and f!=0):
        s=','+s
        k=0
    s=n[i]+s
    k+=1
print(s)
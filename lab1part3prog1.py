def sum(a,s):
    sums=[]
    k=0
    for i in a:
        for j in a[k+1:]:
            if (i+j) == s:
                sums.append((i,j))
        k+=1
    print("Input array: ",a)
    print("Sum: ",s)
    if sums:
        for i in range(len(sums)):
            if i==len(sums)-1:
                print("Pair Found  ",sums[i])
            else:
                print("Pair Found  ",sums[i],"\nor")
    else:
        print("Pair Not Found")

a=[8,7,2,5,3,1]
s=10
sum(a,s)
print("\n\n")
b=[5,2,6,8,1,9]
s=12
sum(b,s)
def split(a):
    z=[]
    o=[]
    l=[]
    for i in a:
        if i==0:
            z.append(i)
        else:
            o.append(i)
    
    for i in z:
        l.append(i)

    for i in o:
        l.append(i)
    return l

a=[0,1,0,1,0,0,1,1,1,0]
print(a,"\n")
b=split(a)
print(b)
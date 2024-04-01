def merge(a):
    a.sort(key=lambda x: x[0])  
    interval=[]
    lb=a[0][0]
    hb=a[0][1]
    b=()
    for i in a[1:]:
        if(hb>i[0]):
            if(i[1]>hb):

                b=(lb,i[1])
                hb=i[1]
        else:
            interval.append(b)
            lb=i[0]
            hb=i[1]
            b=(i)
    if b:
        interval.append(b)
    
    return interval

a=[(1, 4), (2, 5), (7, 8), (6, 9)]
print(merge(a))
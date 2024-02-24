import time
import random

def bubble(a):
    start = time.time()
    swap=0
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if(a[j]>a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
                swap+=1
    end = time.time()
    s1=(end-start)  * 10**3
    print("The time of execution of bubble sort is :", s1,"ms")
    print(f"number of  swaps = {swap}")
    return a,s1

def selection(a):
    start = time.time()
    min=a[0]
    swap=0
    for  i in range(len(a)):
        min=a[i]
        index=i
        for j in range(i+1,len(a)):
            if(a[j]<min):
                min=a[j]
                index=j
        a[i],a[index]=a[index],a[i]
        swap+=1
    end = time.time()
    s1=(end-start) * 10**3
    print("The time of execution of selection sort is :", s1,"ms")
    print(f"number of  swaps = {swap}")

def insertion(a):
    swaps = 0
    start = time.time()

    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and key < a[j]:
            a[j + 1] = a[j]
            j -= 1
            swaps += 1  # Increment the swaps count

        a[j + 1] = key

    end = time.time()
    s1 = (end - start) * 10**3
    print("The time of execution of insertion sort is:", s1, "ms")
    print("The number of swaps made during insertion sort is:", swaps)



a=[random.randint(1, 100) for iter in range(10000)]
bubble(a)
selection(a)
insertion(a)
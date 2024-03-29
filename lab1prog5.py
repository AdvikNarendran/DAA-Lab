def rev(a):
    if len(a)==1:
        return a
    else:
        s=a[len(a)-1]+rev(a[:len(a)-1])
        return s
    
s=input("enter word\t")
print("entered word is ",s)
print("reversed word is ", rev(s))
if(s.lower()==rev(s).lower()):
    print("palindrome")
else:
    print("not palindrome")
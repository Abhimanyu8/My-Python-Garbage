def bs(l,val):
    low=0
    high=n-1
    while high>low:
        midval=low+((high-low)//2)
        if l[midval]==val:
            return midval
        if l[midval]>val:
            high=midval-1
        elif 1[midval]<val:
           low=midval+1
        else:
            print("Value not present")

    return midval

l=[]
n=int(input("Enter the length of the list :"))
for k in range(n):
    x=int(input("Enter Element :"))
    l.append(x)
print("original list :")
print(l)
l.sort()
print("the sorted list is:",l)
e=int(input("enter the element you want to search:"))
print("Value present at index",bs(l,e))
       
        
        
              

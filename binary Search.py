def bsearch(l,low,high,val):
    if high<low:
        return None
    else:
        midval=low+((high-low)//2)  
        if l[midval]>val:
            return bsearch(l,low,midval-1,val)
        elif l[midval]<val:
            return bsearch(l,midval+1,high,val)
        else:
            return midval
#main
l=[]
n=int(input("enter the length of the list :"))
for k in range(n):
    x=int(input("enter element:"))
    l.append(x)
print("Original list :")
l.sort()
print("the sorted list is",l)
e=int(input("Enter the Element you seek to search :"))
print(e,"found at index",bsearch(l,0,n,e))
      


            

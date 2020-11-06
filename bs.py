def Binary_Search(sequence, item, LB, UB):
    if LB>UB:
        return -5
# return any negative value
    mid=int((LB+UB)/2)
    if item==sequence[mid]:
        return mid
    elif item<sequence[mid]:
        UB=mid-1
        return Binary_Search(sequence, item, LB, UB)
    else:
        LB=mid+1
        return Binary_Search(sequence, item, LB, UB)

    
L=eval(input("Enter the elements in order: "))
n=len(L)
element=int(input("Enter the element that you want to search :"))
found=Binary_Search(L,element,0,n-1) 
if found>=0:
    print(element, "Found at the index : ",found)
else:
    print("Element not present in the list")

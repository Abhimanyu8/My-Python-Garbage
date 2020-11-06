x=int(input("Enter how many nos. you want : "))
s=[]
for o in range(x):
    n=int(input("Enter the element : "))
    s.append(n)
print("Original List: ",s)


for j in range(x):
    for i in range(x-1):
        if s[i]<s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]

print("sorted list: ",s)
    

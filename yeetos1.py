s=[]
x=int(input("Enter list size : "))
for o in range(x):
    n=int(input("enter number : "))
    s.append(n)
print("original list :",s)
for j in range(x):
    for i in range(x-1):
        if s[i]<s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
print(s)

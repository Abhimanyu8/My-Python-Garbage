s=[]
x=int(input("list ka size bata MC :"))
for o in range(x):
    n=int(input("Please type some number :"))
    s.append(n)
for j in range(x):
    for i in range(x-1):
        if s[i]<s[i+1]:
            s[i],s[i+1]=s[i+1],s[i]
print("\n ee le tera sorted list :",s)
print("200 rupaya lagega")

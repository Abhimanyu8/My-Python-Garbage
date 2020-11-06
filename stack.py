def push():
    n=int(input("Enter any no"))
    stack.append(n)
    top=len(stack)-1
def pop():
    if stack==[]:
        print("stack empty")
    else :
        item=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        print("the deleted value is",item)
def display():
    if stack==[]:
        print("stack empty")
    else:
        top=len(stack)-1
        print(stack[top],"<-- top")
        for a in range(top-1,-1,-1):
            print(stack[a])

stack=[]
top=None
ch='y'
while ch=='y':
    print("stack opperation")
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.Exit")
    c=int(input("enter your choice"))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        display()
    elif c==4:
        exit(0)
    else:
        print("wrong choice")
    ch=input("do you wish1 to continue (y/n) ")


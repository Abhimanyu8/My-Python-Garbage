def push():
    n=int(input("enter any no"))
    stack.append(n)
    top=len(stack)-1
def pop():
    if stack==[]:
         print("stack empty")
    else:
        item=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        print("the deleted value is ", item)
def display():
    if stack==[]:
        print("stack empty")
    else:
        top=len(stack)-1
        print(stack[top],"<--top")
        for a in range(top -1,-1,-1):
            print(stack [a])
            
stack=[]
top=None
ch='y'
while ch=='y':
    print("stack operation")
    print("1.push")
    print("2.pop")
    print("3.display")
    print("4.exit")
    c=int(input("enter your selection"))
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
    ch=input("Do you wish to continue(y/n)")


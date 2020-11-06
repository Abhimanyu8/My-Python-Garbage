def push():
    n=int(input("enter any number\n"))
    stack.append(n)
    top=len(stack)-1
def pop():
    if stack==[]:
        print("error:stack is empty")
    else:
        item=stack.pop()
        if len(stack)==0:
            top=None
        else:
            top=len(stack)-1
        print("the deleted value is :",item)
def display():
    if stack==[]:
        print("you have an empty stack")
    else:
        top=len(stack)-1
        print(stack[top],"<-- top") 
        for a in range (top-1,-1,-1):
            print (stack[a])

stack=[]
top=None
ch='y'
while ch=='y':
    print("stack operations")
    print("1> Push Values")
    print("2> Pop Values")
    print("3> Display Stack")
    c=int(input("Enter your choice :"))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        display()
    else:
        print("error! deleting system32")
    ch=input("Do you wish to continue?")

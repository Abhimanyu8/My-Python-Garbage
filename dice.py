from random import randint
import time

print("welcome to dice !")
print("this program lets you forget your dice at home if you manage to bring your computer")
num=None
ch='y'
while ch=='y':
    print("choose your roll")
    print("1) GO !!")
    print("2) exit")
    ch=int(input("enter your choice :\n"))
    if ch==1:
        for _ in range(1):
            num=randint(1,6)
        #random number generation.
        print("roll... roll...")
        time.sleep(1)
        #print after one second.
        print("shake...shake...")
        time.sleep(1)
        # print after one second.
        print(num,"!")
    elif ch==2:
        exit()
    else:
        print("wrong choice you dum dum! \n")
        print("choose again !")
    ch=input("Want to continue ? (y/n)")
    
           

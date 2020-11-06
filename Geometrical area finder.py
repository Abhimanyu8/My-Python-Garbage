import numpy as np
import time

def circlearea(r):
    res=2*np.pi*r
    return res
def squarearea(s):
    res=s*s
    return res
def rectarea(x,y):
    res=x*y
    return res
def trianglearea(b,h):
    res=0.5*b*h
    return res
def rhombusarea(d1,d2):
    res=0.5*d1*d2
    return res
def parallelarea(b,h):
    res=b*h
    return res
def spherearea(r):
    res=4*np.pi*r*r
    return res
def trapeziumarea(s1,s2,h):
    res=s1+s2
    res1=res*0.5*h
    return res1
    print("The area of your trapezium is",res1)
    
    
#_main_
ch='y'
while ch=='y':
    print(
        '''\t\t\t\t ***************************
           \t\t\t WELCOME TO AREA FINDER v0.5
           \t\t\t ***************************
           \t\t\t     Made by : Abhimanyu8
           \t\t\t(https://github.com/Abhimanyu8)''')
    time.sleep(1)
           
    print(''' Choose your computation:
          
          1.Circle
          2.Square
          3.Rectrangle
          4.Triangle
          5.Rhombus
          6.Parallelogram
          7.Sphere
          8.Trapezium
          (more comming soon !)'''#add More Funcions needed
        )
    ch=int(input("Enter your choice :"))
    if ch==1:
        print("You have choosen Circle\n")
        r=int(input("Enter the radius:"))
        print("The area of a circle with radius",r,"is",circlearea(r))
    elif ch==2:
        print("you have chosen square\n")
        s=int(input("Enter the length of side : "))
        print("The area of a square with side",s,"is",squarearea(s))
    elif ch==3:
        print("You have Choosen Rectrangle")
        l=int(input("Length = "))
        b=int(input("breadth= "))
        print("The area of your rectrangle is",rectarea(l,b))
    elif ch==4:
        print("You have Choosen Triangle")
        b=int(input("Base = "))
        h=int(input("Height= "))
        print("The area of your Triangle is",trianglearea(b,h))
    elif ch==5:
        print("You have Choosen Rhombus")
        d1=int(input("Diagonal 1 = "))
        d2=int(input("Diagonal 2 = "))
        print("The area of your Rhombus is",rhombusarea(d1,d2))
    elif ch==6:
        print("You have Choosen Paralleogram")
        b=int(input("Base = "))
        h=int(input("Height= "))
        print("The area of your Paralleogram is",parallelarea(b,h))
    elif ch==7:
        print("You have choosen Sphere\n")
        r=int(input("Enter the radius:"))
        print("The area of a sphere with radius",r,"is",spherearea(r))
    elif ch==8:
         print("You have Choosen Trapezium")
         s1=int(input("Side 1 = "))
         s2=int(input("Side 2 = "))
         h=int(input("Height = "))
         print("The area of your Paralleogram is",trapeziumarea(s1,s2,h))
        
#Space For Functions
        
    else:
        print("Wrong Choice")
    ch=input("Continue?(y/n)\n")
        
        
        














    

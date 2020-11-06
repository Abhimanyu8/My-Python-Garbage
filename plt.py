import mysql.connector as m
db=m.connect(host="localhost",user="root",passwd="  ",database="avi")
cr=db.cursor()
ch='y'
while ch=='y':
    _id=int(input("Enter the ID: "))
    n=input("Enter the name: ")
    r=int(input("enter the Roll No :"))
    val=[_id,n,r]
    sql="insert into avi(id,name,roll) values(%s,%s,%s)"
    cr.execute(sql,val)
    c=input("Do you wish to enter again ? y/n: ")

db.commit()




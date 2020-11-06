#!/usr/bin/python
import getpass
import string
import os
import pyttsx3
import mysql.connector
'''#initiating voice

s = pyttsx3.init()
s.setProperty('volume', 0.9)
s.setProperty('rate', 150)'''

# creating lists of users,their PINs and bank statements

users = ['user1', 'user2', 'user3']
pins = ['1111', '2222', '3333']
amounts = [1000, 2000, 3000]
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Micromax123",database="pyhtonproject")
mydb=mycursor()
sql="insert into bank(users,pin,balance) values(%s,%s,%s))"
val=[('user1','1111',1000),('user2','2222',2000),('user3','3333',3000)]
mycursor.executemany(sql,val)
mydb.commit()
print(mycursor.rowcount,"was inserted.")
count = 0
# while loop checks existence of the entered username
while True:
    '''s.say('please enter your username.')
    s.runAndWait()'''
    user = input("\nENTER THE USER NAME:")
    user = user.lower()
    if user in users:
        if user == users[0]:
            n = 0
        elif user == users[1]:
            n = 1
        else:
            n=2
        break
    else:
        print('-------------------------------')
        print('******************************')
        '''s.say('no bank user found with such name.')
        s.runAndWait()'''
        print('INVALID USERNAME')
        print('******************************')
        print('-------------------------------')

# comparing pin
while count < 3:
    print('--------------------------------')
    print('*******************************')
    '''s.say('PLEASE ENTER YOUR PIN')
    s.runAndWait()'''
    pin = str(getpass.getpass("PLEASE ENTER THE PIN:"))
    print('*******************************')
    print('--------------------------------')
    if pin.isdigit():
        if user == 'user1':
            if pin == pins[0]:
                break
            else:
                count += 1
                print('------------')
                print('************')
                '''s.say('the pin you entered is invalid.')
                s.runAndWait()'''
                print('INVALID PIN')
                print('************')
                print('-------------')
                print()

        if user == 'user2':
            if pin == pins[1]:
                break
            else:
                count += 1
                print('------------')
                print('************')
                '''s.say('the pin you entered is invalid.')
                s.runAndWait()'''
                print('INVALID PIN')
                print('************')
                print('------------')
                print()

        if user == 'user3':
            if pin == pins[2]:
                break
            else:
                count += 1
                print('------------')
                print('************')
                '''s.say('the pin you entered is invalid.')
                s.runAndWait()'''
                print('INVALID PIN')
                print('************')
                print('------------')
                print()
    else:
        print('----------------------')
        print('**********************')
        '''s.say('your pin consists of four digits.')
        s.runAndWait()'''
        print('PIN CONSISTS OF 4 DIGITS')
        print('**********************')
        print('----------------------')
        count += 1
# in case of pin-continuing or exiting
if count == 3:
    print('-------------------------------------')
    print('************************************')
    '''s.say('3 UNSUCCESSFUL ATTEMPTS,EXITING')
    s.say('YOUR CARD HAS BEEN LOCKED')
    s.runAndWait()'''
    print('3 UNSUCCESSFUL ATTEMPTS,EXITING')
    print('!!!!!YOUR CARD HAS BEEN LOCKED!!!!!')
    print('************************************')
    print('-------------------------------------')
    exit()
else:
    print('--------------------------------------')
    print('**************************************')
    '''s.say('LOGIN SUCCESSFUL')
    s.runAndWait()'''
    print('LOGIN SUCCESSFUL,CONTINUE')
    print('--------------------------------------')
    print()
    print('--------------------------------------')
    print('**************************************')
    '''s.say('welcome to ATM')
    s.runAndWait()'''
    print(str.capitalize(user[n]), 'welcome to ATM')
    print('**************************************')
    print('---------------------------ATM SYSTEM-----------------------------')
# MAIN MENU
while True:
    # os.system('clear')
    print('------------------------------------------')
    print('**********************************')
    '''s.say('you can choose form the following options.')
    s.runAndWait()'''
    response = input('SELECT FROM FOLLOWING OPTIONS:'
                     '\nStatement__(S)  \nWithdraw___(W)  \nLodgement__(L)'
                     '\nChange PIN_(P)  \nQuit______(Q) \n:').lower()
    print('**********************************')
    print('------------------------------------------')
    valid_responses = ['s', 'w', 'l', 'p', 'q']
    response = response.lower()
    if response == 's':
        print('------------------------------------------------------')
        print('*******************************************')
        p=str(amounts[n])
        '''s.say('YOU HAVE'+ p +'$ ON YOUR ACCOUNT.')
        s.runAndWait()'''
        print(str.capitalize(users[n]),'YOU HAVE', amounts[n], '$ ON YOUR ACCOUNT.')
        print('*******************************************')
        print('------------------------------------------------------')
    elif response == 'w':
        print('------------------------------------------------------')
        print('*******************************************')
        '''s.say('ENTER THE AMOUNT YOU WOULD LIKE TO WITHDRAW:')
        s.runAndWait()'''
        cash_out = int(input("ENTER THE AMOUNT YOU WOULD LIKE TO WITHDRAW:"))
        print('*******************************************')
        print('------------------------------------------------------')
        if cash_out%10 != 0:
            print('------------------------------------------------------')
            print('*******************************************')
            '''s.say('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10$ DOLLAR NOTES.')
            s.runAndWait()'''
            print('AMOUNT YOU WANT TO WITHDRAW MUST MATCH 10$ DOLLAR NOTES.')
            print('*******************************************')
            print('------------------------------------------------------')
        elif cash_out > amounts[n]:
            print('----------------------------------------------')
            print('*************************************')
            '''s.say('YOU HAVE INSUFFICIENT BALANCE')
            s.runAndWait()'''
            print('YOU HAVE INSUFFICIENT BALANCE!!')
            print('*************************************')
            print('----------------------------------------------')
        else:
            amounts[n] = amounts[n]-cash_out
            print('--------------------------------------------------')
            print('****************************************')
            print('YOUR NEW BALANCE IS:', amounts[n], '$')
            print('****************************************')
            print('--------------------------------------------------')
    elif response == 'l':
        print()
        print('-----------------------------------------------------------------------')
        print('*********************************************************')
        '''s.say('ENTER THE AMOUNT YOU WANT TO LODGE:')
        s.runAndWait()'''
        cash_in = int(input('ENTER THE AMOUNT YOU WANT TO LODGE:'))
        print('*********************************************************')
        print('-----------------------------------------------------------------------')
        print()
        if cash_in%10 != 0:
            print('---------------------------------------------------------------------')
            print('********************************************************')
            print('AMOUNT YOU WANT TO LODGE MUST MATCH 10$ NOTES.')
            print('********************************************************')
            print('---------------------------------------------------------------------')
        else:
            amounts[n] = amounts[n]+cash_in
            print('-------------------------------------------------')
            print('***************************************')
            print('YOUR NEW BALANCE IS', amounts[n], '$')
            print('***************************************')
            print('-------------------------------------------------')
    elif response == 'p':
        print('---------------------------------------------')
        print('************************************')
        '''s.say('enter your new pin.')
        s.runAndWait()'''
        new_pin = str(getpass.getpass('ENTER A NEW PIN:'))
        print('************************************')
        print('---------------------------------------------')
        if new_pin.isdigit() and new_pin != pins[n] and len(new_pin) == 4:
            print('------------------------------------------')
            print('**********************************')
            '''s.say('confirm your new pin.')
            s.runAndWait()'''
            new_pinc = str(getpass.getpass('CONFIRM NEW PIN:'))
            print('**********************************')
            print('------------------------------------------')
            if new_pin != new_pinc:
                print('---------------------')
                print('*****************')
                s.say('pin mismatch')
                s.runAndWait()
                print('PIN MISMATCH')
                print('*****************')
                print('---------------------')
            else:
                pins[n] = new_pinc
                print('NEW PIN SAVED.')
                s.say('new pin saved succesfully.')
                s.runAndWait()
        else:
            print('----------------------------------------')
            print('********************************')
            s.say('NEW MUST CONSIST OF 4 DIGIT AND \nAND MUST BE DIFFERENT TO THE PREVIOUS PIN.')
            s.runAndWait()
            print('NEW MUST CONSIST OF 4 DIGIT AND \nAND MUST BE DIFFERENT TO THE PREVIOUS PIN')
            print('********************************')
            print('----------------------------------------')
    elif response == 'q':
        exit()
    else:
        print('-----------------------')
        print('*******************')
        s.say('sorry your response is not valid.')
        s.runAndWait()
        print('RESPONSE NOT VALID')
        print('*******************')
        print('------------------------')


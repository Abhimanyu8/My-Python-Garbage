from time import sleep

def loadingloop(y):
    while y<=10:
        print("\033[92m Loading...\033[00m",y,"%")
        sleep(1)
        loadingloop(y=y+1)
    else:
        print("error_/usr/bin/metasploit dir not found")
        sleep(2)
        exit()
#main

x=int(input("enter app password : "))
if x==2:
    loadingloop(1)

''' DISCLAIMER : Avimanyu Dutta is not responsible for any
friendships or relationships getting burst. The script program 
user holds full responsibility '''

#Debug_Start
import os
os.environ['DISPLAY'] = ':0'
#Debug_End

import pyautogui, time
time.sleep(5) #Think of this is the detonator fuse . tweak it first !

#mayhem starts here :
f = open("beemovie_script.txt","r") #enter your fav payload here

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter") #Change this according to what yor app settings prefer .
    

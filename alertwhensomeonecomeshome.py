import sys
import subprocess
import os
from decouple import config

IP_NETWORK = config('IP Network')
IP_DEVICE = config('IP DEVICE')
proc = subprocess.Popen(['ping',IP_NETWORK], stdout=subprocess.PIPE)
while True:
    line = proc.stdout.readline()
    if not line:
        break
    connected_ip = line.decode('utf-8').split()[3]

    if connected_ip == IP_DEVICE:
        subprocess.Popen(['say','Pahi is leeching the network !!!'])
        #Can also be used to alert when some specific device connects 
        #to your network (alert when the said owner of the device comes home). 
        #In my case, it is my sister Pahi 

#Can improve on this by time.sleep() method to run 24 x 7 or to ring the doorbell as soon as
#someone connects to the wifi network if implemented on a raspberry pi
    

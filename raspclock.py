#Code Write on Python2

#Import
import threading
from time import sleep
from datetime import datetime

#Global Var
itstime = True

#Define methods
def DFprint_name(name):
    print(name)
    sleep(6)
    print_name.start()

def DFloopClock():
    print 'ALARM!'    
    sleep(2)
    loopClock.start()
    
#Start program
print_name = threading.Thread(target=DFprint_name, args=('marco',))
loopClock = threading.Thread(target=DFloopClock)

#Set alarm
I1 = raw_input('Set Alarm Time: ')
if len(I1) > 3:
    hour1 = I1[0:2]
    minute1 = I1[2:]
    print 'Alarm set for: %s:%s' % (hour1,minute1)
    
while itstime:
    now = datetime.now()
    hournow = now.hour
    minnow = now.minute
    if int(hournow) == int (hour1) and int(minnow) == int(minute1) or itstime == False:
        #for x in range (0,10):
        itstime = False
        print_name.start()
        loopClock.start()

#now = datetime.now()
#hournow = now.hour
#minnow = now.minute
#if int(hournow) == int (hour1) and int(minnow) == int(minute1) or itstime == True:
#    #for x in range (0,10):
#    itstime = True
#    print_name.start()
#    loopClock.start()

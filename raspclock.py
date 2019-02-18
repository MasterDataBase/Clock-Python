from time import sleep
from datetime import datetime

itstime = False

I1 = raw_input('Set Alarm Time: ')
if len(I1) > 3:
    hour1 = I1[0:2]
    minute1 = I1[2:]
    print 'Alarm set for: %s:%s' % (hour1,minute1)
    
while True:
    now = datetime.now()
    hournow = now.hour
    minnow = now.minute
    if int(hournow) == int (hour1) and int(minnow) == int(minute1) or itstime == True:
        #for x in range (0,10):
        itstime = True
        print 'ALARM!'
    sleep(2)
import sys
from Tkinter import *
import time

newAlarm = -1

def tick():
    time_string = time.strftime("%H:%M:%S")
    print(time_string, " / ", newAlarm)
    clock.config(text=time_string)
    clock.after(200,tick)
    
#    if time_string == newAlarm:
#        print ("Eccoci")

def setAlarm():
    #Comando per prelevare i dati da TextBox
    newAlarm = T.get("1.0", 'end-1c')
    print(newAlarm)
    print(time_string)

root = Tk()
root.title("Clock")

#Clock
clock = Label(root, font=("times", 50, "bold"),bg="white")
clock.grid(row=0, column=0)
tick()

#TextBox time
T = Text(root, height=0, width=30)
T.grid(row=1, column=0)
T.insert(END, "")

#Button SetTime
btnSetTime = Button(root, text="Set alarm!",
                    command=setAlarm)

btnSetTime.grid(row=1, column=1)

root.mainloop()
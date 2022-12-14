import time
from tkinter import *
from csv import *
import numpy
from datetime import datetime
import os
import threading
import webbrowser

#global variables
now = datetime.now()
current_time = now.strftime("%H:%M:%S.%f")[:-3]
total_data=[]

#save start time
list = ["Start Time", current_time]
total_data.append(list)

#initialize UI
interface = Tk()
interface.geometry("700x600")
interface.title("LifeSpan Trigger Recorder")
interface['background'] = '#EDEDED'

#*Functions*

#Create CSV file
def SaveData():
    with open(str(SubjectCodeEntry.get())+".csv","w") as file:
        Writer = writer(file)
        Writer.writerow(["Event", "Time"])
        Writer.writerows(total_data)


#Add trigger data to csv file
def Add(trigger):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S.%f")[:-3]
    list = [trigger, current_time]
    total_data.append(list)
    Color("#7CFC00")
    time.sleep(0.5)
    Color("#fb3b1e")

def Color(color):
    StatusIndicator.itemconfig(Oval, outline=color, fill=color)

#*labels & entries*

#UI Title
Title = Label(interface, text="LifeSpan Trigger Recorder")
Title.place(relx=0.5, rely=0.1, anchor=CENTER)
Title.configure(bg='#EDEDED', font = ("TkDefaultFont", 25))

#Subject Code Label and Entry
SubjectCodeLabel = Label(interface, text="Subject Code")
SubjectCodeLabel.place(relx=0.2, rely=0.2, anchor=CENTER)
SubjectCodeLabel.configure(bg='#EDEDED')
SubjectCodeEntry = Entry(interface, width=30)
SubjectCodeEntry.place(relx=0.5, rely=0.2, anchor=CENTER)
SubjectCodeEntry.configure(bg='#FFFFFF')

#Status Label and Indicator
StatusLabel = Label(interface, text="Status")
StatusLabel.place(relx=0.2, rely=0.3, anchor=CENTER)
StatusLabel.configure(bg='#EDEDED')
StatusIndicator = Canvas(interface, width=30, height=30, bg='#EDEDED', highlightthickness=0)
StatusIndicator.place(relx=0.26, rely=0.3, anchor=CENTER)
Oval = StatusIndicator.create_oval(2, 27, 27, 2,outline="#fb3b1e", fill="#fb3b1e")

#Eyes Open trigger
EyesOpen = Button(interface, text="Eyes Open", height=2, width=15, command=lambda:Add("Eyes Open"))
EyesOpen.place(relx=0.4, rely=0.3, anchor=CENTER)

#Eyes Closed trigger
EyesClosed = Button(interface, text="Eyes Closed", height=2, width=15, command=lambda:Add("Eyes Closed"))
EyesClosed.place(relx=0.4, rely=0.4, anchor=CENTER)

#Entertainment On trigger
EntertainmentOn = Button(interface, text="Entertainment On", height=2, width=15, command=lambda:Add("Entrainment On"))
EntertainmentOn.place(relx=0.4, rely=0.5, anchor=CENTER)

#Entertainment Off trigger
EntertainmentOff = Button(interface, text="Entertainment Off", height=2, width=15, command=lambda:Add("Entrainment Off"))
EntertainmentOff.place(relx=0.4, rely=0.6, anchor=CENTER)

#Sawtooth On trigger
SawtoothOn = Button(interface, text="Sawtooth On", height=2, width=15, command=lambda:Add("Sawtooth On"))
SawtoothOn.place(relx=0.6, rely=0.3, anchor=CENTER)

#Square On trigger
SquareOn = Button(interface, text="Square On", height=2, width=15, command=lambda:Add("Square On"))
SquareOn.place(relx=0.6, rely=0.4, anchor=CENTER)

#Triangle On trigger
TriangleOn = Button(interface, text="Triangle On", height=2, width=15, command=lambda:Add("Triangle On"))
TriangleOn.place(relx=0.6, rely=0.5, anchor=CENTER)

#Sine On trigger
SineOn = Button(interface, text="Sine On", height=2, width=15, command=lambda:Add("Sine On"))
SineOn.place(relx=0.6, rely=0.6, anchor=CENTER)

#Custom Trigger
CustomTriggerLabel = Label(interface, text="Custom Trigger")
CustomTriggerLabel.place(relx=0.38, rely=0.7, anchor=CENTER)
CustomTriggerLabel.config(bg='#EDEDED')
CustomTriggerEntry = Entry(interface, width=20)
CustomTriggerEntry.place(relx=0.45, rely=0.75, anchor=CENTER)
CustomTriggerButton = Button(interface, text="Send Trigger", command=lambda:Add(CustomTriggerEntry.get()))
CustomTriggerButton.place(relx=0.67, rely=0.75, anchor=CENTER)

#Save Data Button
SaveDataButton = Button(interface, text="Save Data", width=12, height=3, command=SaveData)
SaveDataButton.place(relx=0.5, rely=0.85, anchor=CENTER)

def ActivateRecorder():
    webbrowser.open('file://' + os.path.realpath(r"C:\Users\Oliver\Desktop\CyKit-master-Copy\Web\CyKIT.html"))
    os.system(r"C:\Users\Oliver\AppData\Local\Programs\Python\Python37\python.exe .\CyKIT.py 127.0.0.1 54123 6")

#UI Loop
interface.after(2000, threading.Thread(target=ActivateRecorder).start)
interface.mainloop()


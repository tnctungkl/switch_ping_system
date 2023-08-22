import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import subprocess
from functools import partial
import telepot
import threading
from subprocess import Popen, PIPE, CREATE_NO_WINDOW
import sys
import time
import os

def sendMsg(msg):    
    token = '[your token]' # telegram token
    receiver_id = '[your id]' #https://api.telegram.org/bot<TOKEN>/getUpdates
    bot = telepot.Bot(token)
    bot.sendMessage(receiver_id, msg) # send a activation message to telegram receiver id

def checkPing():    
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
        # determine if application is a script file or frozen exe
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)  
          
    with open(os.path.join(application_path, "ipaddresses.txt"), "r") as ipaddresses:
        root = Tk()
        labels=[] #creates an empty list for your labels
        for line in ipaddresses:
            fields = line.split(";")
            name = fields[0]
            ip = fields[1]
            command = f"ping {ip} -n 2"
            output = []            
            # self.popen is a Popen object
            popen = Popen(command.split(), stdout=PIPE, creationflags=CREATE_NO_WINDOW)
            lines_iterator = iter(popen.stdout.readline, b"")
            # poll() return None if the process has not terminated
            # otherwise poll() returns the process's exit code
            while popen.poll() is None:
                for line in lines_iterator:
                    line = line.decode("utf-8")
                    line = line.replace("\r\n", "")
                    if line != "":
                        print(line)
                    output.append(line)  
                                      
            print("\n" + "--------------------------------------------------------")
            
            if("Request timed out." or "unreachable") in output:                
                if ("KAT" in name):
                    msg = (name + " Kenar Switch 'KAPALI'..! ")
                    print(msg)
                    sendMsg(msg)
                else:
                    msg = (name + " Toplama Switch 'KAPALI'..! ")
                    print(msg)
                    sendMsg(msg)
            else:
                if ("KAT" in name):
                    msg = (name + " Kenar Switch 'AÇIK'..! ")
                    print(msg)                    
                    label = Label(root, text=msg) #set your text
                    label.pack()
                    labels.append(label) #appends the label to the list for further use 
                else:
                    msg = (name + " Toplama Switch 'AÇIK'..! ")
                    print(msg)
                    
                    label = Label(root, text=msg) #set your text
                    label.pack()
                    labels.append(label) #appends the label to the list for further use 
                                                
            print("--------------------------------------------------------" + "\n")
            
        ipaddresses.close()  
          
        print("********************************************************")
        
        time.sleep(60) 

 

checkPing()

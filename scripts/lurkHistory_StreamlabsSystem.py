#! /usr/bin/python2
ScriptName = "Lurk History"
Website = "https://twitch.tv/variablygeeky"
Description = "Saves a text file, to be counted, of users that have lurked."
Creator = "VariablyGeeky"
Version = "1.0.0"

import getpass
import os

def Init():
	return

def Execute(data):
    windowsUser = getpass.getuser()
    message = data.Message
    username = data.UserName
    directory = "C:\\Users\\" + windowsUser + "\\Documents\\Chatbot"
    
    if (data.GetParam(0)).lower() == "!lurkhistory":
        checkForDirectory(directory)
        lurkHistory = open(directory + "\\lurkHistory.txt", "r")
        history = lurkHistory.read()
        lurk = history.count(username.lower())
        send_message(username + " has lurked in stream " + str(lurk) + " times.")
        lurkHistory.close()
        return
        
    elif (data.GetParam(0)).lower() == "!lurk":
        checkForDirectory(directory)
        lurkFile = open(directory + "\\lurkHistory.txt", "a")
        lurkFile.write((username).lower() + "\n")
        lurkFile.close()
        return
    return
def Tick():
	return

def send_message(message):
    Parent.SendStreamMessage(message)
    return

def checkForDirectory(directory):
    if os.path.isdir(directory):
        return
    else:
        os.mkdir(directory)

#! /usr/bin/python2
ScriptName = "Keyword"
Website = "https://twitch.tv/variablygeeky"
Description = "Reads all of chat and triggers at set word"
Creator = "VariablyGeeky"
Version = "0.0.1"


def Init():
	return

def Execute(data):
    #if data.GetParam(0) != "!par":
    #    return
    #game = $mygame 
    message = data.Message 
    if "discord" in message:
        send_message("Join Discord! https://discord.com")
        return
    #split = []
    #split = message.split(",")
    #raw = data.RawData
    #send_message("You passed me " + str(argCount) + " arguments.")
    #send_message(message)
    #send_message(str(game))
    #newArgCount = len(split)
    #send_message(str(newArgCount))
    #game = requests.get("https:\/\/api.crunchprank.net\/twitch\/game\/variablygeeky")
    #send_message(game)
    
    return
def Tick():
	return

def send_message(message):
    Parent.SendStreamMessage(message)
    return

 		
        
	
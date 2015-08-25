'''
Created on 24/08/2015

@author: Jessica
'''

#set up variables with default values
power = "off"
volume = 10
brightness = 50
channel = 1
questionResponse = "top"

#top level menu
def onMenu():
    print("DISPLAY:\ta - change volume or brightness")
    print("\t\tb - change channel or turn off\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        return "volOrBri"
    else:
        return "chaOrPow"

#2nd level menu - volume or brightness
def volumeOrBrightnessMenu():
    print("DISPLAY:\ta - change volume")
    print("\t\tb - change brightness\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        return "vol1"
    else:
        return "bri1"

#2nd level menu - channel or power
def channelOrPowerMenu():
    global power
    print("DISPLAY:\ta - change channel")
    print("\t\tb - turn tv off\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        return "cha1"
    else:
        power = "off"
        return "top"

#3rd level menu - volume
def volumeChange1():
    global volume
    print("DISPLAY:\ta - increase volume by 1")
    print("\t\tb - decrease volume or return to main menu\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        if volume < 40:
            volume +=1
            print("ACTION:\t\tvolume increased\n")
            global questionResponse
            return questionResponse
        else:
            print("DISPLAY:\t\tvolume is already at maximum\n")
            global questionResponse
            return questionResponse
    else:
        return "vol2"

#3rd level menu - brightness
def brightnessChange1():
    global brightness
    print("DISPLAY:\ta - increase brightness by 1")
    print("\t\tb - decrease brightness or return to main menu\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        if brightness < 100:
            brightness +=1
            print("ACTION:\t\tbrightness increased\n")
            global questionResponse
            return questionResponse
        else:
            print("DISPLAY:\t\tbrightness is already at maximum\n")
            global questionResponse
            return questionResponse
    else:
        return "bri2"

#3rd level menu - channel
def channelChange1():
    global channel
    print("DISPLAY:\ta - increase channel by 1")
    print("\t\tb - decrease channel or return to main menu\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        if channel < 5:
            channel +=1
            print("ACTION:\t\tchannel increased\n")
            global questionResponse
            return questionResponse
        else:
            print("DISPLAY:\t\tyou are already on the highest channel\n")
            global questionResponse
            return questionResponse
    else:
        return "cha2"

#4th level menu - volume
def volumeChange2():
    global volume
    print("DISPLAY:\ta - decrease volume by 1")
    print("\t\tb - return to main menu\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        if volume > 0:
            volume -=1
            print("ACTION:\t\tvolume decreased\n")
            global questionResponse
            return questionResponse
        else:
            print("DISPLAY:\t\tvolume is already at minimum\n")
            global questionResponse
            return questionResponse
    else:
        return "main"

#4th level menu - brightness
def brightnessChange2():
    global brightness
    print("DISPLAY:\ta - decrease brightness by 1")
    print("\t\tb - return to main menu\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        if brightness > 0:
            brightness -=1
            print("ACTION:\t\tbrightness decreased\n")
            global questionResponse
            return questionResponse
        else:
            print("DISPLAY:\t\tbrightness is already at minimum\n")
            global questionResponse
            return questionResponse
    else:
        return "main"

#4th level menu - channel
def channelChange2():
    global channel
    print("DISPLAY:\ta - decrease channel by 1")
    print("\t\tb - return to main menu\n")
    response = raw_input("COMMAND:\t")
    if response == "a":
        if channel > 1:
            channel -=1
            print("ACTION:\t\tchannel decreased\n")
            global questionResponse
            return questionResponse
        else:
            print("DISPLAY:\t\tyou are already on the lowest channel\n")
            global questionResponse
            return questionResponse
    else:
        return "main"





while(1):

    #when the tv is off, the only option is to turn on
    while power == "off":
        print("DISPLAY:\ta - turn on")
        if raw_input("COMMAND:\t") == "a":
            power = "a"
        print("")


    print("\nDISPLAY:\tVolume: %d" %volume)
    print("DISPLAY:\tBrightness: %d" %brightness)
    print("DISPLAY:\tChannel: %d\n" %channel)

    if power == "a":
        power = "on"
        print("ACTION:\t\ttv on")

    if questionResponse == "top":
        questionResponse = onMenu()

    if questionResponse == "volOrBri":
        questionResponse = volumeOrBrightnessMenu()

    if questionResponse == "chaOrPow":
        questionResponse = channelOrPowerMenu()

    if questionResponse == "vol1":
        questionResponse = volumeChange1()

    if questionResponse == "bri1":
        questionResponse = brightnessChange1()

    if questionResponse == "cha1":
        questionResponse = channelChange1()

    if questionResponse == "off":
        on = "off"
        questionResponse = ""
        continue

    if questionResponse == "vol2":
        questionResponse = volumeChange2()

    if questionResponse == "bri2":
        questionResponse = brightnessChange2()

    if questionResponse == "cha2":
        questionResponse = channelChange2()

    if questionResponse == "main":
        questionResponse = "top"
        continue

    print questionResponse
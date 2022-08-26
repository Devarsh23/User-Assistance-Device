import pyttsx3

en = pyttsx3.init()
en.setProperty('rate', 125)
en.setProperty('volume',0.8)
    
def select():
    en.say("Select the mode.")
    en.runAndWait()
    return ""

def face(name):
    en.say("The name of the person is " + name)
    en.runAndWait()
    return ""

def name():
    en.say("Speak the name.") #You can speak the whole name or speak every character in the name one by one. Start now.")
    en.runAndWait()
    return ""
    
def spelling():
    en.say("The spelling of the entered name is:")
    en.runAndWait()
    return ""
    
def character(i):
    en.say(i)
    en.runAndWait()
    return ""

def correct():
    en.say("If the name is correct say yes otherwise say no.")
    en.runAndWait()
    return ""
    
def already():
    en.say("The name already exists. Try again, adding some unique information along with the name.")
    en.runAndWait()
    return ""
    
def front():
    en.say("Tell the person to stand exactly in front of the camera and look at the camera.")
    en.runAndWait()
    return ""
    
def right():
    en.say("Tell the person to turn his face slightly to the right.")
    en.runAndWait()
    return ""
    
def left():
    en.say("Tell the person to turn his face slightly to the left.")
    en.runAndWait()
    return ""
    
def up():
    en.say("Tell the person to slightly look upwards.")
    en.runAndWait()
    return ""
    
def down():
    en.say("Tell the person to slightly look downwards.")
    en.runAndWait()
    return ""
    
def complete():
    en.say("Sample collection is complete. Now, adding the face in the system. It can take some time.")
    en.runAndWait()
    return ""
    
def added():
    en.say("Face added to the system.")
    en.runAndWait()
    return ""
    
def again():
    en.say("Sorry, an error occured during the process. A face might not have been captured properly in the images. Try again.")
    en.runAndWait()
    return ""

def not_exist():
    en.say("The name does not exist in the database.")
    en.runAndWait()
    return ""

def removing():
    en.say("Removing the face from the database. It can take some time.")
    en.runAndWait()
    return ""

def removed():
    en.say("Face removed from the system.")
    en.runAndWait()
    return ""

def remove_again():
    en.say("Face removed from the system.")
    en.runAndWait()
    return ""

def sorry():
    en.say("Sorry, I did not get that.")
    en.runAndWait()
    return ""

def sorryyn():
    en.say("Sorry, I did not get that. Say yes or no again.")
    en.runAndWait()
    return ""

def nothing():
    en.say("Did not find anything in the image.")
    en.runAndWait()
    return ""

def caption(s):
    en.say(s)
    en.runAndWait()
    return ""

def taking():
    en.say("Taking the picture in 3 seconds.")
    en.runAndWait()
    return ""

def another():
    en.say("If you want to caption another image say yes otherwise say no.")
    en.runAndWait()
    return ""

def chair(distance):
    en.say("Distance to chair is {} steps.".format(distance))
    en.runAndWait()
    return ""

def sofa(distance):
    en.say("Distance to sofa is {} steps.".format(distance))
    en.runAndWait()
    return ""

def detect(object_name):
    en.say(object_name + " infront of you.")
    en.runAndWait()

#if __name__ == "__main__":
    #import os
    #print(os.path.abspath(os.path.join(os.getcwd(), '..')))
#    run()
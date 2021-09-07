#Authors/Contributors : Jainish Adesara, 
#                       Pruthvi Hingu, 
#                       Bhumit Ghadia, 
#                       Devarsh Patel

# we Are saving images here
import cv2
import numpy as np
import os
import pyttsx3
import speech_recognition as sr
import time
from gtts import gTTS


#import sys  
#sys.path.append('/home/pi/Project')
#import Mode

def run():
    r = sr.Recognizer()

    #en=pyttsx3.init()
    #en.setProperty('rate', 125)
    #en.setProperty('volume',0.8)
    #voices = en.getProperty('voices')
    #for voice in voices:
    #    print("Voice:")
    #    print(" - ID: %s" % voice.id)
    #    print(" - Name: %s" % voice.name)
    #    print(" - Languages: %s" % voice.languages)
    #    print(" - Gender: %s" % voice.gender)
    #    print(" - Age: %s" % voice.age)
    
    #en.setProperty('voice', "hindi")
    #en.say("Use command restart to restart the process. And, use command stop to stop the process.")
    #en.runAndWait()
    f="no"
    while f=="no":
        #en.say("Speak the name.") #You can speak the whole name or speak every character in the name one by one. Start now.")
        #en.runAndWait()
        mytext = "Speak the name."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("name.mp3")
        os.system("mpg321 name.mp3")
        #Mode.name()
        with sr.Microphone(4) as source:
            f2=0
            while f2==0:
                f1=0
                while f1==0:
                    try:
                        audio_text = r.listen(source,timeout=5,phrase_time_limit=15)
                        f1=1
                    except:
                        f1=0
                try:
                    # using google speech recognition
                    print("Text: "+r.recognize_google(audio_text))
                    text=r.recognize_google(audio_text)
                    count=0
                    for i in range(len(text)):
                        if text[i]==" ":
                            count+=1
                    if count>1:
                        text_list = text.split(" ")
                    else:
                        text_list = list(text)
                    #en = pyttsx3.init()
                    #text_list = list(text)
                    #en.say("The spelling of the entered name is:")
                    #en.runAndWait()
                    mytext = "The spelling of the entered name is:"
                    myobj = gTTS(text=mytext, lang='en', slow=False)
                    myobj.save("spelling.mp3")
                    os.system("mpg321 spelling.mp3")
                    #Mode.spelling()
                    for i in text_list:
                        #en.say(i)
                        #en.runAndWait()
                        myobj = gTTS(text=i, lang='en', slow=False)
                        myobj.save("character.mp3")
                        os.system("mpg321 character.mp3")
                        #Mode.character(i)
                    name = ("".join(text_list)).lower()
                    print(name)
                    f2=1
                except:
                    #en.say("Sorry, I did not get that.")
                    #en.runAndWait()
                    mytext = "Sorry, I did not get that."
                    myobj = gTTS(text=mytext, lang='en', slow=False)
                    myobj.save("sorry.mp3")
                    os.system("mpg321 sorry.mp3")
                    #Mode.sorry()
                    f2=0
            
        #en.say("If the name is correct say yes otherwise say no.")
        #en.runAndWait()
        mytext = "If the name is correct say yes otherwise say no."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("correct.mp3")
        os.system("mpg321 correct.mp3")
        #Mode.correct()
        with sr.Microphone(4) as source:
            f2=0
            while f2==0:
                f1=0
                while f1==0:
                    try:
                        print("talk")
                        audio_text= r.listen(source,timeout=5,phrase_time_limit=15)
                        f1=1
                    except:
                        f1=0
                try:
                    # using google speech recognition
                    print("Text: "+r.recognize_google(audio_text))
                    text_2=r.recognize_google(audio_text)
                    #print(text_2)
                    #en = pyttsx3.init()
                    if text_2.lower() == "yes":
                        f="yes"
                        f2=1
                    elif text_2.lower() == "no":
                        f="no"
                        f2=1
                    else:
                        #en.say("Sorry, I did not get that. Say yes or no again.")
                        #en.runAndWait()
                        mytext = "Sorry, I did not get that. Say yes or no again."
                        myobj = gTTS(text=mytext, lang='en', slow=False)
                        myobj.save("sorryyn.mp3")
                        os.system("mpg321 sorryyn.mp3")
                        #Mode.sorryyn()
                        f2=0
                    
                except:
                    #en.say("Sorry, I did not get that. Say yes or no again.")
                    #en.runAndWait()
                    mytext = "Sorry, I did not get that. Say yes or no again."
                    myobj = gTTS(text=mytext, lang='en', slow=False)
                    myobj.save("sorryyn.mp3")
                    os.system("mpg321 sorryyn.mp3")
                    #Mode.sorryyn()
                    f2=0

    try:
        #name=input("Enter Your name")
        os.rmdir("./dataset/"+name)
        #path = os.path.join("./dataset/",name)
        #os.chdir("./dataset")
        f3=1
    except:
        #en.say("The name does not exist in the database.")
        #en.runAndWait()
        mytext = "The name does not exist in the database."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("not_exist.mp3")
        os.system("mpg321 not_exist.mp3")
        #Mode.not_exist()
        f3=0

    if f3==1:
        #en.say("Removing the face from the database. It can take some time.")
        #en.runAndWait()
        mytext = "Removing the face from the database. It can take some time."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("removing.mp3")
        os.system("mpg321 removing.mp3")
        #Mode.removing()
        try:
            from FaceDetection import embeddings_extractor
            from FaceDetection import Train
            #embeddings_extractor.run()
            #Train.run()
            mytext = "Face removed from the system."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("removed.mp3")
            os.system("mpg321 removed.mp3")
            #en.say("Face removed from the system.")
            #en.runAndWait()
            #Mode.removed()
        except:
            #en.say("Sorry, an error occured during the process. Try again.")
            #en.runAndWait()
            mytext = "Sorry, an error occured during the process. Try again."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("error.mp3")
            os.system("mpg321 error.mp3")
            #Mode.remove_again()

if __name__ == "__main__":
    run()
#Authors/Contributors : Jainish Adesara, 
#                       Pruthvi Hingu, 
#                       Bhumit Ghadia, 
#                       Devarsh Patel

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


    f3=0
    while f3 == 0:
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
                        #text = "jainish"
                        text = text.lower()
                        count=0
                        if text == "stop":
                            return ""
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
                            audio_text= r.listen(source,timeout=5,phrase_time_limit=5)
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
                        elif text_2.lower() == "no" or text_2.lower() == "now":
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
            os.mkdir("/home/pi/Project/FaceDetection/dataset/"+name)
            path = os.path.join("/home/pi/Project/FaceDetection/dataset/",name)
            os.chdir("/home/pi/Project/FaceDetection/dataset")
            f3=1
        except:
            #en.say("The name already exists. Try again, adding some unique information along with the name.")
            #en.runAndWait()
            mytext = "The name already exists. Try again, adding some unique information along with the name."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("already.mp3")
            os.system("mpg321 already.mp3")
            #Mode.already()
            f3=0

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 0
    # Collect 100 samples of your face from webcam input
    while count<25:
        if count==0:
            #en.say("Tell the person to stand exactly in front of the camera and look at the camera.")
            #en.runAndWait()
            mytext = "Tell the person to stand exactly in front of the camera and look at the camera."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("front.mp3")
            os.system("mpg321 front.mp3")
            #Mode.front()
            time.sleep(5)
        elif count==5:
            #en.say("Tell the person to turn his face slightly to the right.")
            #en.runAndWait()
            mytext = "Tell the person to turn his face slightly to the right."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("right.mp3")
            os.system("mpg321 right.mp3")
            #Mode.right()
            time.sleep(5)
        elif count==10:
            #en.say("Tell the person to turn his face slightly to the left.")
            #en.runAndWait()
            mytext = "Tell the person to turn his face slightly to the left."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("left.mp3")
            os.system("mpg321 left.mp3")
            #Mode.left()
            time.sleep(5)
        elif count==15:
            #en.say("Tell the person to slightly look upwards.")
            #en.runAndWait()
            mytext = "Tell the person to slightly look upwards."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("up.mp3")
            os.system("mpg321 up.mp3")
            #Mode.up()
            time.sleep(5)
        elif count==20:
            #en.say("Tell the person to slightly look downwards.")
            #en.runAndWait()
            mytext = "Tell the person to slightly look downwards."
            myobj = gTTS(text=mytext, lang='en', slow=False)
            myobj.save("down.mp3")
            os.system("mpg321 down.mp3")
            #Mode.down()
            time.sleep(5)
        ret, frame = cap.read()
        # Save file in specified directory with unique name
        file_name_path = "./"+name+"/"+ str(count) + '.jpg'
        print(file_name_path)
        cv2.imwrite(file_name_path, frame)
        cv2.imshow("Frame",frame)
        count+=1
        if cv2.waitKey(1) == 13: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows()      
    print("Collecting Samples Complete.")
    #en.say("Sample collection is complete. Now, adding the face in the system. It can take some time.")
    #en.runAndWait()
    mytext = "Sample collection is complete. Now, adding the face in the system. It can take some time."
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save("complete.mp3")
    os.system("mpg321 complete.mp3")
    #Mode.complete()

    try:
        #embeddings_extractor.run()
        #Train.run()
        from FaceDetection import embeddings_extractor
        from FaceDetection import Train
        #en.say("Face added to the system.")
        #en.runAndWait()
        mytext = "Face added to the system."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("added.mp3")
        os.system("mpg321 added.mp3")
        #Mode.added()
    except:
        #en.say("Sorry, an error occured during the process. A face might not have been captured properly in the images. Try again.")
        #en.runAndWait()
        mytext = "Sorry, an error occured during the process. A face might not have been captured properly in the images. Try again."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("again.mp3")
        os.system("mpg321 again.mp3")
        #Mode.again()

if __name__ == "__main__":
    run()
#Authors/Contributors : Jainish Adesara, 
#                       Pruthvi Hingu, 
#                       Bhumit Ghadia, 
#                       Devarsh Patel

import cv2
import requests
from io import BytesIO
import pyttsx3
import speech_recognition as sr
from imutils.video import FPS
from imutils.video.pivideostream import PiVideoStream
import time
import os
from gtts import gTTS
#import sys  
#sys.path.append('/home/pi/Project')
#import Mode

#en = pyttsx3.init()
#en.setProperty('rate', 125)
#en.setProperty('volume',0.8)

def showimg(frame):
    ret, img_encode = cv2.imencode('.jpg', frame)
    str_encode = img_encode.tostring()
    f4 = BytesIO(str_encode)
    r = requests.post("https://api.deepai.org/api/densecap",
        files={'image': f4,},
        headers={'api-key': 'fd560200-e009-4bea-b790-a4f62be469ab'})
    j=r.json()
    text=[]
    for i in j["output"]["captions"]:
        if i["confidence"]>=0.95 and i["caption"] not in text:
            text.append(i["caption"])

    if text == []:
        #en.say("Did not find anything in the image.")
        #en.runAndWait()
        mytext = "Did not find anything in the image."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("nothing.mp3")
        os.system("mpg321 nothing.mp3")
        #Mode.nothing()
        return ""
    else:
        s=""
        for i in text:
            s=s+i+", "
        #en.say(s)
        #en.runAndWait()
        #mytext = "Did not find anything in the image."
        myobj = gTTS(text=s, lang='en', slow=False)
        myobj.save("sentence.mp3")
        os.system("mpg321 sentence.mp3")
        #Mode.caption(s)
        return s    

def run():
    #cap=cv2.VideoCapture("http://192.168.0.101:8080/video")
    r = sr.Recognizer()
    #en=pyttsx3.init()
    #en.setProperty('rate', 125)
    #en.setProperty('volume',0.8)

    vs = PiVideoStream().start()
    time.sleep(2.0)

    fps = FPS().start()
    f="yes"
    while f=="yes":
        #en.say("Taking the picture in 3 seconds.")
        #en.runAndWait()
        mytext = "Taking the picture in 3 seconds."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("taking.mp3")
        os.system("mpg321 taking.mp3")
        #Mode.taking()
        time.sleep(3)
        frame = vs.read()
        #_,frame=cap.read()
        #cv2.imshow("frame",frame)
        #key = cv2.waitKey(1) & 0xFF
        #if key == ord("q"):
            #break
        text=showimg(frame)
        print(text)
        time.sleep(2)
        #en.say("If you want to caption another image say yes otherwise say no.")
        #en.runAndWait()
        mytext = "If you want to caption another image say yes otherwise say no."
        myobj = gTTS(text=mytext, lang='en', slow=False)
        myobj.save("caption.mp3")
        os.system("mpg321 caption.mp3")
        #Mode.another()
        f2=0
        with sr.Microphone(4) as source:
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

    #cap.release()
    cv2.destroyAllWindows()
    vs.stop()
    return ""

if __name__ == "__main__":
    run()
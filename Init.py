import multiprocessing
import concurrent.futures
import pyttsx3
import speech_recognition as sr
import os
from Indoor import Chairsofadistance
from ZebraCrossing import zebra_cross
from FaceDetection import FaceDetection, AddFace, RemoveFace
from ImageCaptioning import ImageCaptioning
from ObjectDetection import Detection
#import simpleaudio as sa
#import Mode
# from subprocess import call
# import importlib
from gtts import gTTS
#Mode.run()
#en = pyttsx3.init()

r = sr.Recognizer()
with sr.Microphone(4) as source:

    def stop():
        #en = pyttsx3.init()
        #r = sr.Recognizer()
        mode = ""
        while not(mode == "stop"):
            try:
                #with sr.Microphone() as source:
                        # print("Speak")
                        # en.say("Select the mode.")
                        #en.runAndWait()
                audio_text = r.listen(source,timeout=5, phrase_time_limit=10)
                try:
                        # using google speech recognition
                    print("Text: "+r.recognize_google(audio_text))
                    mode = r.recognize_google(audio_text)
                    mode = mode.lower()
                    print(mode)
                except:
                    print("Say stop to exit")
            except:
                print("Stop wait timeout")
        return "stop"
    
    def module1():
        Detection.run()

    def module2():
        FaceDetection.run()
        #zebra_cross.run()

    def module3():
        Chairsofadistance.run()
        
    def module4():
        ImageCaptioning.run()
        
    def module5():
        AddFace.run()
    
    def module6():
        RemoveFace.run()


    if __name__ == "__main__":
        #r = sr.Recognizer()
        #p1 = multiprocessing.Process(target=stop)
        #mode = "indore"
        # modes = ("indore", "zebra crossing", "face detection")
        # while mode == "none":
        while True:
            mode = ""
            try:
                #with sr.Microphone() as source:
                    # print("Speak")
                #en = pyttsx3.init()
                #en.setProperty('rate', 125)
                #en.setProperty('volume',0.8)
                #en.say("Select the mode.")
                #en.runAndWait()
                #en.stop()
                #Mode.select()
                #filename = 'select.wav'
                #wave_obj = sa.WaveObject.from_wave_file(filename)
                #play_obj = wave_obj.play()
                #play_obj.wait_done()
                #mytext = 'Select the mode.'
                #language = 'en'
                #myobj = gTTS(text=mytext, lang=language, slow=False)
                #myobj.save("welcome.mp3")
                os.system("mpg321 select.mp3")
                
                audio_text = r.listen(source, timeout=5, phrase_time_limit=10)
                try:
                    # using google speech recognition
                    print("Text: "+r.recognize_google(audio_text))
                    mode = r.recognize_google(audio_text)
                    mode = mode.lower()
                    print(mode)
                    if mode == "1":
                        #engine.stop()
                        p1 = multiprocessing.Process(target=stop)
                        p2 = multiprocessing.Process(target=module1)
                        p2.start()
                        p1.start()
                        p1.join()
                        p2.terminate()
        
                    elif mode == "2" or mode == "tu":
                        p1 = multiprocessing.Process(target=stop)
                        p2 = multiprocessing.Process(target=module2)
                        p2.start()
                        # zebra_cross.run()
                        p1.start()
                        p1.join()
                        p2.terminate()

                    elif mode == "3":
                        # FaceDetection.run()
                        p1 = multiprocessing.Process(target=stop)
                        p2 = multiprocessing.Process(target=module3)
                        p2.start()
                        p1.start()
                        p1.join()
                        p2.terminate()
                    elif mode == "4":
                        # FaceDetection.run()
                        p1 = multiprocessing.Process(target=stop)
                        p2 = multiprocessing.Process(target=module4)
                        p2.start()
                        p1.start()
                        p1.join()
                        p2.terminate()
                    elif mode == "5":
                        # FaceDetection.run()
                        p1 = multiprocessing.Process(target=stop)
                        p2 = multiprocessing.Process(target=module5)
                        p2.start()
                        p1.start()
                        p1.join()
                        p2.terminate()
                    elif mode == "6":
                        # FaceDetection.run()
                        p1 = multiprocessing.Process(target=stop)
                        p2 = multiprocessing.Process(target=module6)
                        p2.start()
                        p1.start()
                        p1.join()
                        p2.terminate()
                    else:
                        print("No module selected")
                        
                except:
                    print("Sorry, I did not get that")
            except:
                print("Wait timeout")
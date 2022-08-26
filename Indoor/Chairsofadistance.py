#Authors/Contributors : Jainish Adesara, 
#                       Pruthvi Hingu, 
#                       Bhumit Ghadia, 
#                       Devarsh Patel

import numpy as np
import argparse
import cv2
from imutils.video import FPS
from imutils.video.pivideostream import PiVideoStream
import time
import pyttsx3
from os.path import dirname, join
import os
from gtts import gTTS

#import speech_recognition as sr
#import sys  
#sys.path.append('/home/pi/Project')
#import Mode

protoPath = join(dirname(__file__), "MobileNetSSD_deploy.prototxt")
modelPath = join(dirname(__file__), "MobileNetSSD_deploy.caffemodel")

def run():
    # construct the argument parse
    #parser = argparse.ArgumentParser(description='Script to run MobileNet-SSD object detection network ')
    #parser.add_argument("--video", help="path to video file. If empty, camera's stream will be used")
    #parser.add_argument("--prototxt", default="MobileNetSSD_deploy.prototxt", help='Path to text network file: ' 'MobileNetSSD_deploy.prototxt for Caffe model or ')
    #parser.add_argument("--weights", default="MobileNetSSD_deploy.caffemodel", help='Path to weights: ' 'MobileNetSSD_deploy.caffemodel for Caffe model or ' )
    #parser.add_argument("--thr", default=0.2, type=float, help="confidence threshold to filter out weak detections")
    #args = parser.parse_args()

    # Labels of Network.
    classNames = {0: 'background', 1: 'aeroplane', 2: 'bicycle', 3: 'bird', 4: 'boat', 5: 'bottle', 6: 'bus', 7: 'car', 8: 'cat', 9: 'chair',
                  10: 'cow', 11: 'diningtable', 12: 'dog', 13: 'horse', 14: 'motorbike', 15: 'person', 16: 'pottedplant', 17: 'sheep', 18: 'sofa', 19: 'train', 20: 'tvmonitor'}

    # Open video file or capture device.
    # url="http://192.168.0.102:8080/video"
    #cap = cv2.VideoCapture(url)
    #cap = cv2.VideoCapture("E:/Jupyter-notebook/Project/Indoor/sofa1.mp4")
    #cap = cv2.VideoCapture(0)
    vs = PiVideoStream().start()
    time.sleep(2.0)
    fps = FPS().start()    
    #en = pyttsx3.init()
    #en.setProperty('rate', 125)
    #en.setProperty('volume',0.8)
    #prev_distance = 1000
    distance = 1000
    #r = sr.Recognizer()
    #mode = "none"
    # Load the Caffe model
    net = cv2.dnn.readNetFromCaffe(protoPath, modelPath)
    # while not(mode) == "seat":
    #    with sr.Microphone() as source:
    #        #print("Speak")
    #        en.say("Select the mode.")
    #        en.runAndWait()
    #        audio_text = r.listen(source,timeout=120,phrase_time_limit=5)
    #        try:
    # using google speech recognition
    #            print("Text: "+r.recognize_google(audio_text))
    #            mode = r.recognize_google(audio_text)
    #            mode = mode.lower()
    #            print(mode)
    #engine = pyttsx3.init()
    # engine.say(q)
    # engine.runAndWait()
    #        except:
    #            print("Sorry, I did not get that")

    count = 5
    while distance > 0:
        # Capture frame-by-frame
        #ret, frame = cap.read()
        # resize frame for prediction
        #frame_resized = cv2.resize(frame, (300, 300))
        frame = vs.read()
        frame_resized = cv2.resize(frame,(300,300))
        # MobileNet requires fixed dimensions for input image(s)
        # so we have to ensure that it is resized to 300x300 pixels.
        # set a scale factor to image because network the objects has differents size.
        # We perform a mean subtraction (127.5, 127.5, 127.5) to normalize the input;
        # after executing this command our "blob" now has the shape:
        # (1, 3, 300, 300)
        blob = cv2.dnn.blobFromImage(
            frame_resized, 0.007843, (300, 300), (127.5, 127.5, 127.5), False)
        # Set to network the input blob
        net.setInput(blob)
        # Prediction of network
        detections = net.forward()

        # Size of frame resize (300x300)
        cols = frame_resized.shape[1]
        rows = frame_resized.shape[0]

        #F = 210
        #D = 36
        #W = 22

        # For get the class and location of object detected,
        # There is a fix index for class, location and confidence
        # value in @detections array .
        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]  # Confidence of prediction
            if confidence > 0.8:  # Filter prediction
                class_id = int(detections[0, 0, i, 1])  # Class label

                if class_id == 9:
                    count+=1
                    # Object location
                    xLeftBottom = int(detections[0, 0, i, 3] * cols)
                    yLeftBottom = int(detections[0, 0, i, 4] * rows)
                    xRightTop = int(detections[0, 0, i, 5] * cols)
                    yRightTop = int(detections[0, 0, i, 6] * rows)
                    width = round(xRightTop - xLeftBottom, 4)
                    # print(width)
                    #F = width*D/W
                    # print(F)
                    # Distance from camera based on triangle similarity
                    #distance = (22 * F)/width
                    #distance = distance/12
                    #distance = int(distance)
                    distance = int(385/width)
                    # print("Distance(ft):{dist}/n".format(dist=distance))
                    print("Distance to chair is {} steps".format(distance))
                    if count >= 5:
                        count = 0
                        #en.say("Distance to chair is {} steps.".format(distance))
                        #en.runAndWait()
                        mytext = "Distance to chair is {} steps.".format(distance)
                        myobj = gTTS(text=mytext, lang='en', slow=False)
                        myobj.save("chair.mp3")
                        os.system("mpg321 chair.mp3")
                        #Mode.chair(distance)
                        #prev_distance = distance
                    # Factor for scale to original size of frame
                    heightFactor = frame.shape[0]/300.0
                    widthFactor = frame.shape[1]/300.0
                    # Scale object detection to frame
                    xLeftBottom = int(widthFactor * xLeftBottom)
                    yLeftBottom = int(heightFactor * yLeftBottom)
                    xRightTop = int(widthFactor * xRightTop)
                    yRightTop = int(heightFactor * yRightTop)
                    # Draw location of object
                    cv2.rectangle(frame, (xLeftBottom, yLeftBottom),
                                  (xRightTop, yRightTop), (0, 255, 0))

                    # Draw label and confidence of prediction in frame resized
                    if class_id in classNames:
                        label = classNames[class_id] + ": " + str(confidence)
                        labelSize, baseLine = cv2.getTextSize(
                            label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                        yLeftBottom = max(yLeftBottom, labelSize[1])
                        cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]), (
                            xLeftBottom + labelSize[0], yLeftBottom + baseLine), (255, 255, 255), cv2.FILLED)
                        cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                        #print(label)  # print class and confidence

                elif class_id == 18:
                    count+=1
                    # Object location
                    xLeftBottom = int(detections[0, 0, i, 3] * cols)
                    yLeftBottom = int(detections[0, 0, i, 4] * rows)
                    xRightTop = int(detections[0, 0, i, 5] * cols)
                    yRightTop = int(detections[0, 0, i, 6] * rows)
                    width = round(xRightTop - xLeftBottom, 4)
                    # print(width)
                    #F = width*D/W
                    # print(F)
                    # Distance from camera based on triangle similarity
                    #distance = (84 * F)/width
                    #distance = distance/12
                    #distance = int(distance)
                    distance = int(1470/width)
                    # print("Distance(in):{dist}/n".format(dist=distance))
                    print("Distance to sofa is {} steps".format(distance))
                    if count >= 5:
                        count = 0
                        #en.say("Distance to sofa is {} steps".format(distance))
                        #en.runAndWait()
                        mytext = "Distance to sofa is {} steps.".format(distance)
                        myobj = gTTS(text=mytext, lang='en', slow=False)
                        myobj.save("sofa.mp3")
                        os.system("mpg321 sofa.mp3")
                        #Mode.sofa(distance)
                        #prev_distance = distance
                    # Factor for scale to original size of frame
                    heightFactor = frame.shape[0]/300.0
                    widthFactor = frame.shape[1]/300.0
                    # Scale object detection to frame
                    xLeftBottom = int(widthFactor * xLeftBottom)
                    yLeftBottom = int(heightFactor * yLeftBottom)
                    xRightTop = int(widthFactor * xRightTop)
                    yRightTop = int(heightFactor * yRightTop)
                    # Draw location of object
                    cv2.rectangle(frame, (xLeftBottom, yLeftBottom),
                                  (xRightTop, yRightTop), (0, 255, 0))
                    # Draw label and confidence of prediction in frame resized
                    if class_id in classNames:
                        label = classNames[class_id] + ": " + str(confidence)
                        labelSize, baseLine = cv2.getTextSize(
                            label, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
                        yLeftBottom = max(yLeftBottom, labelSize[1])
                        cv2.rectangle(frame, (xLeftBottom, yLeftBottom - labelSize[1]), (
                            xLeftBottom + labelSize[0], yLeftBottom + baseLine), (255, 255, 255), cv2.FILLED)
                        cv2.putText(frame, label, (xLeftBottom, yLeftBottom),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
                        #print(label)  # print class and confidence
                else:
                    count+=1
            fps.update()        
        fps.stop()
        #print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

        cv2.namedWindow("frame", cv2.WINDOW_NORMAL)
        cv2.imshow("frame", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

if __name__ == "__main__":
    run()
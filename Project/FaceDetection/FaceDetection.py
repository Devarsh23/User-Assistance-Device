#Authors/Contributors : Jainish Adesara, 
#                       Pruthvi Hingu, 
#                       Bhumit Ghadia, 
#                       Devarsh Patel

# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
from imutils.video.pivideostream import PiVideoStream
import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os
import pyttsx3
from gtts import gTTS
#import sys  
#sys.path.append('/home/pi/Project')
#import Mode


def run():
    # load our serialized face detector from disk
    #print("[INFO] loading face detector...")
    protoPath = os.path.sep.join(
        ["/home/pi/Project/FaceDetection/face_detection_model", "deploy.prototxt"])
    modelPath = os.path.sep.join(
        ["/home/pi/Project/FaceDetection/face_detection_model", "res10_300x300_ssd_iter_140000.caffemodel"])
    detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

    # load our serialized face embedding model from disk
    #print("[INFO] loading face recognizer...")
    embedder = cv2.dnn.readNetFromTorch(
        "/home/pi/Project/FaceDetection/openface_nn4.small2.v1.t7")

    # load the actual face recognition model along with the label encoder
    recognizer = pickle.loads(open(
        "/home/pi/Project/FaceDetection/output/recognizer.pickle", "rb").read())
    le = pickle.loads(open(
        "/home/pi/Project/FaceDetection/output/le.pickle", "rb").read())

    # initialize the video stream, then allow the camera sensor to warm up
    #print("[INFO] starting video stream...")
    vs = PiVideoStream().start()
    time.sleep(2.0)

    fps = FPS().start()
    #vs = VideoStream(src=0).start()
    #time.sleep(2.0)
    # start the FPS throughput estimator
    #fps = FPS().start()
    
    #en=pyttsx3.init()
    #en.setProperty('rate', 125)
    #en.setProperty('volume',0.8)
    # loop over frames from the video file stream
    name=""
    while name=="":
        # grab the frame from the threaded video stream
        frame = vs.read()

        # resize the frame to have a width of 600 pixels (while
        # maintaining the aspect ratio), and then grab the image
        # dimensions
        frame = imutils.resize(frame, width=600)
        (h, w) = frame.shape[:2]

        # construct a blob from the image
        imageBlob = cv2.dnn.blobFromImage(cv2.resize(
            frame, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0), swapRB=False, crop=False)

        # apply OpenCV's deep learning-based face detector to localize
        # faces in the input image
        detector.setInput(imageBlob)
        detections = detector.forward()

        # loop over the detections
        for i in range(0, detections.shape[2]):
            # extract the confidence (i.e., probability) associated with
            # the prediction
            confidence = detections[0, 0, i, 2]

            # filter out weak detections
            if confidence > 0.5:
                # compute the (x, y)-coordinates of the bounding box for
                # the face
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (startX, startY, endX, endY) = box.astype("int")

                # extract the face ROI
                face = frame[startY:endY, startX:endX]
                (fH, fW) = face.shape[:2]

                # ensure the face width and height are sufficiently large
                if fW < 20 or fH < 20:
                    continue

                # construct a blob for the face ROI, then pass the blob
                # through our face embedding model to obtain the 128-d
                # quantification of the face
                faceBlob = cv2.dnn.blobFromImage(
                    face, 1.0 / 255, (96, 96), (0, 0, 0), swapRB=True, crop=False)
                embedder.setInput(faceBlob)
                vec = embedder.forward()

                # perform classification to recognize the face
                preds = recognizer.predict_proba(vec)[0]
                j = np.argmax(preds)
                proba = preds[j]
                if proba > 0.7:
                    name = le.classes_[j]
                    # draw the bounding box of the face along with the
                    # associated probability
                    text = "{}: {:.2f}%".format(name, proba * 100)
                    y = startY - 10 if startY - 10 > 10 else startY + 10
                    cv2.rectangle(frame, (startX, startY), (endX, endY),
                                  (0, 0, 255), 2)
                    cv2.putText(frame, text, (startX, y),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        # update the FPS counter
        fps.update()

        # show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break

    # stop the timer and display FPS information
    fps.stop()
    mytext = "The name of the person is " + name
    myobj = gTTS(text=mytext, lang='en', slow=False)
    myobj.save("face.mp3")
    os.system("mpg321 face.mp3")
    #en.say("The name of the person is " + name)
    #en.runAndWait()
    #Mode.face(name)
    print(name)
    #print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
    #print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))

    # do a bit of cleanup
    cv2.destroyAllWindows()
    #vs.stream.release()
    vs.stop()
    return ""


if __name__ == "__main__":
    run()
# import the necessary packages
from imutils.video import VideoStream
from imutils.video import FPS
import numpy as np
from datetime import datetime
import imutils
import time
import cv2
import os
import telepot




# initialize the list of class labels MobileNet SSD was trained to
# load our serialized model from disk
print("[INFO] loading model...")
net = cv2.dnn.readNetFromCaffe("deploy.prototxt.txt", "deploy.caffemodel")
conf=0.5
# initialize the video stream, allow the cammera sensor to warmup,
# and initialize the FPS counter
print("[INFO] Initializing Camera...")

cam = cv2.VideoCapture(0)
time.sleep(0.1)



def handle(msg):
    #print(msg)
    global bot_api
    chat_id = msg['chat']['id']
    bot.sendMessage(bot_api,str(msg))
    command = msg['text']

    print('Got command: %s' % command)
    
    if command == '/image':
       
       bot.sendMessage(chat_id,text="Capturing Photos")
       
       ret, frame = cam.read()
       if ret==True:
            frame = cv2.flip(frame,1)
            cv2.imwrite('./photo.jpg', frame)
            cv2.imshow('Motion Detection',frame) 
       else:
            bot.sendMessage(chat_id,text="Captured Failed")
       
       #cv2.destroyAllWindows()
       bot.sendPhoto(chat_id=chat_id, photo=open('./photo.jpg', 'rb'))
      

    elif command =='/video':
        bot.sendMessage(chat_id,text="Camera starts recording")
        time.sleep(.1)
        bot.sendMessage(chat_id,text="Hold on please for 3 sec ")
        print('Start recording..')
        capture_duration = 10 #change here for duration of capturing video
        
        dim=(640,480)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('video.mp4',fourcc, 20.0, (640,480))
        start_time = time.time()
        while( int(time.time() - start_time) < capture_duration ):
            ret, frame = cam.read()
            if ret==True:
                frame = cv2.flip(frame,1)
                resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
                out.write(resized)
                cv2.imshow('Motion Detection',frame)                
            else:
                bot.sendMessage(chat_id,text="Record Failed")
                break
            k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
        
        out.release()
        #cam.release()
        #cv2.destroyAllWindows()
        
        print('Stop recording..')
        bot.sendMessage(chat_id,text="Recoding Completed")
        time.sleep(.1)
        bot.sendMessage(chat_id,text="Uploading video please be patient")
        time.sleep(.1)
        bot.sendVideo(chat_id, video=open('./video.mp4', 'rb'))

        
    elif (command=='hi') or (command=='Hi') or (command=='Hello') or (command=='hello') or (command=='Hey') or (command=='hey'):
        bot.sendMessage(chat_id,text="Hello i'm your Motion Detection assistant.\nHow can I Help You. \n/help")
    elif (command=='/-h') or (command=='/help') or (command=='/info') :
        bot.sendMessage(chat_id,text="Hello You Can Proceed with these commands \n /video \n /image")

def sendvid(objc):
        global chat_id
        global bot_api
        bot.sendMessage(chat_id,text=(str(objc)+"Detected \nI'm going to Send you the footage now"))
        time.sleep(0.1)
        bot.sendMessage(chat_id,text="Hold on please for 3 sec ")
        print('Start recording..')
        capture_duration = 3 #duration of capturing video
        
        dim=(640,480)
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter('video.mp4',fourcc, 20.0, (640,480))
        start_time = time.time()
        while( int(time.time() - start_time) < capture_duration ):
            ret, frame = cam.read()
            if ret==True:
                frame = cv2.flip(frame,1)
                resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
                out.write(resized)
                cv2.imshow('Motion Detection',frame)                
            else:
                bot.sendMessage(chat_id,text="Record Failed")
                break
            k = cv2.waitKey(1) & 0xff # Press 'ESC' for exiting video
            if k == 27:
                break
        
        out.release()
        #cv2.destroyAllWindows()
        #cam.release()
        
        print('Stop recording..')
        bot.sendMessage(chat_id,text="Recoding Completed")
        
        time.sleep(.1)
        bot.sendMessage(chat_id,text="Uploading video please be patient..")
        time.sleep(.1)
        bot.sendVideo(bot_api, video=open('./video.mp4', 'rb'))
        bot.sendVideo(chat_id, video=open('./video.mp4', 'rb'))


bot = telepot.Bot('5344427693:AAG0LnkC8VeM7ykp2oYc8nkeG1CnbvUJDIA')
bot_api= 465509021
bot.message_loop(handle)
bot.sendMessage(1126960078,text="Hello I'm your assistant")
bot.sendMessage(1126960078,text="How can I Help You?")
print('Hello')
chat_id=1126960078




# loop over the frames from the video stream
ct=0
ct_t=0
v_thres_H=5
v_thres_C=5
v_thres_D=5
while True:
        # grab the frame from the threaded video stream and resize it
        # to have a maximum width of 300 pixels
        ct_t+=1
        
        _,frame = cam.read()
        frame=cv2.flip(frame,1)
        #frame = imutils.resize(frame, width=300)
      
        # grab the frame dimensions and convert it to a blob
        (h, w) = frame.shape[:2]
        blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)),
                0.007843, (300, 300), 127.5)

        # pass the blob through the network and obtain the detections and
        # predictions
        net.setInput(blob)
        detections = net.forward()

        # loop over the detections
        for i in np.arange(0, detections.shape[2]):
                # extract the confidence (i.e., probability) associated with
                # the prediction
                confidence = detections[0, 0, i, 2]

                # filter out weak detections by ensuring the `confidence` is
                # greater than the minimum confidence
                if confidence > conf:
                        # extract the index of the class label from the
                        # `detections`, then compute the (x, y)-coordinates of
                        # the bounding box for the object
                        
                        
                        idx = int(detections[0, 0, i, 1])
                        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                        (startX, startY, endX, endY) = box.astype("int")
                        
                        if idx==15:
                        # draw the prediction on the frame
                            label = "{}: {:.2f}%".format(("Person Detected"),confidence * 100)
                            cv2.rectangle(frame, (startX, startY), (endX, endY),
                                    (0,255,0), 2)
                            y = startY - 15 if startY - 15 > 15 else startY + 15
                            cv2.putText(frame, label, (startX, y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                            
                            cv2.imshow("Motion Detection", frame)
                            print("Motion Detected")
                            ct+=1
                            if(ct>=v_thres_H ):
                                    sendvid("Human Motion ")
                                    ct=0
                                    v_thres_H=150
                                    v_thres_C=5
                                    v_thres_D=5
                        elif(idx==8):#cat
                            label = "{}: {:.2f}%".format(("Cat Detected"),confidence * 100)
                            cv2.rectangle(frame, (startX, startY), (endX, endY),
                                    (0,255,0), 2)
                            y = startY - 15 if startY - 15 > 15 else startY + 15
                            cv2.putText(frame, label, (startX, y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                            
                            cv2.imshow("Motion Detection", frame)
                            print("Motion Detected")
                            ct+=1
                            if(ct>=v_thres_C ):
                                    sendvid("Animal Cat Motion ")
                                    ct=0
                                    v_thres_H=5
                                    v_thres_C=150
                                    v_thres_D=5

                            
                        elif(idx==12):#dog
                            label = "{}: {:.2f}%".format(("Dog Detected"),confidence * 100)
                            cv2.rectangle(frame, (startX, startY), (endX, endY),
                                    (0,255,0), 2)
                            y = startY - 15 if startY - 15 > 15 else startY + 15
                            cv2.putText(frame, label, (startX, y),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
                            
                            cv2.imshow("Motion Detection ", frame)
                            print("Motion Detected")
                            ct+=1
                            if(ct>=v_thres_D ):
                                    sendvid("Animal dog Motion")
                                    ct=0
                                    v_thres_H=5
                                    v_thres_C=5
                                    v_thres_D0=150



                                

        # show the output frame
        
        cv2.imshow("Image Classifier", frame)
        if(ct_t>=150):
                ct_t=0
                ct=0
        if cv2.waitKey(1) & 0xFF == 27:
                break


# do a bit of cleanup
cv2.destroyAllWindows()
cam.release()

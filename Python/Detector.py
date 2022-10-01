#Name:Ashish Ramesh
#Github ID : AshishRamesh

import cv2 as cv , pandas
from datetime import datetime

video = cv.VideoCapture(0)
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
first_frame = None
status_list = [None,None]
times = []
df = pandas.DataFrame(columns=['Start','End'])

while True :
    check,frame = video.read()
    cvt = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    cvt = cv.GaussianBlur(cvt,(21,21),0)
    status = 0

    if first_frame is None:
        first_frame = cvt
        continue
    
    delta_frame = cv.absdiff(first_frame,cvt)
    thres_frame = cv.threshold(delta_frame,50,255,cv.THRESH_BINARY)[1]
    thres_frame = cv.dilate(thres_frame,None,iterations=2)
    (cnts,_) = cv.findContours(thres_frame.copy(),cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv.contourArea(contour) <= 10000:
            continue
        status = 1
        (x,y,w,h) = cv.boundingRect(contour)
        cv.rectangle(frame,(x,y),(x+w , y+h),(128,0,128),3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
        times.append(datetime.now())
    if status_list[-1]==0 and status_list[-2]==1:
        times.append(datetime.now())

    face = face_cascade.detectMultiScale(frame,
    scaleFactor = 2,
    minNeighbors = 5)
    for x,y,w,h in face:
        frame = cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv.imshow('Video',frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break

for i in range(0,len(times),2):
    df = df.append({'Start':times[i],'End':times[i+1]},ignore_index = True)
    print(df)
video.release()
cv.destroyAllWindows()
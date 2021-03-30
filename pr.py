import cv2
import sys
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_cepture = cv2.VideoCapture(0)
while True:
    ret,frame =video_cepture.read()
    gray=cv2.ctvColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30)
    )
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y) , (x+w , y+h) ,(0,255,0),2)
        cv2.waitKey(1) & 0xFF == ord('q')
        break
    video_cepture.release()
    cv2.destroyAllWindows()
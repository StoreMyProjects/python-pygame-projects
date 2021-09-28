import cv2

#load the cascade
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

#read the image input
img = cv2.imread("me.jpg")

#convert into grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#detect faces
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=5)

#draw rectangles around the faces
for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 3)

#display the output
cv2.imshow("Gray", img)
cv2.waitKey(0)

#close window
cv2.destroyAllWindows()
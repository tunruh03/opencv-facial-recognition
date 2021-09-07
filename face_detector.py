import cv2

#creates CascadeClassifier object that you can use to search for a face in an image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#opencv reads the file and stores it being read in the img variable
img = cv2.imread('news.jpg')

#converts rbg image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img,
                                    scaleFactor=1.1,
                                    minNeighbors=5)

for x, y, w, h in faces:
    img = cv2.rectangle(img, (x, y), (x+w, y+h),(0,255,0), 3)

print(faces, type(faces[0][0]))

resized = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

cv2.imshow('Gray', resized)
#the key must be pressed or it be in timed close mode
#otherwise the terminal will be stuck and you wont be able to use escape keys tp exit it
print("Press a key to quit please")
cv2.waitKey(0)
cv2.destroyAllWindows()
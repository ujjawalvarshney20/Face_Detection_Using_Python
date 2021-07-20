import cv2

# Load the cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Read the given image
uvfile = cv2.imread('test.jpeg')
# Convert the image into grayscales
gray = cv2.cvtColor(uvfile, cv2.COLOR_BGR2GRAY)
# Detect the faces in the image
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draw rectangle around the faces in the given image
for (x, y, w, h) in faces:
    cv2.rectangle(uvfile, (x, y), (x+w, y+h), (0, 255, 0), 2)
# Display the output
cv2.imshow('uvfile', uvfile )
cv2.waitKey()
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 17:16:24 2022

@author: 21260
"""

import cv2  
import matplotlib.pyplot as plt
# Load the cascade  
face_cascade = cv2.CascadeClassifier('resources/harcascade/haarcascade_frontalface_default.xml')  
  
# To capture video from existing video.   
cap = cv2.VideoCapture(0)  
  
while True:  
    # Read the frame  
    _, img = cap.read()  
  
    # Convert to grayscale  
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
  
    # Detect the faces  
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)  
  
    # Draw the rectangle around each face  
    for (x, y, w, h) in faces:  
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  
  
    # Display  
    cv2.imshow('Video', img)  
  
    # Stop if escape key is pressed  
    if cv2.waitKey(1) & 0xFF == ord('q'):
     
        break  
          
# Release the VideoCapture object  
cap.release()
cv2.destroyAllWindows()
plt.show()
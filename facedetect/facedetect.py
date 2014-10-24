#!/usr/bin/python
import sys, os
from opencv.cv import *
from opencv.highgui import *
 
def detectObjects(image):
  """Converts an image to grayscale and prints the locations of any 
     faces found"""
  grayscale = cvCreateImage(cvSize(image.width, image.height), 8, 1)
  cvCvtColor(image, grayscale, CV_BGR2GRAY)
 
  storage = cvCreateMemStorage(0)
  cvClearMemStorage(storage)
   
  cvEqualizeHist(grayscale, grayscale)
  face_cascade = cvLoadHaarClassifierCascade(
    '/usr/share/opencv/haarcascades/haarcascade_frontalface_default.xml',
    cvSize(1,1))
    
  face_cascade_2 = cvLoadHaarClassifierCascade(
    '/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml',
    cvSize(1,1))
 
   
  profile_cascade = cvLoadHaarClassifierCascade(
    '/usr/share/opencv/haarcascades/haarcascade_profileface.xml',
    cvSize(1,1)) 
   
  faces = cvHaarDetectObjects(image, face_cascade, storage, 1.2, 3,
                             CV_HAAR_DO_CANNY_PRUNING, cvSize(20, 20))
  
                         
  
                             
  faces2 = cvHaarDetectObjects(image, face_cascade_2, storage, 1.1, 3,
                             CV_HAAR_DO_CANNY_PRUNING, cvSize(20, 20))
                    
  faces_profiles = cvHaarDetectObjects(image, profile_cascade, storage, 1.1, 3,
                             CV_HAAR_DO_CANNY_PRUNING, cvSize(20, 20))
                             
  
  list=[];                     
  print('{"faces":[')
  if faces:
    for f in faces:
      list.append("["+str(f.x)+", "+str(f.y)+", "+str(f.width)+", "+str(f.height)+', "front_default"]')
  
  if faces2:
    for f in faces2:
      list.append("["+str(f.x)+", "+str(f.y)+", "+str(f.width)+", "+str(f.height)+', "front_alt"]')
  
  if faces_profiles:
    for f in faces_profiles:
      list.append("["+str(f.x)+", "+str(f.y)+", "+str(f.width)+", "+str(f.height)+', "profile"]')  
      
    
  print(", ".join(list))
  print(']}')
def main():
  image = cvLoadImage(sys.argv[1]);
  detectObjects(image)
 
if __name__ == "__main__":
  main()
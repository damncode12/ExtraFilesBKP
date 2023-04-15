import cv2 as cv
import numpy as np
blank = np.zeros((500,500,3),dtype='uint8')

cv.imshow('Blank',blank)
blank[200:300,300:400]=0,255,0
cv.imshow('Green',blank)
img =cv.imread('photos\pic1.png')
cv.imshow('pic',img)



cv.putText(blank,'Hello I am Ayushi',(0,255),cv.FONT_HERSHEY_TRIPLEX , 1.0,(0,255,0),2)
cv.imshow('Text',blank)



cv.waitKey(0)
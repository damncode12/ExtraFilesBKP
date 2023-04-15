import cv2 as cv
img =cv.imread('photos\pic2.png')
cv.imshow('pic',img)
#convert to grayscale
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur

blur=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#edge cascade
canny=cv.Canny(img,125,175)
cv.imshow('Canny',canny)

#dilating

dilated=cv.dilate(canny,(3,3),iterations=1)
cv.imshow('Dilated',dilated)
#eroding

eroded=cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded',eroded)

#resize
resized=cv.resize(img,(500,500))
cv.imshow('resized',resized)

cv.waitKey(0)
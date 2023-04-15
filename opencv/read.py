import cv2 as cv

#img=cv.imread('photos\pic1.png')

#cv.imshow('pic',img)
capture=cv.VideoCapture('video/videoplayback.mp4')
while True:
    isTrue, frame =capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()



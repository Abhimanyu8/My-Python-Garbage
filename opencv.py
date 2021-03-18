import cv2
import numpy as np

#import image and assign it to img variable :
img=cv2.imread("/home/Avimanyu/Pictures/gintama-minimalist-wallpaper-animewallpaper-ec6l9yn5yy4eh4ra.jpg")
#define kernel ((matrix size), numpy.unsigned-int, 8-bits) :
kernel = np.ones((5,5),np.uint8)

#turn image into grayscale :
imgrey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Using Canny edge-dector :
imgCanny = cv2.Canny(img,150,100)
#Dialation to increase edge thickness and clarity:
#iteration=thickness
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)s 

#display the output:
cv2.imshow("Gray Image",imgrey)
cv2.imshow("Canny Output",imgCanny)
cv2.imshow("imgDilation Output",imgDilation)

cv2.waitKey(0)
exit()
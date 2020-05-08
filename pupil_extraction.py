import cv2
import numpy as np

img_path = '/home/shrey/Desktop/eye images/eye9.jpg'
img = cv2.imread(img_path,0)
blur=cv2.GaussianBlur(img,(5,5),0)
kernel=np.ones((5,5),np.uint8)
mean = blur.mean()
print(mean)
_,th1 = cv2.threshold(blur,50,255,cv2.THRESH_BINARY_INV)

#opening=cv2.morphologyEx(th1,cv2.MORPH_OPEN,kernel,iterations=5)

closing=cv2.morphologyEx(th1,cv2.MORPH_CLOSE,kernel,iterations=5)

canny=cv2.Canny(closing,100,200)
circles=cv2.HoughCircles(canny,cv2.HOUGH_GRADIENT,1,20,param1=10,param2=20,minRadius=0,maxRadius=0)#

print(circles)

x = circles[:,:,0]
y = circles[:,:,1]
r = circles[:,:,2]

print(x,y,r)
img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
img = cv2.circle(img,(x,y),r,(0,255,0),1)
img = cv2.circle(img,(x,y),3,(0,0,255),-1)

#dilation=cv2.dilate(th1,kernel,iterations=5)

#erosion=cv2.erode(th1,kernel,iterations=5)

#_, contours, hierarchy=cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

#print(len(contours))

#img = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#img=cv2.drawContours(img,contours,-1,(0,0,255),2)

cv2.imshow('image',img)
#cv2.imshow('blur',blur)
#cv2.imshow('threshold',th1)
#cv2.imshow('canny',canny)

#cv2.imshow('opening',opening)
#cv2.imshow('closing',closing)
#cv2.imshow('erode',erosion)
#cv2.imshow('dilate',dilation)
cv2.waitKey(100000)
cv2.destroyAllWindows()

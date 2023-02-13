import cv2
import numpy as np


planets	= cv2.imread('testeesquerda.jpeg')
gray_img	=	cv2.cvtColor(planets,	cv2.COLOR_BGR2GRAY)
img	= cv2.medianBlur(gray_img,	5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

#center

circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=30,minRadius=0,maxRadius=0)
circles	= np.uint16(np.around(circles))


cont = 0
cont2 = 0

for	i in circles[0,:]:
		cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),6)
		cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)
		if (i[0]<300):
			cont=cont+1
		else:
			cont2=cont2+1
		print(i[0],i[1],i[2])

planets = cv2.putText( planets, str(cont),(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
planets = cv2.putText( planets, str(cont2),(350,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
planets = cv2.rectangle(planets,(1,1),(300,598),(255,0,0),2)
planets = cv2.rectangle(planets,(300,1),(598,598),(255,0,0),2)

cv2.imshow("HoughCirlces",	planets)
cv2.waitKey()
cv2.destroyAllWindows()
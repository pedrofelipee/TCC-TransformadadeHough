import cv2
import numpy as np


planets	= cv2.imread('erro.jpeg')

gray_img	=	cv2.cvtColor(planets,	cv2.COLOR_BGR2GRAY)
img	= cv2.medianBlur(gray_img,	5)


hsv_frame = cv2.cvtColor(planets, cv2.COLOR_BGR2HSV)
height, width, _ = planets.shape

circles	= cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,120,param1=100,param2=60,minRadius=0,maxRadius=0)
circles	= np.uint16(np.around(circles))


cont1 = 0
cont2 = 0
cont3 = 0

for	i in circles[0,:]:
    if i[2]>60 and i[2]<100:


        #Detecção de cor-----------------------
        cx = i[0]
        cy = i[1]

        pixel_center = hsv_frame[cy][cx]
        hue_value = pixel_center[0]
        saturation_value = pixel_center[1]
        value = pixel_center[2]

        color = "Undefined"
        if saturation_value<40:
            color = "Branco"
        elif value<50:
            color = "Preto"
        elif hue_value<5:
            color="Vermelho"
        elif hue_value<22:
            color="Laranja"
        elif hue_value<33:
            color="Amarelo"
        elif hue_value<78:
            color="Verde"
        elif hue_value<131:
            color="Azul"
        elif hue_value<170:
            color="Violeta"
        else:
            color="Vermelho"

        #	Desenha os circulos-------------------------------------------------------------------------
        cv2.circle(planets,(i[0],i[1]),i[2],(0,255,0),6)
		#	Desenha o centro dos circulos
        cv2.circle(planets,(i[0],i[1]),2,(0,0,255),3)

        
		
        # Acha onde esta errado o disco ----------------------------------------------------------------
        if((i[0]<300 and color=="Vermelho") or (i[0]<300 and color=="Preto")):
            cont1 = cont1 + 1
        if((i[0]>300 and i[0]<600 and color=="Branco") or (i[0]>300 and i[0]<600 and color=="Preto")):
            cont2 = cont2 + 1  
        if((i[0]>600 and color=="Vermelho" ) or (i[0]>600 and color=="Branco" )):
            cont3 = cont3 + 1


		
#Caso queira colocar numero de erros
#planets = cv2.putText( planets, str(cont1),(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
#planets = cv2.putText( planets, str(cont2),(350,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
#planets = cv2.putText( planets, str(cont3),(650,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

if(cont1>0):
    planets = cv2.putText( planets, "ERRO",(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
else:
    planets = cv2.putText( planets, "CORRETO",(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

if(cont2>0):
    planets = cv2.putText( planets, "ERRO",(400,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
else:
    planets = cv2.putText( planets, "CORRETO",(400,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

if(cont3>0):
    planets = cv2.putText( planets, "ERRO",(700,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
else:
    planets = cv2.putText( planets, "CORRETO",(700,50), cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

barra1 = int(((width)/3)-2)
barra2 = int(((width*2)/3)-2)
barra3 = int(width-2)
#print(barra1)

planets = cv2.rectangle(planets,(1,1),(barra1,height-2),(255,0,0),2)
planets = cv2.rectangle(planets,(barra1,1),(barra2,height-2),(255,0,0),2)
planets = cv2.rectangle(planets,(barra2,1),(barra3,height-2),(255,0,0),2)

cv2.imshow("HoughCirlces",	planets)
cv2.waitKey()
cv2.destroyAllWindows()
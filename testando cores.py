import cv2
import numpy as np
#import imutils

cap= cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,640)
cap.set(4,480)

while True:
    _,frame= cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width/2)
    cy = int(height/2)

    pixel_center = hsv_frame[cy,cx]
    hue_value = pixel_center[0]
    saturation_value = pixel_center[1]
    value = pixel_center[2]

    color = "Undefined"
    if saturation_value<80:
        color = "Branco"
    elif value<40:
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



    print(pixel_center)
    print(saturation_value)
    cv2.putText(frame,color,(10,50), 0, 1, (255,0,0), 2)
    cv2.circle(frame, (cx,cy), 5 , (255,0,0), 3)

    cv2.imshow("Frame", frame)


    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
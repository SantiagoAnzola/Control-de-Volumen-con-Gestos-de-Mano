#Se importan las librerias necesarias
import cv2
import mediapipe as mp
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from math import hypot
from comtypes import CLSCTX_ALL
import numpy as np
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np
from ctypes import cast, POINTER
import mediapipe as mp
from math import hypot
from ctypes import cast, POINTER


 #Inicia el prceso de captura de imagenes a traves de video, llamando a la funcion de OpenCV
cap = cv2.VideoCapture(0) 

#Se referencias las manos a traves de la funcion correspondiente de la libreria MediaPipe
mpHands = mp.solutions.hands 
hands = mpHands.Hands()  #Se termina de configurar la deteccion de manos 
#Detectar puntos de referencia 
mpDraw = mp.solutions.drawing_utils
 
#A traves de la libreria de pycaw se accede a los altavoces
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
#Volumen:
volume = cast(interface, POINTER(IAudioEndpointVolume))
#Barra de volumen
volbar=400
volper=0
 
#Se obtiene los rangos de volumen del altavoz y se guardan en sus respectivas variables
volMin,volMax = volume.GetVolumeRange()[:2]
 
while True:
    #Se verifica que la camara funcione
    success,img = cap.read() 
    #Para procesa #Se convierte la imagen BRG a RGB
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) 
    
    #Obtiene informcaion informacion
    #Se procesa la imagen paara analizar las manos 
    results = hands.process(imgRGB) 
 
    lmList = [] #Lista
    #Se agragan los resultados de la manos a la lista
    if results.multi_hand_landmarks: 

        #A traevs de la lista se halla la informacion de cada mano procesada 
        for handlandmark in results.multi_hand_landmarks:
            for id,lm in enumerate(handlandmark.landmark): #Se enumeran las imagenes
                # Se obtiene los puntos referencia de la mano
                h,w,_ = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmList.append([id,cx,cy]) #sSe agrega a la lista 
            #Se dibujan los puntos de la imagen    
            mpDraw.draw_landmarks(img,handlandmark,mpHands.HAND_CONNECTIONS)
    
    if lmList != []:
        #Se obtiene los valores en cada punto 
                        #x      #y
        x1,y1 = lmList[4][1],lmList[4][2]  #Punto del pulgar
        x2,y2 = lmList[8][1],lmList[8][2]  #Punto del indice
        #Se crea la conexion entre el pulgar y el indices
          #circulo en los dedos  con su respectvo radio en este caso de 10
        cv2.circle(img,(x1,y1),10,(0,0,0),cv2.FILLED) 
        cv2.circle(img,(x2,y2),10,(0,0,0),cv2.FILLED) 
          #Linea que conecta el indice con el pulgar
        cv2.line(img,(x1,y1),(x2,y2),(0,0,0),3)  
          #distancia de dedo a dedo con hipotenusa
        length = hypot(x2-x1,y2-y1) 
          
          #Longitud de los dedos en en terminos del volumen de -63 a 0
          #Longitud de manos de 30 a 350
        vol = np.interp(length,[30,350],[volMin,volMax])
        #Progreso de la barra lateral 
        volbar=np.interp(length,[30,350],[400,150])
        volper=np.interp(length,[30,350],[0,100])
        
        #Se dibujan las marcas calculadas
        print(vol,int(length))
        #Se da el volumen al altavoz del computador
        volume.SetMasterVolumeLevel(vol, None)

        #Se crea la barra lateral donde se muestera el progreso del volumen segun los calculos hechos 
        cv2.rectangle(img,(50,150),(85,400),(0,0,255),4) # Imagen , Posicion inicial , Posicion final ,color RGB ,Gr
        cv2.rectangle(img,(50,int(volbar)),(85,400),(0,0,255),cv2.FILLED)
        cv2.putText(img,f"{int(volper)}%",(10,40),cv2.FONT_ITALIC,1,(0, 255, 98),3)

        #tell the volume percentage ,location,font of text,length,rgb color,thickness
    cv2.imshow('Image',img) #Se muestra el video
    if cv2.waitKey(1) & 0xff==ord(' '): #Usando espacio, se detiene retraso
        break
        
cap.release()    #Se detiene camara     
cv2.destroyAllWindows() #Cierra ventana 
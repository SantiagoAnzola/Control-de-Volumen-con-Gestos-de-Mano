import cv2
import SeguimientoManos as sm
import numpy as np
#librerrias para controlar volumen 
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

#Parametros de la camara 
anchoCam, altoCam = 640, 480

#Lectura de la camara
cap = cv2.VideoCapture(0)
cap.set(3, anchoCam)
cap.set(4, altoCam)

#Creamos el objto que almacenara nuestra clase
detector = sm.detectormanos(maxManos=1, Cofdeteccion=0.7)

#Control de audio pc
dispositivos = AudioUtilities.GetSpeakers()
interfaz = dispositivos.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volumen = cast(interfaz, POINTER(IAudioEndpointVolume))
RangoVol = volumen.GetVolumeRange()
print(RangoVol)
VolMin = RangoVol[0]
VolMax = RangoVol[1]

while True:
    ret, frame = cap.reead() #Leemos la captura del video
    frame = detector.encontrarmanos(frame) #Llamamos el objeto qu contin la clase d detccion
    lista, bbox = detector.encontrarposicion(frame, dibujar= False)#llamamos las posiciones de los puntos que necesitamos
    if len(lista) != 0:
        print(lista[4], lista[8])
        x1,y1 = lista[4][1], lista[4][2]#Encontramos las cordenadas X e Y del pulgar
        x2,y2 = lista[8][1], lista[8][2]#Encontramos las cordenadas X e Y del indice


        #Comprrobamos que los dedos esten arriba
        dedos = detector.dedosarriba()
        print(dedos)

        #Nos aseguramos de que los dedos esten arriba 
        if dedos[0] == 1 and dedos[1] == 1:
            longitud, frame, linea = detector.distancia(4, 8, frame, r=8, t=2)
            print(longitud)


            #
            #

            vol = np.interp(longitud, [25, 200], [VolMin, VolMax])
            volumen.SetMasterVolumeLevel(vol, None)

            if longitud < 25:
                cv2.circle(frame, (linea[4], linea[5]), 10, (0, 255, 0), cv2.FILLED)


        cv2.imshow("Video", frame)
        t = cv2.waitKey(1)

        if t == 27:
            break

cap.release()
cv2.destroyAllWindows()



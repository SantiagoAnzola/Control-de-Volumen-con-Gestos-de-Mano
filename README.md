# 🔉 Control de Volumen con Gestos de Mano 🤏

<p align="center">
  <img src="https://github.com/SantiagoAnzola/Control-de-Volumen-con-Gestos-de-Mano/assets/87992831/d77e2377-589d-4904-b7ae-ecc5d8959f47" alt="Player" />
</p>

<br>
<p align="center">
  | <a href=READMEEN.md>English</a> | 
    <span>Español</span> |
</p>
<br>

## :hammer_and_wrench: Lenguajes y herramientas:
<p align="center" > <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## 📃 Descripción
Este código en Python utiliza gestos de mano capturados a través de una cámara web para controlar el volumen del sistema. Utiliza bibliotecas como OpenCV para capturar imágenes, MediaPipe para la detección de manos y PyCaw para el control de volumen.

## 💻 ¿Cómo Funciona? 

- El script captura imágenes a través de la cámara web utilizando OpenCV.
- Detecta los puntos de referencia de las manos utilizando MediaPipe.
- Calcula la distancia entre puntos específicos en el pulgar y el dedo índice para estimar la longitud del gesto de la mano.
- Según la longitud del gesto de la mano, ajusta el volumen del sistema.
- Se muestra una interfaz gráfica en la pantalla que muestra el nivel de volumen actual como un porcentaje y una representación visual de la barra de volumen.
>[!IMPORTANT]
>
>❌ Para cerrar la aplicación se debe usar la tecla ***ESC***  o la ***barra espaciadora (Spacebar)***.


## 📋 Requisitos

- Python 3.9
- OpenCV
  ```
  pip install opencv-python
  ```
- MediaPipe
  ```
  pip install mediapipe
  ```
- PyCaw
  ```
  pip install pycaw
  ```
- NumPy
  ```
  pip install numpy
  ```

## 📜 ¿Cómo Usar?

1. Asegúrate de tener todas las bibliotecas requeridas instaladas.
2. Ejecuta el código.
3. Coloca tu mano frente a la cámara web.
4. Utiliza tu pulgar y dedo índice para controlar el volumen:
   - Acerca tu pulgar y dedo índice para aumentar el volumen.
   - Separa tu pulgar y dedo índice para disminuir el volumen.
5. Presiona la barra espaciadora para salir del programa.

## 🔗 Referencias

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyCaw](https://github.com/AndreMiras/pycaw)

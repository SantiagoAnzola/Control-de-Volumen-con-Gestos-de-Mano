# 🔉 Control de Volumen con Gestos de Mano 🤏


<br>
<p align="center">
  | <a href=READMEEN.md>English</a> | 
    <span>Español</span> |
</p>
<br>

## 📃 Descripción:
Este código en Python utiliza gestos de mano capturados a través de una cámara web para controlar el volumen del sistema. Utiliza bibliotecas como OpenCV para capturar imágenes, MediaPipe para la detección de manos y PyCaw para el control de volumen.

## 💻 ¿Cómo Funciona? 

- El script captura imágenes a través de la cámara web utilizando OpenCV.
- Detecta los puntos de referencia de las manos utilizando MediaPipe.
- Calcula la distancia entre puntos específicos en el pulgar y el dedo índice para estimar la longitud del gesto de la mano.
- Según la longitud del gesto de la mano, ajusta el volumen del sistema.
- Se muestra una interfaz gráfica en la pantalla que muestra el nivel de volumen actual como un porcentaje y una representación visual de la barra de volumen.

## 📋 Requisitos

- Python 3.x
- OpenCV
- MediaPipe
- PyCaw
- NumPy

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

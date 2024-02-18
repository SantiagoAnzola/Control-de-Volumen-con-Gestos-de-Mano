# 🔉 Hands Gesture Volume Control 🤏

<p align="center">
  <img src="https://github.com/SantiagoAnzola/Control-de-Volumen-con-Gestos-de-Mano/assets/87992831/d77e2377-589d-4904-b7ae-ecc5d8959f47" alt="Player" />
</p>

<br>
<p align="center">
  | <span>English</span> | 
    <a href=README.md>Español</a> |
</p>
<be>

## :hammer_and_wrench: Languages and Tools:
<p align="center" > <a href="https://www.python.org" target="_blank" rel="noreferrer"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> </a> </p>

## 📃 Description
This Python script uses hand gestures captured through a webcam to control the system volume. It utilizes libraries like OpenCV for capturing images, MediaPipe for hand detection, and PyCaw for volume control.

## 💻 How It Works?

- The script captures images through the webcam using OpenCV.
- It detects hand landmarks using MediaPipe.
- It calculates the distance between specific points on the thumb and index finger to estimate the hand gesture's length.
- Based on the length of the hand gesture, it adjusts the system volume.
- A graphical interface is displayed on the screen showing the current volume level as a percentage and a visual representation of the volume bar.
>[!IMPORTANT]
>
>❌ To close the application, you must use the ***ESC*** key or the ***Spacebar***..


## 📋 Requirements

- Python 3.9
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

## 📜 How to Use?

1. Ensure you have all the required libraries installed.
2. Run the script.
3. Position your hand in front of the webcam.
4. Use your thumb and index finger to control the volume:
   - Move your thumb and index finger closer to increase the volume.
   - Move your thumb and index finger apart to decrease the volume.
5. Press the spacebar to exit the program.

## 🔗 References

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyCaw](https://github.com/AndreMiras/pycaw)

Feel free to modify and improve the script according to your needs!

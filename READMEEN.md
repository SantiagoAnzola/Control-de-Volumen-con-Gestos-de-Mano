# Hands Gesture Volume Control

This Python script uses hand gestures captured through a webcam to control the system volume. It utilizes libraries like OpenCV for capturing images, MediaPipe for hand detection, and PyCaw for volume control.
<br>
<p align="center">
  | <span>English</span> | 
    <a href=README.md>Español</a> |
</p>
<br>
## How It Works

- The script captures images through the webcam using OpenCV.
- It detects hand landmarks using MediaPipe.
- It calculates the distance between specific points on the thumb and index finger to estimate the hand gesture's length.
- Based on the length of the hand gesture, it adjusts the system volume.
- A graphical interface is displayed on the screen showing the current volume level as a percentage and a visual representation of the volume bar.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
- PyCaw
- NumPy

## How to Use

1. Ensure you have all the required libraries installed.
2. Run the script.
3. Position your hand in front of the webcam.
4. Use your thumb and index finger to control the volume:
   - Move your thumb and index finger closer to increase the volume.
   - Move your thumb and index finger apart to decrease the volume.
5. Press the spacebar to exit the program.

## References

- [OpenCV](https://opencv.org/)
- [MediaPipe](https://mediapipe.dev/)
- [PyCaw](https://github.com/AndreMiras/pycaw)

Feel free to modify and improve the script according to your needs!

# Actions-with-face-tracking
## Introductions
<img src = "./Readme/result.gif">


This project tracks face and eyes in face from camera by using **haarcascade_eye.xml, haarcascade_frontalface_default.xml.**  
It **calculate the coordinates of the center of your eyes** to **move your mouse**   
&nbsp;  
And it detects your **eye blinking** to enable various function like **click** or **scroll**. If you want other functions, modify
left_blink_op(), right_blink_op(), both_blink_op()in mouse_control.py.  
&nbsp;  
If this project is developed a little more, It will help you in a difficult situation to use your hands.

&nbsp;  

## Required library
- scipy
- matplotlib.pyplot
- numpy
- pyautogui  
&nbsp;  

## globals.py
It's for global values.  
For maintaining the detected face, eye, and coordinates to compare previous and current value.  
```python
import cv2
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
pyautogui.FAILSAFE = False

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# To keep when undetected 
last_left = None
last_right = None

last_left_coords = None
last_right_coords = None

last_detected_face = None
last_detected_face_coords = None

last_center_coords = (855, 553)
prev_center_coords = last_center_coords


#mouse_moving_threshold and sensitivity
movement_threshold = (2,20)
mouse_sensitivity = (15,15)

# to filter noise coordinate changes
my_list_x = [0]
my_list_y = [0]
N = 2 # Filter order
Wn = 0.9 # Cutoff frequency
B, A = signal.butter(N, Wn, output='ba')

min_blink_frames = 5
left_blink_frame_count = 0
right_blink_frame_count = 0
``` 
&nbsp;  

## detection.py
### detecting face
<img src = "./Readme/face_detect.gif">

By using haarcascade_frontalface_default.xml you can detect front-face on the img. 
And with the code inside of that function you can detect one of the largest faces it finds
```python
def detect_face(frame, face_cascade):
```
### detecting eyes
<img src = "./Readme/eye_detect.gif">

By using haarcascade_eye.xml you can detect eyes from the face-image that you already detected at detect_face function. 
Sometimes the nostrils are recognized with the eyes, so to increase accuracy, the faces were divided to detect the eyes.
```python
def detect_eyes(face_region, eye_cascade)
```

### detecting eye blinking
<img src = "./Readme/blink_detect.gif">

If the eye was not recognized for more than a few frames, it was made to recognize that the eye was blinking.
```python
def detect_blink(left_eye, right_eye, frame):
```
### detecting coordinate for eye
<img src = "./Readme/coord_detect.gif">

Returns the coordinates of the eyes on the screen.
```python
def coordForEye(face_coord, frame):
```
&nbsp;  
## mouse_control.py
### filtering the noise of x-coordinates of center of eyes
When moving the mouse using the received coordinates, the noise was so severe that it made a simple process. However, even if it is processed like this, the noise is so severe that we need to find a better way
```python
def processingX(a):
```
### filtering the noise of y-coordinates of center of eyes
```python
def processingY(a):
```
### moving mouse
Use the processed coordinates to move the mouse.
```python
def move_mouse_smoothly(left_eye, right_eye)
```
### various operations when eye blinks
For now, I only add click and scroll, but you can add various functions.
```python
def left_blink_op():
```
```python
def right_blink_op():
```
```python
def both_blink_op():
```  
&nbsp;

## main.py
```python
video_device = 0						
video = cv2.VideoCapture(video_device)
```
Adjust this if you want to change the video input device
```python
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```
If you press 'q' on the keyboard, it will stop running.



&nbsp;
## Reference
- for initial framework
    https://docs.opencv.org/4.x/d2/d99/tutorial_js_face_detection.html
- haarcascade_eye.xml, haarcascade_frontalface_default.xml for cascading:
    https://github.com/kipr/opencv/tree/master/data/haarcascades
- For processing the coordinates to decrease noise:  
    https://all-knowledge-of-the-world.tistory.com/19
- To stop the execution
    https://deep-learning-study.tistory.com/109  
&nbsp;  

## Licensing
This project is released by HuisuLim and following MIT LICENSE.
If you want to get more information about MIT LICENSE, viewing **LICENSE** file would help you.








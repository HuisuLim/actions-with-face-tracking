# Mouse control by eye tracking
## Introductions
<img src = "./Readme/result.gif">
It provides a camara based eye position tracking system. It **calculate the position of the center of your eyes** to **move your mouse** and  detecting your **eye blinking** to enable various function like **click** or **scroll**.  
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

```python
def detect_face(frame, face_cascade)
```
### detecting eyes
<img src = "./Readme/eye_detect.gif">

```python
def detect_eyes(face_region, eye_cascade)
```

### detecting eye blinking
<img src = "./Readme/blink_detect.gif">

```python
def detect_blink(left_eye, right_eye, frame):
```
### detecting coordinate for eye
<img src = "./Readme/coord_detect.gif">

```python
def coordForEye(face_coord, frame)
```
&nbsp;  
## mouse_control.py
### filtering the noise of x-coordinates of center of eyes
```python
def processingX(a):
```
### filtering the noise of y-coordinates of center of eyes
```python
def processingY(a):
```
### mouse moving rules
```python
def move_mouse_smoothly(left_eye, right_eye)
```
### various operations when eye blinks
```python
def left_blink_op()
```
```python
def right_blink_op()
```
```python
def both_blink_op()
```  
&nbsp;

## Reference
https://github.com/kipr/opencv/tree/master/data/haarcascades
&nbsp;  

## Licensing
This project is released by HuisuLim and following MIT LICENSE.
If you want to get more information, viewing **LICENSE** file would help you.








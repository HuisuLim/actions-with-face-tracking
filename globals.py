import cv2
from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
import os
pyautogui.FAILSAFE = False

script_dir = os.path.dirname(os.path.abspath(__file__))
face_cascade_path = os.path.join(script_dir, 'source', 'haarcascade_frontalface_default.xml')
face_cascade = cv2.CascadeClassifier(face_cascade_path)
eye_cascade_path = os.path.join(script_dir, 'source', 'haarcascade_eye.xml')
eye_cascade = cv2.CascadeClassifier(eye_cascade_path)

# To keep when undetected 
last_left = None
last_right = None

last_left_coords = None
last_right_coords = None

last_detected_face = None
last_detected_face_coords = None


screen_width, screen_height = pyautogui.size()
screen_center_coord = (screen_width // 2, screen_height // 2)

last_center_coords = (screen_center_coord[0], screen_center_coord[1])
prev_center_coords = last_center_coords

#mouse_moving_threshold and sensitivity
movement_threshold = (2,20)
mouse_sensitivity = (15,15)

# to filter noise coordinate changes
my_list_x = [0]
my_list_y = [0]
N = 2
Wn = 0.9
B, A = signal.butter(N, Wn, output='ba')

min_blink_frames = 4
max_blink_frames = 6
left_blink_frame_count = 0
right_blink_frame_count = 0

    



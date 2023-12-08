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


# 눈 감지 경계 설정
movement_threshold = (2,20)  # 설정할 움직임 경계값
mouse_sensitivity = (15,15)

# ... (이전과 동일한 코드)
my_list_x = [0]
my_list_y = [0]
N = 2 # Filter order
Wn = 0.9 # Cutoff frequency
B, A = signal.butter(N, Wn, output='ba')

min_blink_frames = 5
left_blink_frame_count = 0
right_blink_frame_count = 0

    



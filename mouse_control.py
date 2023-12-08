from scipy import signal
import matplotlib.pyplot as plt
import numpy as np
import pyautogui
pyautogui.FAILSAFE = False
from globals import *

def processingX(a):
    global my_list_x, N, Wn, B, A
    if len(my_list_x)-1-a >= 0:
        if len(my_list_x)>9:
            temp=np.array(my_list_x)
            temp = temp.astype(float)
            tempf = signal.filtfilt(B,A, temp)
            lenx = len(tempf)
            return tempf[lenx-1-a]
        else:
            return my_list_x[len(my_list_x)-1-a]
    else:
        return my_list_x[0]

def processingY(a):
    global my_list_y
    if len(my_list_y)-1-a >= 0:
        if len(my_list_y)>9:
            temp=np.array(my_list_y)
            temp = temp.astype(float)
            tempf = signal.filtfilt(B,A, temp)
            leny = len(tempf)
            return tempf[leny-1-a]
        else:
            return my_list_y[len(my_list_y)-1-a]
    else:
        return my_list_y[0]
    
def move_mouse_smoothly(left_eye, right_eye):
    global prev_center_coords, last_center_coords, movement_threshold, mouse_sensitivity
    if left_eye is not None and right_eye is not None:
        new_mouse_x, new_mouse_y = pyautogui.position()
        prev_center_x, prev_center_y = processingX(1), processingY(1)
        current_center_x, current_center_y = processingX(0), processingY(0)
        distance = ((current_center_x - prev_center_x)**2 + (current_center_y - prev_center_y)**2)**0.5
        if distance <50:
            pyautogui.moveTo(new_mouse_x+(current_center_x-prev_center_x)*7, new_mouse_y+(current_center_y-prev_center_y)*7, duration=0.1, tween=pyautogui.easeInOutQuad)

def left_blink_op():
    pyautogui.click(button='left')

def right_blink_op():
    pyautogui.scroll(-10)

def both_blink_op():
    pyautogui.click(button='left')
    


    

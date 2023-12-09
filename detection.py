import cv2
from globals import *

#detect faces to incline eye detecting accuracy
def detect_face(frame, face_cascade):
    global last_detected_face, last_detected_face_coords
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(grey, 1.3, 3)
    largest_area = 0
    largest_face = None
    largest_face_coords = None
    largest_area = 0
    for (x, y, w, h) in faces:
        area = w * h
        if area > largest_area:
            largest_area = area
            largest_face = frame[y:y + h, x:x + w]
            largest_face_coords = (x, y)

    if largest_face is not None:
        cv2.rectangle(frame, (largest_face_coords[0], largest_face_coords[1]),(largest_face_coords[0] + largest_face.shape[1], largest_face_coords[1] + largest_face.shape[0]),(255, 255, 0), 2)
        text = f"face: x={largest_face_coords[0]}, y={largest_face_coords[1]}, w={largest_face.shape[1]}, h={largest_face.shape[0]}"
        cv2.putText(frame, text, (largest_face_coords[0], largest_face_coords[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
        
    last_detected_face = largest_face
    last_detected_face_coords = largest_face_coords

    return last_detected_face, last_detected_face_coords

#detect eyes within a face region
def detect_eyes(face_region, eye_cascade):
    global last_left, last_right, last_left_coords, last_right_coords
    left, right = None, None
    if face_region is not None:
        grey_face = cv2.cvtColor(face_region, cv2.COLOR_BGR2GRAY)
        eyes = eye_cascade.detectMultiScale(grey_face, 1.3, 3)
        for (ex, ey, ew, eh) in eyes:
            #cut face half to increase accurancy
            y_center = ey + (eh / 2)
            if (y_center < (face_region.shape[0] / 2)):
                #find left, right eyes by cutting face in half horizontally
                x_center = ex+(ew/2)
                if (x_center < (face_region.shape[1] / 2)):
                    left = face_region[ey:ey+eh, ex:ex+ew]
                    last_left = left
                    cv2.rectangle(face_region, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)
                    text_left = f"left: x={ex}, y={ey}, w={ew}, h={eh}"
                    cv2.putText(face_region, text_left, (ex, eh+ey+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                    last_left_coords = (x_center, y_center)
                else:
                    right = face_region[ey:ey+eh, ex:ex+ew]
                    last_right = right 
                    cv2.rectangle(face_region, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 2)
                    text_right = f"right: x={ex}, y={ey}, w={ew}, h={eh}"
                    cv2.putText(face_region, text_right, (ex, eh+ey+10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
                    last_right_coords = (x_center, y_center)
        return left, right
    else:
        return left, right
    
def coordForEye(face_coord, frame):
    global last_center_coords, my_list_x, my_list_y, last_left_coords, last_right_coords
    left_x_coord = None
    left_y_coord = None
    left_coord = None
    right_coord = None
    if last_left_coords is not None and last_right_coords is not None:
        left_x_coord = face_coord[0] + last_left_coords[0]
        left_y_coord = face_coord[1] + last_left_coords[1]
        text_left_coord = f"left_eye_center: x={left_x_coord}, y={left_y_coord}"
        cv2.putText(frame, text_left_coord, (0,30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        left_coord = (left_x_coord, left_y_coord)
        right_x_coord = face_coord[0] + last_right_coords[0]
        right_y_coord = face_coord[1] + last_right_coords[1]
        text_right_coord = f"right_eye_center: x={right_x_coord}, y={right_y_coord}"
        cv2.putText(frame, text_right_coord, (0,60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        right_coord = (right_x_coord, right_y_coord)
        center_eye_coord= ((left_coord[0]+right_coord[0])/2,(left_coord[1]+right_coord[1])/2)
        last_center_coords = center_eye_coord
        text_center_coord = f"both eye center coord: x={last_center_coords[0]}, y={last_center_coords[1]}"
        cv2.putText(frame, text_center_coord, (0,90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
        my_list_x.append(last_center_coords[0])
        my_list_y.append(last_center_coords[1])
        return last_center_coords
    else:
        return last_center_coords
    

def detect_blink(left_eye, right_eye, frame):
    global left_blink_frame_count, right_blink_frame_count
    global min_blink_frames, max_blink_frames
    
    left_eye_detected = left_eye is not None
    right_eye_detected = right_eye is not None
    
    if not left_eye_detected:
        left_blink_frame_count += 1
    else:
        left_blink_frame_count = 0
    if not right_eye_detected:
        right_blink_frame_count += 1
    else:
        right_blink_frame_count = 0

    if left_blink_frame_count >= min_blink_frames and max_blink_frames>left_blink_frame_count and right_blink_frame_count >= min_blink_frames and right_blink_frame_count<max_blink_frames:
        text_both_blink = "both blink"
        cv2.putText(frame, text_both_blink, (0,150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
        return 1
    elif left_blink_frame_count >= min_blink_frames and left_blink_frame_count < max_blink_frames:
        text_left_blink = "left blink"
        cv2.putText(frame, text_left_blink, (0,150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
        return 2
    elif right_blink_frame_count >= min_blink_frames and right_blink_frame_count < max_blink_frames:
        text_right_blink = "right blink"
        cv2.putText(frame, text_right_blink, (0,150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 2)
        return 3
    else:
        return -1
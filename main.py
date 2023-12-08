import cv2
from mouse_control import processingX, processingY, move_mouse_smoothly, left_blink_op, right_blink_op, both_blink_op
from detection import detect_face, detect_eyes, coordForEye, detect_blink
from globals import *





# read input image
video_device = 0						
video = cv2.VideoCapture(video_device)
pyautogui.moveTo(855, 553, duration=0.1, tween=pyautogui.easeInOutQuad)

while True:
    _, frame = video.read()
    frame = cv2.flip(frame, 1)
    face_frame, face_coord = detect_face(frame, face_cascade)
    if face_frame is not None:
        left_eye, right_eye = detect_eyes(face_frame, eye_cascade)
        coordForEye(face_coord, frame)
        blink_return = detect_blink(left_eye, right_eye, frame)
        if blink_return == -1:
            move_mouse_smoothly(left_eye, right_eye)
        elif blink_return == 1:
            both_blink_op()
        elif blink_return == 2:
            left_blink_op()
        elif blink_return == 3:
            right_blink_op()

    text_center_coord = f"coord: x={last_center_coords[0]}, y={last_center_coords[1]}"
    cv2.putText(frame, text_center_coord, (0,60), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 0), 2)
    
    # display the resulting frame
    cv2.imshow('Eyes Detection', frame) 

    # break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()


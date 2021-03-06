import cv2
import numpy as np

algo = 'MOG2'
inputt = './data/Background_Subtraction_Tutorial_frame.mp4'

capture = cv2.VideoCapture(cv2.samples.findFileOrKeep(inputt))
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))

out = cv2.VideoWriter('Background_Subtraction_Tutorial_frame_output.mp4',cv2.VideoWriter_fourcc('M','J','P','G'),30, (frame_width,frame_height))

if algo == 'MOG2':
    backSub = cv2.createBackgroundSubtractorMOG2()
else:
    backSub = cv2.createBackgroundSubtractorKNN()


while True:
    
    ret, frame = capture.read()
    
    if frame is None:
        break
    
    fgMask = backSub.apply(frame)
    
    cv2.rectangle(frame, (10, 2), (100,20), (255,255,255), -1)

    cv2.imshow('Frame', frame)
    cv2.imshow('FG Mask', fgMask)
    
    out.write(cv2.cvtColor(fgMask, cv2.COLOR_BGR2RGB))
    
    keyboard = cv2.waitKey(1) & 0xFF;
        
    if (keyboard == 27 or keyboard == ord('q')):
        cv2.destroyAllWindows()
        break;
        
capture.release()
out.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import math
 
capture = cv2.VideoCapture(0)

while (True):
 
    (ret, frame) = capture.read()
 
    grayFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 
    (thresh, blackAndWhiteFrame) = cv2.threshold(grayFrame, 100, 255, cv2.THRESH_TOZERO)
 
    #Takes the OG image and flips on the Y-axis to make it easier to see
    img_inv = cv2.flip(blackAndWhiteFrame, 1)   
    
    '''
    # try to make this work live
    dst_img = cv2.Canny(capture, 50, 200, None, 3)
    lines = cv2.HoughLines(dst_img, 1, np.pi / 180, 150, None, 0, 0)
    for i in range(0, (lines)):
        rho_l = lines[i][0][0]
        theta_l = lines[i][0][1]
        a_l = math.cos(theta_l)
        b_l = math.sin(theta_l)
        x0_l = a_l * rho_l
        y0_l = b_l * rho_l
        pt1_l = (int(x0_l + 1000*(-b_l)), int(y0_l + 1000*(a_l)))
        pt2_l = (int(x0_l - 1000*(-b_l)), int(y0_l - 1000*(a_l)))
        cv2.line(capture, pt1_l, pt2_l, (0,0,255), 3, cv2.LINE_AA)

    cv2.imshow('Lines', capture)
    # ^
    '''
    
    cv2.imshow('video bw', img_inv)
    cv2.imshow('video original', frame)
    
 
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
 
capture.release()
cv2.destroyAllWindows()
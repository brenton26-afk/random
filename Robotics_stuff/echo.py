import cv2
import numpy as np
import math
import time
print("Hello World!")

cap = cv2.VideoCapture(0)

# The line(s) for the other lines to pass over
crossL = 280
crossR = 360

# Sets the resolution of the camera cap
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Define the two windows - not needed.
cv2.namedWindow("Left Camera", cv2.WINDOW_NORMAL)
cv2.namedWindow("Right Camera", cv2.WINDOW_NORMAL)


'''

'''

thresh = None
BandW_frame = None



def process_frame(thisFrame, gray_frame, wSide):
    global thresh, BandW_frame
    blurred_frame = cv2.GaussianBlur(gray_frame, (5,5), 0)
    _, thresholded_frame = cv2.threshold(blurred_frame, 200, 255, cv2.THRESH_BINARY)
    lines = cv2.HoughLinesP(thresholded_frame, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)
    #print(len(lines))
    thresh, BandW_frame = cv2.threshold(gray_frame, 127, 255, cv2.THRESH_BINARY)    #150, 200

    if lines is not None:
        if (wSide == "Left"):
            for line in lines:
                x1, y1, x2, y2 = line[0]
                cv2.line(thisFrame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                if(x1 < crossL) & (crossL < x2) & (y1 > 150) & (y2 > 150):
                    print("Right")
        
        if (wSide == "Right"):
            for line2 in lines:
                x3, y3, x4, y4 = line2[0]
                cv2.line(thisFrame, (x3, y3), (x4, y4), (255, 0, 0), 2)
                if(x3 < crossR - (width_cutoff - 10)) & (crossR - (width_cutoff - 10) < x4) & (y3 > 150) & (y4 > 150):
                    print("Left")
    
    return thisFrame

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    # Makes sure it is working and will close if it does not load
    if not ret:
        break

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Split the frame in half
    height, width = frame.shape[:2]
    width_cutoff = width // 2
    #black_frame = np.zeros((height, width, 3), dtype=np.uint8)
    right_frame = frame[:, width_cutoff-10:]
    left_frame = frame[:, :10+width_cutoff]
    
    #Each direction "arrow"
    cv2.line(left_frame, (crossL, 480), (crossL, 180), (0, 0, 255), 5)
    # Adjust for the different frame
    cv2.line(right_frame, (crossR - (width_cutoff - 10), 480), (crossR  - (width_cutoff - 10), 180), (0, 0, 255), 5)
    

    # Apply the mask
    right_mask = process_frame(right_frame, gray_frame[:, width_cutoff-10:], "Right")
    left_mask = process_frame(left_frame, gray_frame[:, :10+width_cutoff], "Left")
    # Processes the frames again and applies the mask
    processed_right_frame = cv2.cvtColor(right_mask, cv2.THRESH_BINARY_INV)
    processed_left_frame = cv2.cvtColor(left_mask, cv2.THRESH_BINARY_INV)

    #processed_right_frame = cv2.bitwise_and(right_frame, right_mask)
    #processed_left_frame = cv2.bitwise_and(left_frame, left_mask)

    # Calls the process_frame function twice to create the lines
    #processed_right_frame = process_frame(right_frame, gray_frame[:, width_cutoff-10:], "Right")
    #processed_left_frame = process_frame(left_frame, gray_frame[:, :10+width_cutoff], "Left")
    
    # Show each half in its corresponding window
    cv2.imshow("Left Camera", processed_left_frame)
    cv2.imshow("Right Camera", processed_right_frame)
    cv2.imshow("BW", BandW_frame)
    # Exit on Q key press
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

# Release the camera and destroy the windows
cap.release()
cv2.destroyAllWindows()

'''
#finds average light level
def average_light(frame):
    return np.mean(frame)
    
# This creates the frame that should find the lines
# maybe if light level is higher then change threshold
thresh, blackAndWhiteFrame = cv2.threshold(gray_frame, 150, 200, cv2.THRESH_TOZERO)
    
#invert B&W because i want to
img_inv = cv2.flip(blackAndWhiteFrame, 1)


'''

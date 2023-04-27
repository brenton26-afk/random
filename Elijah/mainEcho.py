import cv2
import numpy as np
import math
print("Hello World!")

#find average light level
# when the average light level is found "map" it into another window that will find and detect lines

cap = cv2.VideoCapture(1)

#finds average light level
def average_light(frame):
    return np.mean(frame)


def process_frame(frame):
    blurred_frame = cv2.GaussianBlur(gray_frame, (5,5), 0)

    _, thresholded_frame = cv2.threshold(blurred_frame, 200, 255, cv2.THRESH_BINARY)
    lines = cv2.HoughLinesP(thresholded_frame, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)


    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            if (x2 <= 320) & (y1 > y2) & (x1 > 320) & (x2 < x1):
                print("Left")

            if (x2 >= 320) & (y1 > y2) & (x1 < 320) & (x2 > x1):
                print("Right")  
    
    return frame


while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #This creates the frame that should find the lines
    # maybe if light level is higher then change threshold
    thresh, blackAndWhiteFrame = cv2.threshold(gray_frame, 150, 200, cv2.THRESH_TOZERO)
    
    #invert B&W because i want to
    img_inv = cv2.flip(blackAndWhiteFrame, 1)

    # Vertical direction line: "arrow"
    #>
    height, width, _ = frame.shape
    black_frame = np.zeros((height, width, 3), dtype=np.uint8)
    middle = int(width/2)    
    cv2.line(black_frame, (320, 480), (middle, 180), (255, 0, 0), 5)
    # ^
    
    averageLevel = average_light(frame)
    printLevel = str(averageLevel)
    #print("Average Light Level is: " + printLevel)    

    #finding white line function
    processed_frame = process_frame(black_frame)
    
    #Video windows
    #cv2.imshow('BandW', img_inv)
    
    # A video window that only shows the green lines. Then add a single "arrow" line in the middle pointing forward.
    # Find if the "arrow" intersects a green line for a couple seconds then figure how to change course.
    # Could use angles and math. or map cords ==> if when x1 is smaller than x2 y1 will be higher than y2 straying right.
    cv2.imshow('just lines', black_frame)
    
    #cv2.imshow('OG Video', frame)
    cv2.imshow('other Window', frame)
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


import cv2
import numpy as np
import math
print("Hello World!")

#find average light level
# when the average light level is found "map" it into another window that will find and detect lines

cap = cv2.VideoCapture(1)

#finds average light level
def average_light(frame):
    return np.mean(gray_frame)


def process_frame(frame):
    blurred_frame = cv2.GaussianBlur(gray_frame, (5,5), 0)

    _, thresholded_frame = cv2.threshold(blurred_frame, 200, 255, cv2.THRESH_BINARY)
    lines = cv2.HoughLinesP(thresholded_frame, 1, np.pi / 180, 100, minLineLength=50, maxLineGap=10)

    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line[0]
            cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
    
    return frame


while True:
    ret, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    #This creates the frame that should find the lines
    # maybe if light level is higher then change threshold
    thresh, blackAndWhiteFrame = cv2.threshold(gray_frame, 150, 200, cv2.THRESH_TOZERO)
    
    #invert B&W because i want to
    img_inv = cv2.flip(blackAndWhiteFrame, 1)
    
    averageLevel = average_light(frame)
    printLevel = str(averageLevel)
    print("Average Light Level is: " + printLevel)

    #finding white line function
    processed_frame = process_frame(frame)
    
    #Video windows
    #cv2.imshow('BandW', img_inv)
    #show just lines
    #cv2,imshow('just lines', )
    
    cv2.imshow('OG Video', frame)
    cv2.imshow('other Window', processed_frame)
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np
print("hello world")

#find average light level
# when the average light level is found "map" it into another window that will find and detect lines

cap = cv2.VideoCapture(0)

#finds average light level
def average_light(frame):
    return np.mean(gray_frame)


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
    
    #Video windows
    cv2.imshow('BandW', img_inv)
    cv2.imshow('OG Video', frame)
    
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

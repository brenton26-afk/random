# project echo. Code to get a camera to recognize things. 
# Goal: recognize reflective tape on dark cement.

# import the cv library
import cv2

# video capture object
vid = cv2.VideoCapture(0)

# this should always be running while being tested and used to see what the camera is seeing.
while(True):
      
    # Capture the video frame
    # by frame
    ret, frame = vid.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()


import cv2

white = False

def on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        frame = param
        b, g, r = frame[y, x]
        #print(f"Clicked location: ({x}, {y}), RGB values: ({r:.0f}, {g:.0f}, {b:.0f})")
        red = str(r)
        blue = str(b)
        green = str(g)
        print("RGD: " + red + " " + green + " " + blue)
        if (r > 100) & (b > 100) & (g > 100):
            print("true")
            

cap = cv2.VideoCapture(0)

cv2.namedWindow("Live Video")
while True:
    ret, frame = cap.read()
    
    cv2.setMouseCallback("Live Video", on_mouse_click, frame)

    cv2.imshow("Live Video", frame)
    key = cv2.waitKey(1)
    if key == ord('q') or key == 27:  # Press 'q' or 'ESC' to exit
        break

cap.release()
cv2.destroyAllWindows()

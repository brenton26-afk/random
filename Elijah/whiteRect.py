import cv2
import numpy as np

def find_white_rectangles(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for white
    lower_white = np.array([100, 100, 100])
    upper_white = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_white, upper_white)
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    rectangles = []
    for contour in contours:
        rect = cv2.boundingRect(contour)
        x, y, w, h = rect
        aspect_ratio = w / h

        # Filter for rectangular shapes and a minimum area
        if 0.9 <= aspect_ratio <= 1.1 and cv2.contourArea(contour) > 100:
            rectangles.append(rect)

    # Sort rectangles by area and select the two largest ones
    rectangles.sort(key=lambda x: x[2] * x[3], reverse=True)
    return rectangles[:2]

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        rectangles = find_white_rectangles(frame)
        for rect in rectangles:
            x, y, w, h = rect
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        img_inv = cv2.flip(frame, 1)
        cv2.imshow('Two White Rectangles Detection', img_inv)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:  # Press 'q' or 'ESC' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

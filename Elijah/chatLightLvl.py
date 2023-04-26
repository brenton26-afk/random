import cv2
import numpy as np

def calculate_average_light_level(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    return np.mean(gray_frame)

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot open the camera.")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to read frame.")
            break

        average_light_level = calculate_average_light_level(frame)
        print("Average Light Level: {:.2f}".format(average_light_level))

        cv2.imshow('Live Video', frame)

        key = cv2.waitKey(1)
        if key == ord('q') or key == 27:  # Press 'q' or 'ESC' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

# import the necessary packages
import cv2


def human_detected(frame):
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))

    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))

    if len(boxes) >= 1:
        return True
    else:
        return False

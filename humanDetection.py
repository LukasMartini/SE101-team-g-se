# import the necessary packages
import cv2


def human_detected(frame):
    # initialize the HOG descriptor/person detector
    hog = cv2.HOGDescriptor()
    # Model from [OpenCV Documentation](https://docs.opencv.org/4.x/d5/d33/structcv_1_1HOGDescriptor.html)
    hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))

    # returns the bounding boxes for the detected objects
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    
    # returns true if it detects more than one human
    if len(boxes) >= 1:
        return True
    else:
        return False

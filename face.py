import cv2
import numpy

import frames
import notifications

cascPath = "haarcascade_frontalface_default.xml"
cascade = cv2.CascadeClassifier(cascPath)


def process_frame(frame: numpy.ndarray):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE,
    )

    if len(faces) > 0:
        title = "Face detected"
        message = "Image of person:"
        notifications.send_notification(title, message, frame)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    return frame


if __name__ == "__main__":
    frames.test_model(process_frame)

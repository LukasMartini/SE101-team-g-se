import cv2
import numpy


def encode_frame(frame: numpy.ndarray) -> bytes:
    ret, buffer = cv2.imencode(".jpg", frame)

    if not ret:
        raise Exception("Failed to encode frame")

    return buffer.tobytes()


def new_video_capture() -> cv2.VideoCapture:
    return cv2.VideoCapture(0)


def capture_frame(vc: cv2.VideoCapture) -> numpy.ndarray:
    ret, frame = vc.read()

    if not ret:
        raise Exception("Failed to capture frame")

    return frame

import cv2
import numpy

from camera import capture_frame, new_video_capture


class ModelClass:
    def __init__(self, frame: numpy.ndarray):
        pass

    def process(self, frame: numpy.ndarray):
        pass

    @classmethod
    def test(cls):
        video_capture = new_video_capture()

        while True:
            frame = capture_frame(video_capture)

            model = cls(frame)

            model.process(frame)

            cv2.imshow(f"Testing model {cls.__name__}", frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

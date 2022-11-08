import os
import threading
import time
from multiprocessing.pool import ThreadPool
from typing import Callable

import cv2
import numpy

import face

ACTIVE_FRAME_RATE = 30
INACTIVE_FRAME_RATE = 1

Model = Callable[[numpy.ndarray], numpy.ndarray]


def encode_frame(frame: numpy.ndarray) -> bytes:
    ret, buffer = cv2.imencode(".jpg", frame)

    if not ret:
        raise Exception("Failed to encode frame")

    return buffer.tobytes()


class Camera:
    models: list[Model] = [face.process_frame]

    def __init__(self):
        self.FRAME_RATE = INACTIVE_FRAME_RATE
        self.frame: numpy.ndarray
        self.last_gen = time.time()
        self.last_capture = time.time()
        self.last_access = time.time()
        self.video_capture = self.new_video_capture()

        num_models = len(self.models)
        os_cores = os.cpu_count() or 1

        num_threads = min(os_cores, num_models)
        print(f"Using {num_threads} threads")

        self.pool = ThreadPool(num_threads)

        threading.Thread(target=self._thread).start()

        print("Waiting for first frame...")

        while True:
            if hasattr(self, "frame"):
                print("Received first frame.")
                break

            time.sleep(0.1)

    @staticmethod
    def new_video_capture() -> cv2.VideoCapture:
        return cv2.VideoCapture(0)

    @staticmethod
    def capture_frame(vc: cv2.VideoCapture) -> numpy.ndarray:
        ret, frame = vc.read()

        if not ret:
            raise Exception("Failed to capture frame")

        return frame

    @staticmethod
    def format_frame_for_web(frame: bytes):
        return b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n"

    @staticmethod
    def pool_error(e: BaseException):
        print(e)

    def gen_web(self):
        while True:
            self.last_access = time.time()
            if self.FRAME_RATE != ACTIVE_FRAME_RATE:
                print(f"Accessed, entering active mode")
                self.FRAME_RATE = ACTIVE_FRAME_RATE

            while self.last_gen == self.last_capture:
                time.sleep(0.01)

            self.last_gen = self.last_capture
            frame_bytes = encode_frame(self.frame)

            yield self.format_frame_for_web(frame_bytes)

    def _thread(self):
        while True:
            frame = self.capture_frame(self.video_capture)

            if (time.time() - self.last_capture) > (1 / self.FRAME_RATE):
                self.frame = frame
                self.last_capture = time.time()

                if time.time() - self.last_access > 10:
                    if self.FRAME_RATE != INACTIVE_FRAME_RATE:
                        print(f"No access for 10s, entering inactive mode")
                        self.FRAME_RATE = INACTIVE_FRAME_RATE

                if len(self.pool._cache) == 0:  # type: ignore
                    for model in self.models:
                        self.pool.apply_async(
                            model, (frame,), error_callback=self.pool_error
                        )


def test_model(model: Model):
    video_capture = Camera.new_video_capture()

    while True:
        frame = Camera.capture_frame(video_capture)

        model(frame)

        cv2.imshow("Video", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

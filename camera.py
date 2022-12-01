import copy
import os
import threading
import time
from multiprocessing.pool import ThreadPool

import numpy

import playSound
from frames import capture_frame, encode_frame, new_video_capture

ACTIVE_FRAME_RATE = 60
INACTIVE_FRAME_RATE = 1


class Camera:
    def __init__(self, models):
        self.FRAME_RATE = INACTIVE_FRAME_RATE
        self.models = []
        self.frame: numpy.ndarray
        self.last_gen = time.time()
        self.last_capture = time.time()
        self.last_access = time.time()
        self.video_capture = new_video_capture()

        num_models = len(models) + 2
        os_cores = os.cpu_count() or 1

        num_threads = min(os_cores, num_models)
        print(f"Using {num_threads} threads")

        self.pool = ThreadPool(num_threads)

        threading.Thread(target=self._thread).start()

        try:
            self.pool.apply_async(playSound.playsound)
        except AttributeError:
            print("rip no button x2")

        print("Waiting for first frame...")

        while True:
            if hasattr(self, "frame"):
                print("Received first frame.")
                break

            time.sleep(0.1)

        for model in models:
            model = model(self.frame)
            self.models.append(model)

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
                print("Accessed, entering active mode")
                self.FRAME_RATE = ACTIVE_FRAME_RATE

            while self.last_gen == self.last_capture:
                time.sleep(0.01)

            self.last_gen = self.last_capture
            frame_bytes = encode_frame(self.frame)

            yield self.format_frame_for_web(frame_bytes)

    def _thread(self):
        while True:
            frame = capture_frame(self.video_capture)

            if (time.time() - self.last_capture) > (1 / self.FRAME_RATE):
                self.frame = frame
                self.last_capture = time.time()

                if time.time() - self.last_access > 10:
                    if self.FRAME_RATE != INACTIVE_FRAME_RATE:
                        print("No access for 10s, entering inactive mode")
                        self.FRAME_RATE = INACTIVE_FRAME_RATE

                if len(self.pool._cache) == 0:  # type: ignore
                    for model in self.models:
                        self.pool.apply_async(
                            model.process,
                            (copy.deepcopy(frame),),
                            error_callback=self.pool_error,
                        )

from typing import Optional

import httpx
import numpy

from frames import encode_frame
from limiter import limit

PUSHOVER_TOKEN = "apacy68n1q58vv9mhe9h88yj35joef"
PUSHOVER_USER = "ug4q55gv4gnmbt1t4h2bbvfq9enzy8"

client = httpx.Client()


@limit(30)
def send_notification(title: str, message: str, frame: Optional[numpy.ndarray] = None):
    print("Sending notification")

    if frame is not None:
        frame_bytes = encode_frame(frame)
        files = {"attachment": ("image.jpeg", frame_bytes, "image/jpeg")}
    else:
        files = {}

    data = {
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER,
        "title": title,
        "message": message,
    }

    res = client.post(
        "https://api.pushover.net/1/messages.json",
        data=data,
        files=files,
    )

    res.raise_for_status()

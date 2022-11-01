import requests

PUSHOVER_TOKEN = "apacy68n1q58vv9mhe9h88yj35joef"
PUSHOVER_USER = "ug4q55gv4gnmbt1t4h2bbvfq9enzy8"


def send_notification(title: str, message: str):
    post_data = {
        "token": PUSHOVER_TOKEN,
        "user": PUSHOVER_USER,
        "title": title,
        "message": message,
    }

    requests.post("https://api.pushover.net/1/messages.json", json=post_data)

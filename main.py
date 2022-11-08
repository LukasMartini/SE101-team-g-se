from flask import Flask
from flask.wrappers import Response

from frames import Camera

app = Flask(__name__)
camera = Camera()


def main():
    app.run(port=8080)


@app.route("/")
def index():
    mime_type = "multipart/x-mixed-replace; boundary=frame"
    return Response(camera.gen_web(), mimetype=mime_type)


if __name__ == "__main__":
    main()

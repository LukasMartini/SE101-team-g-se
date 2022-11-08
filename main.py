from flask import Flask
from flask.wrappers import Response

from camera import Camera
from face import FaceModel
from motionDet import MotionModel

models = [FaceModel,MotionModel]

app = Flask(__name__)
camera = Camera(models)


def main():
    app.run(port=8080)


@app.route("/")
def index():
    mime_type = "multipart/x-mixed-replace; boundary=frame"
    return Response(camera.gen_web(), mimetype=mime_type)


if __name__ == "__main__":
    main()

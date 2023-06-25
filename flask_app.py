import argparse
import io
from PIL import Image
import os
import torch
from flask import Flask, render_template, request, redirect
from keras.applications.imagenet_utils import preprocess_input
from tensorflow.keras.models import load_model
from flask import Flask, render_template, request, redirect, flash, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if not file:
            return
        img_bytes = file.read()
        img = Image.open(io.BytesIO(img_bytes))
        results = model(img)  # inference
        results.render()  # updates results.ims with boxes and labels
        Image.fromarray(results.ims[0]).save("static/images/image0.jpg")
        return redirect("static/images/image0.jpg")

    return render_template("index.html")
if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5000, type=int, help="port number")
    args = parser.parse_args()

    model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
    model.eval()

    app.run(host="0.0.0.0", port=args.port)
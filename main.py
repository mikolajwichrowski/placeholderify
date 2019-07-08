#!/usr/local/bin/python3

import sys
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from util.fileSaver import generate_from_img
from util.Size import Size
from util.Color import Color
from util.Placeholder import Placeholder

app = Flask(__name__)

@app.route('/')
def index():
    return send_file(
        "images/{}".format(Placeholder(
            Size(
                width = int(str(request.args.get('size')).split("x", 1)[0]),
                height = int(str(request.args.get('size')).split("x", 1)[1])
            ),
            str(request.args.get('text')),
            Color(
                str(request.args.get('fore'))
            ),
            Color(
                str(request.args.get('back'))
            ),
            int(request.args.get('font'))
        ).name
    ), mimetype='image/png')

if __name__ == "__main__":
    # You can change port here
    app.run(debug=True, host='127.0.0.1', port=5000) 
#!/usr/local/bin/python3

import sys
from flask import Flask, request, send_file
from PIL import Image, ImageDraw, ImageFont
from util.file_saver import generate_from_img
from util.size import Size
from util.color import Color

class Program:
    def __init__(self, size, text, foreColor, backColor, fontSize):
        # Init canvas size
        self.width = size.width
        self.height = size.height

        # Show image
        self.img = Image.new('RGB', (self.width, self.height), (backColor.r, backColor.g, backColor.b)) 
        self.draw = ImageDraw.Draw(self.img)

        # Draw text
        self.draw_text(text, foreColor, fontSize)

        # Generate file from img
        self.name = "{}{}{}{}{}.png".format(size, text, foreColor, backColor, fontSize)
        generate_from_img(self.img, self.name)

        # Debug show
        # self.img.show()

    def draw_text(self, text, foreColor, fontSize):
        # Set font
        self.font = ImageFont.truetype("Montserrat-Regular.ttf", fontSize)

        # Set text in center
        text_x, text_y = self.font.getsize(text)
        x = (self.width - text_x)/2
        y = (self.height - text_y)/2

        # Draw text
        self.draw.text(xy=(x, y), text=text, font=self.font, fill=(foreColor.r, foreColor.g, foreColor.b))

def placeholderify(textString, fontSizeString, sizeString, foreColorString, backColorString):
    print(sizeString)
    p = Program(
        Size(
            width = int(str(sizeString).split("x", 1)[0]),
            height = int(str(sizeString).split("x", 1)[1])
        ),
        str(textString),
        Color(
            str(foreColorString)
        ),
        Color(
            str(backColorString)
        ),
        int(fontSizeString)
    )
    return p.name

app = Flask(__name__)

@app.route('/')
def index():
    return send_file(
        placeholderify(
            request.args.get('text'), 
            request.args.get('font'), 
            request.args.get('size'), 
            request.args.get('fore'), 
            request.args.get('back')
        ), mimetype='image/png')

if __name__ == "__main__":
    # You can change port here
    app.run(debug=True, host='127.0.0.1', port=5000) 
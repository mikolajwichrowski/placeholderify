from PIL import Image, ImageDraw, ImageFont
from util.fileSaver import generate_from_img
from util.Size import Size
from util.Color import Color

class Placeholder:
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
        self.font = ImageFont.truetype("fonts/Montserrat-Regular.ttf", fontSize)

        # Set text in center
        text_x, text_y = self.font.getsize(text)
        x = (self.width - text_x)/2
        y = (self.height - text_y)/2

        # Draw text
        self.draw.text(xy=(x, y), text=text, font=self.font, fill=(foreColor.r, foreColor.g, foreColor.b))
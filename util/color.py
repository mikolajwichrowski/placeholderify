import struct
import codecs
import webcolors

class Color:
    def __init__(self, hexString):
        rgb = webcolors.html5_parse_legacy_color(hexString)
        self.r = rgb.red
        self.g = rgb.green
        self.b = rgb.blue
        
    def __repr__(self):
        return "{}{}{}".format(self.r, self.g, self.b)
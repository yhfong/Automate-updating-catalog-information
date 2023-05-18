#!/usr/bin/env python3

import os
import re
from PIL import Image

size = (600, 400)
old_path = "supplier-data/images/"
new_path = "supplier-data/images/"
format = "jpeg"

# Covert the image to "RGB" format, resize the input image to 600x400 pixel and image format to .JPEG
# Use regular expression to obtain the filename
for infile in os.listdir(old_path):
    try:
        with Image.open(old_path + infile) as im:
            new_img = im.resize(size).convert("RGB")
            filename = re.findall(r'([0-9]+)', infile)
            new_img.save(new_path + filename[0] + ".jpeg")
    except OSError:
        print("Cannot convert ", infile)
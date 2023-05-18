#!/usr/bin/env python3

import requests
import os

# Using the Python Requests module to upload all the JPEG file to the following URL

url = "http://localhost/upload/"
path = "supplier-data/images/"

for infile in os.listdir(path):
    root_ext = os.path.splitext(infile)

    if root_ext[1] == ".jpeg":
        with open(path + infile, 'rb') as opened:
            r = requests.post(url, files={'file': opened})
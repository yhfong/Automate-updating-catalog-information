#! /usr/bin/env python3

import os
import requests
import re

# Read the information from txt file and upload the information with linkage to JPEG to the following URL
path = "supplier-data/descriptions/"
url = "http://localhost/fruits/"

for file in os.listdir(path):
    content_title = ["name", "weight", "description", "image_name"]
    content = {}
# Read the information from txt file to a list of content
    with open(path+'/'+file, "r") as f:
        position = 0
        for line in f:
            content[content_title[position]] = line.rstrip('\n')
            position += 1
# Covert weight content into integer and drops the unit
        if not content["weight"].isdigit():
            weight = content["weight"]
            weight_no = re.findall(r'([0-9]+)', weight)
            content["weight"] = weight_no[0]
# Upload the text from the list with the according to uploaded JPEG file name
        root_ext = os.path.splitext(file)
        content["image_name"] = root_ext[0]+".jpeg"
        response = requests.post(url, json=content)

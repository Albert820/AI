from PIL import Image
from os import listdir
from os.path import isfile, join
import re

import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        name_path = os.path.join(root, name)
#        print(name_path)
        image = Image.open(name_path)
        filename = re.findall(".*\.", name_path)
#        print(filename[0])
        image = image.convert('RGB')
        image.save(filename[0]+"jpg")
#    for name in dirs:
#        print(os.path.join(root, name))

"""
onlyfiles = [f for f in listdir("./labeled_image") if isfile(join("./labeled_image", f))]
#print(onlyfiles)

for filename in onlyfiles:
#    print(filename)
#    print(str(filename)+".test")
    image = Image.open("labeled_image/"+filename)
    filename = re.findall(".*\.", filename)
    print(filename[0])
    image = image.convert('RGB')
    image.save("labeled_image_jpg/"+filename[0]+"jpg")
"""

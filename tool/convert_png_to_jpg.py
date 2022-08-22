from PIL import Image
from os import listdir
from os.path import isfile, join
import re

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

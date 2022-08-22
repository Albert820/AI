from PIL import Image
from os import listdir
from os.path import isfile, join
import re
import cv2

onlyfiles = [f for f in listdir("./SegmentationObjectPNG_jpg/") if isfile(join("./SegmentationObjectPNG_jpg/", f))]
#print(onlyfiles)

for filename in onlyfiles:
    print(filename)
#    print(str(filename)+".test")
    #image = Image.open("SegmentationObjectPNG_jpg/"+filename)
    image = cv2.imread('SegmentationObjectPNG_jpg/'+filename)
    filename = re.findall(".*\.", filename)
    print(filename[0])
    #image = image.convert('RGB')
    image8 = (image/256).astype('uint8')
    image8 = Image.fromarray(image8)
    image8.save("8_bits_SegmentationObjectPNG/"+filename[0]+"jpg")






#img8 = (img16/256).astype('uint8')

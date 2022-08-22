import os
import shutil
import re
import math


# folder path
dir_path = os.getcwd()
dst = "./test/"

_image = "NULL"
images = list()

#train_dir_path = dir_path + "/train_data"
#image_folder = '/home/cheng/dir_for_label_data/gopro/clearer_image/left_cut_pic'

for img in os.listdir(dir_path):
#    print(img)
    if img.endswith(".json"):
#        print(img)
        filename = re.findall(".*[^\.json]", img)
        images.append(filename[0])
        """
        if int(filename[0]) >= 1600 and int(filename[0]) <= 19692:
            images.append(filename[0])
            if _image == "NULL":
                _image = img
        """

images.sort(key=int)
#print(_json_filename)
#"""
#print(image_files)
# Iterate directory
index = 0
frame_count = 0

for image in images:
#    os.makedirs(train_dir_path + "/" + directory)
    shutil.copyfile(image + ".png", dst + image + ".png")
    shutil.copyfile(image + ".json", dst + image + ".json")
#    print(dir_path + "/" + _json_file + "/" + "img.png")
    # check if current path is a file
#    print(dir_path)
#    print(path)



import os
import shutil
import re
import math


# folder path
dir_path = os.getcwd()
dir_path = dir_path + "/test"
#dir_path = "/home/cheng/Mask_RCNN_GPU_train_on_coco_dataset/instance_segmentationt_data/train_data"
dir2_path = "/mnt/lab603/Longdiann/20220504/left/first/count/pic"
dst = "./test/"

_image = "NULL"
images = list()
images2 = list()

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

for img in os.listdir(dir2_path):
#    print(img)
    if img.endswith(".json"):
#        print(img)
        filename = re.findall(".*[^\.json]", img)
        images2.append(filename[0])
        """
        if int(filename[0]) >= 1600 and int(filename[0]) <= 19692:
            images.append(filename[0])
            if _image == "NULL":
                _image = img
        """

images.sort(key=int)
images2.sort(key=int)
"""
print(images)
print()
print(images2)
"""
for val in images[:]:
    for val2 in images2:
        if val == val2:
            print("duplication: " + val)
            images.remove(val)

#print(images)
#print(_json_filename)
#"""
#print(image_files)
# Iterate directory
index = 0
frame_count = 0
"""
for image in images:
#    os.makedirs(train_dir_path + "/" + directory)
    shutil.copyfile(image + ".png", dst + image + ".png")
    shutil.copyfile(image + ".json", dst + image + ".json")
"""
#    print(dir_path + "/" + _json_file + "/" + "img.png")
    # check if current path is a file
#    print(dir_path)
#    print(path)



import os
import shutil
import re
import math

if not os.path.exists("train_data_multi_dir_2"):
    os.makedirs("train_data_multi_dir_2")

# folder path
dir_path = os.getcwd()

_image = "NULL"
_image2 = "NULL"
images = list()
images_right = list()

train_dir_path = dir_path + "/train_data_multi_dir_2"
image_folder = '/home/cheng/dir_for_label_data/gopro/clearer_image/left_cut_pic'
right_image_folder = '/home/cheng/dir_for_label_data/gopro/clearer_image/right_cut_pic'

for img in os.listdir(image_folder):
#    print(img)
    if img.endswith(".png"):
#        print(img)
        filename = re.findall(".*[^\.png]", img)
        #"""
        if int(filename[0]) >= 8400 and int(filename[0]) <= 19715:
            images.append(filename[0])
            if _image == "NULL":
                _image = img
        #"""
        """
        images.append(filename[0])
        if _image == "NULL":
            _image = img
        """

for img in os.listdir(right_image_folder):
#    print(img)
    if img.endswith(".png"):
#        print(img)
        filename = re.findall(".*[^\.png]", img)
        #"""
        if int(filename[0]) >= 8400 and int(filename[0]) <= 19715:
            images.append(filename[0])
            if _image == "NULL":
                _image = img
        #"""
        """
        images_right.append(filename[0])
        if _image2 == "NULL":
             _image2 = img
        """


images.sort(key=int)
images_right.sort(key=int)
#print(_json_filename)
#"""
#print(image_files)
# Iterate directory
index = 0
frame_count = 0
stride = 0
dir_count = 0

for image in images:
    stride += 1
    index += 1
    frame_count += 1

    print(dir_count)
    """
    print("index: " + str(index))
    print()
    print("frame_count: " + str(frame_count))
    """
    if frame_count == 3:
#        print("frame_count: " + str(frame_count))
#        directory = str(math.ceil(index/3))
        dir_count += 1
        directory = str(dir_count)
        os.makedirs(train_dir_path + "/" + directory)
        shutil.copyfile(image_folder + "/" + images[index-3] + ".png", train_dir_path + "/" + directory + "/" + "frame0.png")
        shutil.copyfile(image_folder + "/" + images[index-2] + ".png", train_dir_path + "/" + directory + "/" + "frame1.png")
        shutil.copyfile(image_folder + "/" + images[index-1] + ".png", train_dir_path + "/" + directory + "/" + "frame2.png")
        frame_count = 0

index = 0
frame_count = 0
stride = 0

for image in images_right:
    stride += 1
    index += 1
    frame_count += 1

    print("right_dir: " +str(dir_count))
    """
    print("index: " + str(index))
    print()
    print("frame_count: " + str(frame_count))
    """
    if frame_count == 3:
#        print("frame_count: " + str(frame_count))
#        directory = str(math.ceil(index/3))
        dir_count += 1
        directory = str(dir_count)
        os.makedirs(train_dir_path + "/" + directory)
        shutil.copyfile(right_image_folder + "/" + images_right[index-3] + ".png", train_dir_path + "/" + directory + "/" + "frame0.png")
        shutil.copyfile(right_image_folder + "/" + images_right[index-2] + ".png", train_dir_path + "/" + directory + "/" + "frame1.png")
        shutil.copyfile(right_image_folder + "/" + images_right[index-1] + ".png", train_dir_path + "/" + directory + "/" + "frame2.png")
        frame_count = 0

#    print(dir_path + "/" + _json_file + "/" + "img.png")
    # check if current path is a file
#    print(dir_path)
#    print(path)



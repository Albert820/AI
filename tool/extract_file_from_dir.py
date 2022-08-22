import os
import shutil
import re
import math

if not os.path.exists("extract_dir"):
    os.makedirs("extract_dir")

# folder path
dir_path = os.getcwd()
save_img_dir = dir_path + "/extract_dir"

#_image = "NULL"
#images = list()

dirs_list = list()
save_index = 0

#train_dir_path = dir_path + "/train_data_optical_flow_A13"
image_folder = dir_path + '/train_LNG0401_1frame'

for key, dirs in enumerate(os.listdir(image_folder)):
    print(key)
    dirs_list.append(key)
    for img in os.listdir(image_folder + "/" + str(key)):
        print(img)
        save_index += 1
        shutil.copyfile(image_folder + "/" + str(key)+ "/" +img, save_img_dir + "/" + str(save_index) + ".jpg")


#    print(img)i
    """
    if img.endswith(".png"):
#        print(img)
        filename = re.findall(".*[^\.png]", img)
        images.append(filename[0])
        '''
        if int(filename[0]) >= 1600 and int(filename[0]) <= 19692:
            images.append(filename[0])
            if _image == "NULL":
                _image = img
        '''
    """

#print(dirs_list)
#images.sort(key=int)
#print(_json_filename)
#"""
#print(image_files)
# Iterate directory

"""
index = 0
frame_count = 0

for image in images:
    frame_count += 1
    index += 1
    '''
    print("index: " + str(index))
    print()
    print("frame_count: " + str(frame_count))
    '''
    if frame_count == 3:
#        print("frame_count: " + str(frame_count))
        directory = str(math.ceil(index/3))
        os.makedirs(train_dir_path + "/" + directory)
        shutil.copyfile(image_folder + "/" + images[index-3] + ".png", train_dir_path + "/" + directory + "/" + "frame0.png")
        shutil.copyfile(image_folder + "/" + images[index-2] + ".png", train_dir_path + "/" + directory + "/" + "frame1.png")
        shutil.copyfile(image_folder + "/" + images[index-1] + ".png", train_dir_path + "/" + directory + "/" + "frame2.png")
        frame_count = 0
#    print(dir_path + "/" + _json_file + "/" + "img.png")
    # check if current path is a file
#    print(dir_path)
#    print(path)
"""

import os
import shutil
import re

# folder path
root_dir = os.getcwd()

dir_image_path = root_dir + "/image"
dst_image_val_path = root_dir + "/image_val"

dir_yaml_path = root_dir + "/yaml"
dst_yaml_val_path = root_dir + "/yaml_val"

dir_label_path = root_dir + "/label"
dst_label_val_path = root_dir + "/label_val"

if not os.path.exists("image_val"):
    os.makedirs("image_val")

if not os.path.exists("yaml_val"):
    os.makedirs("yaml_val")

if not os.path.exists("label_val"):
    os.makedirs("label_val")

#"""
count = 0
# Iterate directory
for path in os.listdir(dir_image_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(dir_image_path, path)):
        count += 1
print('File count:', count)

count_val = int(count * 0.3)

file_timer = 0
print("count_val: " + str(count_val))
for path in os.listdir(dir_image_path):
    print(path)
    # check if current path is a file
    if file_timer != count_val:
        shutil.move(dir_image_path +"/"+ path, dst_image_val_path)
        file_timer += 1
    else:
        break
#"""
#count_val = 54
file_timer = 0
#"""
for path in os.listdir(dst_image_val_path):
    print(path)
    filename = re.findall(".*\.", path)
    yaml_filename = filename[0]+"yaml"
    print(yaml_filename)
    # check if current path is a file
    if file_timer != count_val:
        shutil.move(dir_yaml_path +"/"+ yaml_filename, dst_yaml_val_path)
        file_timer += 1
    else:
        break
#"""

file_timer = 0
for path in os.listdir(dst_image_val_path):
    print(path)
    filename = re.findall(".*\.", path)
    label_filename = filename[0]+"png"
    print(label_filename)
    # check if current path is a file
    if file_timer != count_val:
        shutil.move(dir_label_path +"/"+ label_filename, dst_label_val_path)
        file_timer += 1
    else:
        break



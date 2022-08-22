import os
import shutil
import re

if not os.path.exists("train_data"):
    os.makedirs("train_data")

# folder path
dir_path = os.getcwd()

train_dir_path = dir_path + "/train_data"
original_dir_path = dir_path + "/left_cut_pic"

json_filenames = [pos_json for pos_json in os.listdir(original_dir_path) if pos_json.endswith('.json')]
#print(_json_filename)
#"""
#print(image_files)
# Iterate directory
for json_file in json_filenames:
    json_filename = re.findall(".*\.", json_file)

    shutil.copyfile(original_dir_path + "/" + json_filename[0] + "png", train_dir_path + "/" + json_filename[0]  + "png")
    shutil.copyfile(original_dir_path + "/" + json_filename[0] + "json", train_dir_path + "/" + json_filename[0]  + "json")

#    print(dir_path + "/" + _json_file + "/" + "img.png")
    # check if current path is a file
#    print(dir_path)
#    print(path)



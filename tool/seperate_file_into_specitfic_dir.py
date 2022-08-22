import os
import shutil
import re

if not os.path.exists("image"):
    os.makedirs("image")

if not os.path.exists("label"):
    os.makedirs("label")

if not os.path.exists("label_viz"):
    os.makedirs("label_viz")

if not os.path.exists("yaml"):
    os.makedirs("yaml")

# folder path
dir_path = os.getcwd()

image_dir_path = dir_path + "/image"
label_dir_path = dir_path + "/label"
label_viz_dir_path = dir_path + "/label_viz"
yaml_dir_path = dir_path + "/yaml"


_json_filename = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('_json')]
#print(_json_filename)
#"""
image_files = [pos_json for pos_json in os.listdir(image_dir_path) if pos_json.endswith('img.png')]
#print(image_files)
# Iterate directory
for _json_file in _json_filename:
    shutil.copyfile(dir_path + "/" + _json_file + "/" + "img.png", image_dir_path + "/" + _json_file + ".png")
    shutil.copyfile(dir_path + "/" + _json_file + "/" + "label.png", label_dir_path + "/" + _json_file + ".png")
    shutil.copyfile(dir_path + "/" + _json_file + "/" + "label_viz.png", label_viz_dir_path + "/" + _json_file + ".png")
    shutil.copyfile(dir_path + "/" + _json_file + "/" + "info.yaml", yaml_dir_path + "/" + _json_file + ".yaml")

#    print(dir_path + "/" + _json_file + "/" + "img.png")
    # check if current path is a file
#    print(dir_path)
#    print(path)



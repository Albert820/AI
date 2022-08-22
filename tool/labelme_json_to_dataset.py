import os
import shutil
import re

# folder path
dir_path = os.getcwd()
#"""
json_files = [pos_json for pos_json in os.listdir(dir_path) if pos_json.endswith('.json')]
print(json_files)
# Iterate directory
for path in json_files:
    # check if current path is a file
    print(dir_path)
    print(path)
    os.system("labelme_json_to_dataset " + dir_path + "/" + path)

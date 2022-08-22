import os
import shutil
import re

if not os.path.exists("train_data"):
    os.makedirs("train_data")

if not os.path.exists("validation_data"):
    os.makedirs("validation_data")

dir_path = os.getcwd()

train_dir_path = dir_path + "/train_data"
validation_dir_path = dir_path + "/validation_data"

#"""
count = 0
# Iterate directory
for path in os.listdir(train_dir_path):
    # check if current path is a file
    if os.path.isfile(os.path.join(train_dir_path, path)):
        if path.endswith('.json'):
            count += 1
print('File count:', count)

count_val = int(count * 0.3)

file_timer = 0
print("count_val: " + str(count_val))
for path in os.listdir(train_dir_path):
#    print(path)
    filename = re.findall(".*\.", path)
    # check if current path is a file
    if file_timer != count_val:
        if path.endswith('.json'):
            #print(path)
            #print(filename[0] + "png")
            shutil.move(train_dir_path +"/"+ path, validation_dir_path)
            shutil.move(train_dir_path +"/"+ filename[0] + "png", validation_dir_path)
            file_timer += 1
    else:
        break

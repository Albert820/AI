import json
import os
import shutil
import re
import math


# folder path
dir_path = os.getcwd()
dst = "./test/"

_image = "NULL"
images = list()



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

# Opening JSON file

for image in images:

    f = open(image+'.json')

# returns JSON object as 
# a dictionary
    data = json.load(f)

# Iterating through the json
# list
#    print(data['label'])
    for val in data["shapes"]:
        if val['label'] == "Spotted _knife_face":
            val['label'] = "Spotted _knifejaw_face"
        elif val['label'] == "Spotted _knife_side":
            val['label'] = "Spotted _knifejaw_side"

    with open(image + '.json', 'w') as f2:
        json.dump(data, f2)

#        print(val['label'])
#        print(image)
#        shutil.copyfile(dir_path + "/" + image + ".png", "./train_data/" + image + ".png")
#        shutil.copyfile(dir_path + "/" + image + ".json", "./train_data/" + image + ".json")

# Closing file
f.close()

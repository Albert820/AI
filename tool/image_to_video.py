import cv2
import os
import re

#image_folder = 'svo_left'
#video_name = 'svo_left_video.avi'
image_folder = './extract_dir'
video_name = './extract_dir.avi'

_image = "NULL"

images = list()

for img in os.listdir(image_folder):
#    print(img)
#    if img.endswith(".png"):
    if img.endswith(".jpg"):
#        print(img)
#        filename = re.findall(".*[^\.png]", img)
        filename = re.findall(".*[^\.jpg]", img)
        """
        if int(filename[0]) >= 1600 and int(filename[0]) <= 19692:
            images.append(filename[0])
            if _image == "NULL":
                _image = img
        """
        images.append(filename[0])
        if _image == "NULL":
            _image = img

#    print(filename[0])
#    images = [img for img in os.listdir(image_folder) if img.endswith(".png") and (int(filename[0]) >= 1600 and int(filename[0]) <= 19692)]


"""
for val in images:
    print(val)
"""

frame = cv2.imread(os.path.join(image_folder, _image))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30.0, (width,height))
images.sort(key=int)
print(images)

for image in images:
#    video.write(cv2.imread(os.path.join(image_folder, image + ".png")))
    video.write(cv2.imread(os.path.join(image_folder, image + ".jpg")))

cv2.destroyAllWindows()
video.release()

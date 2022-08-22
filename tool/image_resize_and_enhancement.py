#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image
import numpy as np
import cv2

img = cv2.imread('frame11.png')
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
R, G, B = cv2.split(img)
output1_R = clahe.apply(R)
output1_G = clahe.apply(G)
output1_B = clahe.apply(B)
img = cv2.merge((output1_R, output1_G, output1_B))
cv2.imwrite('frame11.png',img)

img = cv2.imread('frame10.png')
# create a CLAHE object (Arguments are optional).
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
R, G, B = cv2.split(img)
output1_R = clahe.apply(R)
output1_G = clahe.apply(G)
output1_B = clahe.apply(B)
img = cv2.merge((output1_R, output1_G, output1_B))
cv2.imwrite('frame10.png',img)


img = Image.open("frame11.png")
(w, h) = img.size
print('w=%d, h=%d', w, h)
img.show()

new_img = img.resize((640, 480))
new_img.show()
new_img.save("frame11.png")

img = Image.open("frame10.png")
(w, h) = img.size
print('w=%d, h=%d', w, h)
img.show()

new_img = img.resize((640, 480))
new_img.show()
new_img.save("frame10.png")

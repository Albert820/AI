#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from PIL import Image

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

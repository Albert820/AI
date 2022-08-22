import cv2
vidcap = cv2.VideoCapture('/home/cheng/dir_for_label_data/龍佃/0407/gopro/0408/左/GH031772.MP4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("/home/cheng/dir_for_label_data/left_cut_pic/%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1

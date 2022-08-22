#!/usr/bin/env python
# coding: utf-8

# # 左影像

# In[ ]:


#gopro每秒30frame，每部影片21209frame
#左影像
import cv2
import numpy as np

def no(x):
    pass
def set_frame_number(x):
    global frame_num
    frame_num = x
    return

cap = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/龍佃/0407/gopro/0408/右/GH031776.MP4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter(r'C:\Users\cheng\Desktop\實地審核\right.mp4',fourcc, 30.0, (1920,1080))

total_frame= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_num = 17 # 3915: 16:53:26.42    第一張:16.15.59
k=0
#cv2.namedWindow('frame')
cv2.createTrackbar('frame no.','frame',0,total_frame-1,set_frame_number)
cv2.setTrackbarPos('frame no.','frame',frame_num)  
cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)


while(True):
    try:
        ret,frame = cap.read()
        frame2 = frame[:1080,:]       
        frame3 = cv2.resize(frame2,(960,540))
        #cv2.setTrackbarPos('frame no.','frame',frame_num)  
        #cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        cv2.imshow('frame',frame3)
        if cv2.waitKey(1) &0xFF ==ord('q'):
            cv2.destroyAllWindows()
            break
    except:
        print(k)
        k+=1
        pass
    if(k%1==0):
        try:
            cv2.imwrite(r"/home/cheng/dir_for_label_data/right_cut_pic/%s.png"%k, frame2)
        except:
            pass
    frame_num+=1
    k+=1


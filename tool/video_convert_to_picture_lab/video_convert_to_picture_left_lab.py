#!/usr/bin/env python
# coding: utf-8

# # 左影像

# In[6]:


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

cap = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/gopro/龍佃/0407/gopro/20220407/左/GH011773.MP4")
#cap2 = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/gopro/龍佃/0407/gopro/20220407/右/GH011769.MP4")
#cap = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/gopro/clearer_image/left_cut_pic.avi")
#cap = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/gopro/clearer_image/n.mp4")
#cap2 = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/gopro/clearer_image/n2.mp4")
#cap2 = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/gopro/clearer_image/right_cut_pic.avi")
#cap2 = cv2.VideoCapture(r"/home/cheng/dir_for_label_data/龍佃/0407/gopro/0408/左/GH031772.MP4")

fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter(r'C:\Users\cheng\Desktop\實地審核\right.mp4',fourcc, 30.0, (1920,1080))

total_frame= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_num = 0 # 3915: 16:53:26.42    第一張:16.15.59
#frame_num = 1517 # 3915: 16:53:26.42    第一張:16.15.59

k=0
cv2.namedWindow('frame_left')
cv2.createTrackbar('frame no left.','frame_left',0,total_frame-1,set_frame_number)
cv2.setTrackbarPos('frame no left.','frame_left',frame_num)  
cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)

"""
right_frame_num = 0
right_total_frame= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
cv2.namedWindow('frame_right')
cv2.createTrackbar('frame no right.','frame_right',0,right_total_frame-1,set_frame_number)
cv2.setTrackbarPos('frame no right.','frame_right',right_frame_num)  
cap2.set(cv2.CAP_PROP_POS_FRAMES,right_frame_num)
end_flag = 0
"""

while(True):    
    key = cv2.waitKey(500)
    if key &0xFF == 32:
        cv2.waitKey()
    if key &0xFF == ord('q'):
        cv2.destroyAllWindows()
        break    

    cv2.setTrackbarPos('frame no left.','frame_left',frame_num)  
    cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)

            
    #"""
    #"""
    if frame_num==total_frame:
        #total_frame= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
        #frame_num = 0
        #cap = cap2
        #if end_flag==1:
            cv2.destroyAllWindows()
            break
        #end_flag = 1
    #"""
    try:
        ret,frame = cap.read()
        
        frame2 = frame[:1080,:]       
        frame3 = cv2.resize(frame2,(960,540))
        
        #image=np.hstack((frame3,cap2_frame3))
        #cv2.setTrackbarPos('frame no.','frame',frame_num)  
        #cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        #cv2.imshow('frame_left',image)
        cv2.imshow('frame_left',frame3)

    except:
        print(k)
        k+=1
        pass
    #"""
    if(k%1==0):
        try:
            pass
#            cv2.imwrite(r"/home/cheng/dir_for_label_data/clearer_image/left_cut_pic/%s.png"%k, frame2)
        except:
            pass
    #"""
    frame_num+=1
    k+=1


# # 右影像

# In[7]:


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
frame_num = 0 # 3915: 16:53:26.42    第一張:16.15.59
k=0
cv2.namedWindow('frame')
cv2.createTrackbar('frame no.','frame',0,total_frame-1,set_frame_number)
cv2.setTrackbarPos('frame no.','frame',frame_num)  
cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)


while(True):
    if k>=21209:
            cv2.destroyAllWindows()
            break
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
    """
    if(k%1==0):
        try:
            cv2.imwrite(r"/home/cheng/dir_for_label_data/left_cut_pic/%s.png"%k, frame2)
        except:
            pass
    """
    frame_num+=1
    k+=1


# # 聲納

# In[2]:


#sonar 
#15:45:15.65
import cv2
import numpy as np
def set_frame_number(x):
    global frame_num
    frame_num = x
    return

date = 20220217

cap2 = cv2.VideoCapture(r"Y:\video\%d\20220217_15hr36m35s384886ms.mp4"%date)
total_frame= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_num = 1 #66:換到16:10
k=0
cv2.namedWindow('frame2')
cv2.createTrackbar('frame no.','frame2',0,total_frame-1,set_frame_number)

while(True):
    try:
        key = cv2.waitKey(20) & 0xFF
        ret,frame = cap2.read()
        frame2 = cv2.resize(frame,(width//2,height//2))
        cv2.setTrackbarPos('frame no.','frame2',frame_num)  
        cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        cv2.imshow('frame2',frame2)
        if key ==ord('q'):
            cv2.destroyAllWindows()
            break      
    except:
        pass
    if(k%10==0):
        try:
            cv2.imwrite(r"C:\Users\cheng\Desktop\water\{a}\sonar\{b}.png".format(a=date,b=k), frame)
        except:
            pass
    k+=1 
    frame_num+=1


# In[ ]:


import requests

# 使用 GET 方式下載普通網頁
r = requests.get('http://111.121.102.191:8081')
print(r.status_code)
#


# In[ ]:


#GAN圖片處理


# In[ ]:


#sonar
import cv2
cap2 = cv2.VideoCapture(r"Y:\video\20211027\20211027_09hr14m07s582811ms.mp4")
def set_frame_number(x):
    global frame_num
    frame_num = x
    return
total_frame= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
width = 256
height = 512
cv2.namedWindow('frame2')
frame_num = 1500
cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
cv2.createTrackbar('frame no.','frame2',0,total_frame-1,set_frame_number)
k=0
while(True):
    try:
        key = cv2.waitKey(20) & 0xFF
        ret,frame = cap2.read()
        #cv2.setTrackbarPos('frame no.','frame2',frame_num)  
        #cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        frame = frame[100:350,200:430,:]
        print(frame.shape)
        frame = cv2.resize(frame,(256,512), interpolation=cv2.INTER_AREA)
        cv2.imshow('frame2',frame)
        if key ==ord('q'):
            cv2.destroyAllWindows()
            break
    except:
        continue
    if(k%5==0):
        cv2.imwrite(r"C:\nightvision\20211107\sonar\%s.png"%k, frame)
    frame_num+=1
    k+=1


# In[ ]:


import cv2
import numpy as np
from PIL import Image
cap2 = cv2.VideoCapture(r"Y:\video\20211027\左\GH041719.MP4")
def set_frame_number(x):
    global frame_num
    frame_num = x
    return
total_frame= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
width = 1920
height = 1080
cv2.namedWindow('frame2')
frame_num=800 #8277: 9:02:49
cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
cv2.createTrackbar('frame no.','frame2',0,total_frame-1,set_frame_number)
k=0
while(True):
    try:
        key = cv2.waitKey(20) & 0xFF
        ret,frame = cap2.read()
        frame = np.rot90(frame, 2)
        #cv2.setTrackbarPos('frame no.','frame2',frame_num)  
        #cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        #frame = frame[0:960,300:1700,:]
        frame = cv2.resize(frame, (256, 512), interpolation=cv2.INTER_AREA)
        cv2.imshow('frame2',frame)
        if key ==ord('q'):
            cv2.destroyAllWindows()
            break
    except:
        continue
    if(k%5==0):
        cv2.imwrite(r"C:\nightvision\20211107\gt\%s.png"%k, frame)
    if(k==8999):
        cv2.destroyAllWindows()
        break
    frame_num+=1
    k+=1


# In[ ]:


#sonar
import cv2
import datetime
cap2 = cv2.VideoCapture(r"Y:\video\20211027\20211027_09hr14m07s582811ms.mp4")
def set_frame_number(x):
    global frame_num
    frame_num = x
    return
total_frame= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
width = 1920
height = 1080
cv2.namedWindow('frame2')
frame_num = 35792
cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
cv2.createTrackbar('frame no.','frame2',0,total_frame-1,set_frame_number)
k=0
while(True):
    try:
        key = cv2.waitKey(20) & 0xFF
        ret,frame = cap2.read()
        frame = frame[300:860,110:1700,:]
        #cv2.setTrackbarPos('frame no.','frame2',frame_num)  
        #cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
        frame = cv2.resize(frame,(256,512), interpolation=cv2.INTER_AREA)
        cv2.imshow('frame2',frame)
        if key ==ord('q'):
            cv2.destroyAllWindows()
            break
    except:
        continue
    if(k%5==0):
        cv2.imwrite(r"C:\nightvision\20211107\sonar\%s.png"%k, frame)
    if(k==8999):
        cv2.destroyAllWindows()
        break
    frame_num+=1
    k+=1


# In[ ]:


import cv2
import time
cap = cv2.VideoCapture(r'C:\Users\cheng\Desktop\實地審核\澎湖影像\0810\prophase\prophase_output_trans.mp4')

while(True):
    ret, frame = cap.read()
    cv2.imshow('1',frame)
    time.sleep(5)
    key = cv2.waitKey(20)
    if key == ord('q'):
        cv2.destroyAllWindows()
                    


# In[ ]:





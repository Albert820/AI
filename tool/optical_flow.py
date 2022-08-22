import cv2
import numpy as np
import os
import re

if not os.path.exists("optical_flow_A13"):
    os.makedirs("optical_flow_A13")

dst_dir = "./optical_flow_A13/"

def set_frame_number(x):
    global frame_num
    frame_num = x
    return

#cap = cv2.VideoCapture("/home/cheng/dir_for_label_data/gopro/clearer_image/n.mp4")
cap = cv2.VideoCapture("/home/cheng/Masr_rcnn revise/test/L_cut.avi")
cap2 = cv2.VideoCapture("/home/cheng/Masr_rcnn revise/test/R_cut.avi")

total_frame= int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
total_frame_right= int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

frame_num = 0
frame_num_right = 0

cv2.namedWindow('frame_left')
cv2.createTrackbar('frame no left.','frame_left',0,total_frame-1,set_frame_number)
cv2.setTrackbarPos('frame no left.','frame_left',frame_num)
cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num_right)


ret, frame1 = cap.read()
prvs_frame = frame1
prvs = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
hsv = np.zeros_like(frame1)
hsv[...,1] = 255

ret, frame1_right = cap2.read()
prvs_frame_right = frame1_right
prvs_right = cv2.cvtColor(frame1_right,cv2.COLOR_BGR2GRAY)
hsv_right = np.zeros_like(frame1_right)
hsv_right[...,1] = 255


_image = "NULL"
images = list()


for img in os.listdir(dst_dir):
      if img.endswith(".png"):
          filename = re.findall(".*[^\.png]", img)
#          print(filename[0])
          images.append(filename[0])
          if _image == "NULL":
              _image = img
images.sort(key=int)
#print(images[-1])

if len(images) != 0:
    save_index =  int(images[-1]) + 1
else:
    save_index = 1

_save_next_flag = 0
print(save_index)
while(1):
    cv2.setTrackbarPos('frame no left.','frame_left',frame_num)
    cap.set(cv2.CAP_PROP_POS_FRAMES,frame_num)
#    cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num_right)
    cap2.set(cv2.CAP_PROP_POS_FRAMES,frame_num)


    ret, frame2 = cap.read()
    next = cv2.cvtColor(frame2,cv2.COLOR_BGR2GRAY)

    ret, frame2_right = cap2.read()
    next_right = cv2.cvtColor(frame2_right,cv2.COLOR_BGR2GRAY)

    if _save_next_flag == 1:
        cv2.imwrite(dst_dir+str(save_index+2)+'.png',frame2)
        cv2.imwrite(dst_dir+str(save_index+5)+'.png',frame2_right)
#        cv2.imwrite('./optical_flow_test/'+str(save_index+2)+'.png',frame2)
#        cv2.imwrite('./optical_flow_test_2/'+str(save_index+2)+'.png',frame2)
        save_index += 6
        _save_next_flag = 0


    flow = cv2.calcOpticalFlowFarneback(prvs,next, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag, ang = cv2.cartToPolar(flow[...,0], flow[...,1])
    hsv[...,0] = ang*180/np.pi/2
    hsv[...,2] = cv2.normalize(mag,None,0,255,cv2.NORM_MINMAX)
    rgb = cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)

    flow_right = cv2.calcOpticalFlowFarneback(prvs_right,next_right, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    mag_right, ang_right = cv2.cartToPolar(flow_right[...,0], flow_right[...,1])
    hsv_right[...,0] = ang_right*180/np.pi/2
    hsv_right[...,2] = cv2.normalize(mag_right,None,0,255,cv2.NORM_MINMAX)
    rgb_right = cv2.cvtColor(hsv_right,cv2.COLOR_HSV2BGR)


    rgb_display = cv2.resize(rgb,(960,540))
    rgb_right_display = cv2.resize(rgb_right,(960,540))
 
    rgb_image=np.hstack((rgb_display,rgb_right_display))

#    rgb_display = cv2.resize(frame2,(960,540))
#    rgb_right_display = cv2.resize(frame2_right,(960,540))
 
#    rgb_image=np.hstack((rgb_display,rgb_right_display))


    cv2.imshow('frame_left',rgb_image)
    k = cv2.waitKey(30) & 0xff

    if k &0xFF == 32:
       cv2.waitKey()
    elif k == ord('q'):
        break
    elif k == ord('s'):
        if frame_num != total_frame:
            cv2.imwrite(dst_dir+str(save_index)+'.png',prvs_frame)
            cv2.imwrite(dst_dir+str(save_index+1)+'.png',frame2)

            cv2.imwrite(dst_dir+str(save_index+3)+'.png',prvs_frame_right)
            cv2.imwrite(dst_dir+str(save_index+4)+'.png',frame2_right)

#            cv2.imwrite('./optical_flow_test_2/'+str(save_index)+'.png',prvs_frame)
#            cv2.imwrite('./optical_flow_test/'+str(save_index)+'.png',prvs_frame)
#            cv2.imwrite('./optical_flow_test/'+str(save_index+1)+'.png',frame2)
#            cv2.imwrite('./optical_flow_test_2/'+str(save_index+1)+'.png',frame2)
            _save_next_flag = 1
#        cv2.imwrite('./optical_flow_test/opticalfb.png',frame2)
#        cv2.imwrite('./optical_flow_test2/opticalhsv.png',rgb)
    prvs_frame = frame2
    prvs = next

    if frame_num == total_frame:
        break

    frame_num += 1
    frame_num_right += 1

cap.release()
cv2.destroyAllWindows()

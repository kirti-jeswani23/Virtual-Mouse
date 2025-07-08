import time
import cv2
import mediapipe as mp
import numpy as np
import tracking_module as tm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


width,height = 640,480
cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

prev_time = 0

obj = tm.HandTracking()


devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

range = volume.GetVolumeRange()
min_vol = range[0]
max_vol = range[1]

sys_volume = 0
bar_volume = 400
per = 0

while True:
    test, img = cap.read()

    img = obj.hand_tracker(img)
    pos_list  = obj.finger_tracker_vc(img,show=False)

    if len(pos_list) !=0:
        x1 , y1 = pos_list[4][1] , pos_list[4][2]
        x2 , y2 = pos_list[8][1] , pos_list[8][2]
        cx , cy = (x1+x2)//2 , (y1+y2)//2

        cv2.circle(img, (x1,y1), 10, (0,0,255), cv2.FILLED)
        cv2.circle(img, (x2,y2), 10, (0,0,255), cv2.FILLED)
        cv2.line(img, (x1,y1), (x2,y2), (0,0,255), 3)
        cv2.circle(img, (cx,cy), 10, (0,0,255), cv2.FILLED)

        length = math.hypot(x2-x1,y2-y1)
        # print(length)
        # 180-10, -65-0
        sys_volume = np.interp(length,[10,180],[min_vol,max_vol])
        bar_volume = np.interp(length,[10,180],[400,150])
        per = np.interp(length,[10,180],[0,100])
        # print(volume)
        volume.SetMasterVolumeLevel(sys_volume, None)

        if length<50:
            cv2.circle(img, (cx,cy), 10, (0,255,0), cv2.FILLED)

    cv2.rectangle(img, (50,150), (100,400), (0,255,0), 3)
    cv2.rectangle(img, (50,int(bar_volume)), (100,400), (0,255,0), cv2.FILLED)
    cv2.putText(img,f"{int(per)} %",(70,460),cv2.FONT_HERSHEY_PLAIN,3,(0,255,0),3)

    curr_time = time.time()
    fps = 1/(curr_time-prev_time)
    prev_time = curr_time

    cv2.putText(img,str(int(fps)),(10,60),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)

    cv2.imshow("Volume Control",img)
    cv2.waitKey(1)

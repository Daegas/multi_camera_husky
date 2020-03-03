#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Listener from husky's camera.

import sys
import rospy
from sensor_msgs.msg import  CameraInfo, Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
from matplotlib import pyplot as plt

# Instantiate CvBridge
bridge = CvBridge()
#Variables
NHus=int(sys.argv[1]) if len(sys.argv) > 1 else 1
cams_rgb=[]
cams_info=[]
for i in range(NHus):
    cams_rgb.append([])
    cams_info.append([])


def callback(msg, n):
    try:
        #Convert to openCV2
        cv2_img=bridge.imgmsg_to_cv2(msg,"bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        cams_rgb[n]=cv2_img 
        #AnalizeImages()        

def AnalizeImages():
    for n in range(len(cams_rgb)):
        plt.imshow(cams_rgb[n])



def main():
    rospy.init_node('camera_listener', anonymous=True)

    for n in range(NHus):
        image_topic = "/husky" + str(n) + "/camera/rgb/"
        sub_cam_info = rospy.Subscriber(image_topic +"image_raw", Image, callback,n)
        
        #TODO:Implement camera_info
        #sub_rgb=rospy.Subscriber(image_topic + "camera_info", CameraInfo)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()

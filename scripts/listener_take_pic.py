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
Hn=1 #Husky Number to use


def callback(msg):
    try:
        #Convert to openCV2
        cv2_img=bridge.imgmsg_to_cv2(msg,"bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        cv2.imshow('image',cv2_img)
        k=cv2.waitKey(0)
        #if spacebar pressed
        if k == 32:
            #Save images
            i=input()
            path='../husky_images/husky' + str(Hn) + '_' + str(i) + '.jpg' 
            cv2.imwrite(path,cv2_img) 


def main(): 
    rospy.init_node('camera_listener', anonymous=True)
    image_topic = "/husky" + str(Hn) + "/camera/rgb/"
    sub_cam_info = rospy.Subscriber(image_topic +"image_raw", Image, callback)

    rospy.spin()

if __name__ == '__main__':
    main()

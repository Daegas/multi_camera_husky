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
#Camera= 0, no camera
camera=1
#Husky to subscribe to 
Hn=0 


def callback(msg):
    try:
        #Convert to openCV2
        cv2_img=bridge.imgmsg_to_cv2(msg,"bgr8")
    except CvBridgeError as e:
        print(e)
    else:
        cv2.imshow('iamge',cv2_img)
        


def main(): 
    rospy.init_node('camera_listener', anonymous=True)
    image_topic = "/husky" + str(Hn) + "/camera/rgb/"
    sub_cam_info = rospy.Subscriber(image_topic +"image_raw", Image, callback)

    rospy.spin()

if __name__ == '__main__':
    main()

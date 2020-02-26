#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Listener from husky's camera.

import rospy
from std_msgs.msg import  CameraInfo Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

# Instantiate CvBridge
bridge = CvBridge()

def callback(msg):
    print('Received an image!')
    try:
        #Convert to openCV2
        cv2_img=bridge.imgmsg_to_cv2(msg,"bgr8")
    except CvBridgeError, e:
        print(e)
    else:
        #Save image as a jpeg
        print('Wunderwall!')
def main():
    rospy.init_node('camera_listener', anonymous=True)
    image_topic = "/husky/camera1/image_raw"
    sub_cam_info = rospy.Subscriber(image_topic, CameraInfo)
    sub_rgb=rospy.Subscriber(image_topic,Image)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    main()

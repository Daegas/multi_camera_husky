#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Converting ROS images and saving image
#https://wiki.ros.org/cv_bridge/Tutorials/ConvertingBetweenROSImagesAndOpenCVImagesPython
#Command
#rosrun multi_camera_husky listener_take_pic.py <Husky to subscribe> <camera true/false> <train true/false>
#rosrun multi_camera_husky listener_take_pic.py 0 true true


from __future__ import print_function

import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


####-------Variables
#Variable i... modify to the one is next


#Husky Number to subscribe
Hn=int(sys.argv[1])
text='\n\nConfiguration: \n \tHusky' + str(Hn)

#Camera
if sys.argv[2]== 'true' or sys.argv[2]=='True':
    cam= 1    
    text+='\n \tCamera ADDED'
elif sys.argv[2]== 'False' or sys.argv[2]=='false':
    cam= 0 
    text+='\n \tCamera OFF'
         

#Train/test
if sys.argv[3]== 'True' or sys.argv[3]=='true': 
    train= True    
    text+='\n \tfor TRAINING'
elif sys.argv[3]== 'False' or sys.argv[3]=='false':
    train= False
    text+='\n \tfor TESTING'

print(text)




# Instantiate CvBridge
bridge = CvBridge()

    

class image_converter:

  def __init__(self,Hn):
    self.i=21
    image_topic = "/husky" + str(Hn) + "/camera/rgb/"
    self.bridge = CvBridge()
    self.image_sub = rospy.Subscriber(image_topic +"image_raw",Image,self.callback)

  def callback(self,data):
    try:
      cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
    except CvBridgeError as e:
      print(e)

    (rows,cols,channels) = cv_image.shape
    if cols > 60 and rows > 60 :
      cv2.circle(cv_image, (50,50), 10, 255)

    cv2.imshow("Image window", cv_image)
    k=cv2.waitKey(3)
    if k== 32:
        if train == True:
            path='../husky_images/train/' + str(cam) + '_' + str(self.i) + '.jpg'
        else:
            path='../husky_images/test/' + str(cam) + '_' + str(self.i) + '.jpg' 
        cv2.imwrite(path,cv_image)
        self.i+=1
	print('Saved image:', path)

def main(args):
  ic = image_converter(Hn)
  rospy.init_node('image_converter', anonymous=True)
  try:
    rospy.spin()
  except KeyboardInterrupt:
    print("Shutting down")
  cv2.destroyAllWindows()

if __name__ == '__main__':
    main(sys.argv)

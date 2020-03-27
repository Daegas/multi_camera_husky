#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Robot Detection 
# Author: Dara Gama <de.gamasandoval@ugto.mx>
# University of Guanajuato

# Train script for detecting a Clearpath Robot Husky by another Husky Robot 

import cv2

#Variables
images=[]
train=True
stop=27


#####
if train== True:
    path= '../husky_images/train/'
else:
    path='../husky_images/test/' 



for i in range(2):
    for j in range(1,stop):
        print('Read image', i ,'_', j)
        path += str(i) + '_' + str(j) + '.jpg'
        img=cv2.imread(path)
        images.append(img)

print(len(images))
    

#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:     Vrushali Dhoe
#
# Created:     13/02/2024
# Copyright:   (c) Nilesh 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import cv2                           #import opencv
video_cap = cv2.VideoCapture(0)     #video captuer
while True :                          #camera disable after presing any key
    ret , video_data = video_cap.read()       #read images
    cv2.imshow("video_live",video_data)
    if cv2.waitKey(10) == ord("a"):
        break                                 #shwoing frem
    video_cap.release()


    #.........................................................................
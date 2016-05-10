import cv2
import os, sys, inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sourcedir = parentdir+'/src'
sys.path.insert(0,parentdir)
sys.path.insert(0,sourcedir)
import config_inicialstates as config
import classParkingPlace as cPP
import Occupancy_functions as occ
import numpy as np
import d5_2 as track
import classCam2 as cam2
import classCam3 as cam3
import classCam4 as cam4
import classCam5 as cam5
import socket
import initParkingPlaces as init

def computeframe(cam, frame, name):
    print ("Starting " + name)
    cam.checkState(frame)
    centres=cam.track_centers(frame)
#SOCKETS CENTRES!!!!!!!!
    if centres:
        longitud= len(centres)
        longi=longitud.to_bytes(1, byteorder='big')
        s_centres.send(longi)
        while centres:
            a= centres.pop()
            data=a[0]
            data_send=data.to_bytes(2, byteorder='big')
            #print(data)
            s_centres.send(data_send)
            data=a[1]
            data_send=data.to_bytes(2, byteorder='big')
            s_centres.send(data_send)
	    #print(data_send)

#socket cam



#init all sockets
host= '46.101.132.172'
port= 3337
port_places= 3339
backlog=5
size= 1024
s_centres = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_centres.connect((host,port))
s_places = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_places.connect((host,port_places))



cap1=cv2.VideoCapture('../src/samples/Videos/test.mp4')
cap2=cv2.VideoCapture('../src/samples/Videos/test.mp4')
cap3=cv2.VideoCapture('../src/samples/Videos/test.mp4')
cap4=cv2.VideoCapture('../src/samples/Videos/test.mp4')

rval, frame1 = cap1.read()
rval, frame2 = cap2.read()
rval, frame3 = cap3.read()
rval, frame4 = cap4.read()
parkingsDown_Cam2, parkingUp_Cam2, masks_Cam2, parkingsDown_Cam3, parkingUp_Cam3, masks_Cam3, parkingsDown_Cam4, parkingUp_Cam4, masks_Cam4, parkingsDown_Cam5, parkingUp_Cam5, masks_Cam5 = init.defineParkingPlaces(frame1, frame2, frame3, frame4, config)
cam2 = cam2.Cam2(masks_Cam2, parkingsDown_Cam2, parkingUp_Cam2)
cam3 = cam3.Cam3(masks_Cam3, parkingsDown_Cam3, parkingUp_Cam3)
cam4 = cam4.Cam4(masks_Cam4, parkingsDown_Cam4, parkingUp_Cam4)
cam5 = cam5.Cam5(masks_Cam5, parkingsDown_Cam5, parkingUp_Cam5)
while rval:
	computeframe(cam2, frame1, "Cam-2")
	computeframe(cam3, frame2, "Cam-3")
	computeframe(cam4, frame3, "Cam-4")
	computeframe(cam5, frame4, "Cam-5")
	cv2.imwrite('framej.jpg',frame1)

cap1.release()
cap2.release()
cap3.release()
cap4.release()

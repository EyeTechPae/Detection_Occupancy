import cv2
import classParkingPlace as cPP
import Occupancy_functions as occ
import numpy as np
import time

t=time.time()
cap=cv2.VideoCapture('cotxeVerd.mp4')
cont=0
rval, frame = cap.read()

parking= cPP.ParkingPlace('placa9.jpg', 9, 20)
parking.setMask(frame)
parking.setMaskState()
rval, frame = cap.read()
while rval:
	if cont%30 is 0:
		parking.checkOccupancy(frame)
	cont=cont+1
	cv2.imwrite('Video.jpg',frame)
	rval, frame = cap.read()
	if cont%1800 is 0:
		parking.setMask(frame)
		parking.setMaskState()

tend=time.time()-t
print("Total time elapsesd: "+str(tend))
cap.release()


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
import classCam2 as cam
import socket

cap=cv2.VideoCapture('test.mp4')
rval, frame = cap.read()
print(config.parking1)
print(rval)
parking1 = cPP.ParkingPlace('placa1.jpg', 1, 65, config.parking1)
parking1.setMask(frame)
parking2 = cPP.ParkingPlace('placa2.jpg', 2, 65, config.parking2)
parking2.setMask(frame)
parking3 = cPP.ParkingPlace('placa3.jpg', 3, 65, config.parking3)
parking3.setMask(frame)
parking4 = cPP.ParkingPlace('placa4.jpg', 4, 65, config.parking4)
parking4.setMask(frame)
parking5 = cPP.ParkingPlace('placa5.jpg', 5, 30, config.parking5)
parking5.setMask(frame)
parking6 = cPP.ParkingPlace('placa6.jpg', 6, 25, config.parking6)
parking6.setMask(frame)
parking7 = cPP.ParkingPlace('placa7.jpg', 7, 20, config.parking7)
parking7.setMask(frame)
parking8 = cPP.ParkingPlace('placa8.jpg', 8, 20,config.parking8)
parking8.setMask(frame)
parking9 = cPP.ParkingPlace('placa9.jpg', 9, 20,config.parking9)
parking9.setMask(frame)

parkingsDown = [parking1, parking2, parking3, parking4, parking5]
parkingUp = [parking6, parking7, parking8, parking9]  
masks = ['maskin.jpg', 'maskout.jpg', 'maskdown.jpg', 'maskup.jpg', 'mask_d5_2.jpg']
#masks = []
#masks.append(cv2.imread(mask[i], 0))
cam = cam.Cam2(masks, parkingsDown, parkingUp)
#frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
skip=1
prev_inMotion = False
prev_up = False
prev_down = False
timer_references=0
timer_up=0
timer_down=0
host= '192.168.43.116'
port= 3335
backlog=5
size= 1024

while rval:
#actualitzar occupació parkUp i parkDown quan hi ha hagut moviment transició de moviment a no moviment i amb una frequencia maxima d'un cop per minut

#actualitzem les imatges de referencia pel matcher cada cop que detectem moviment a la zoneIn i amb una frequencia maxima d'un cop per minut

			
	cam.checkState(frame)
	
	#print(centres)




	#print(centres)
#cam.checkCamState(frame) 
	rval, frame = cap.read()

	cv2.imwrite('framej.jpg',frame)
	#frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
cap.release()





















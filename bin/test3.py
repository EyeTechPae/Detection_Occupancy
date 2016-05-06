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
from multiprocessing import Process, Lock

def computeframe(l, cam, frame, name):
    l.acquire()
    print ("Starting " + name)
    cam.checkState(frame)
    l.release()


cap1=cv2.VideoCapture('../src/samples/Videos/test.mp4')
cap2=cv2.VideoCapture('../src/samples/Videos/test.mp4')
cap3=cv2.VideoCapture('../src/samples/Videos/test.mp4')
cap4=cv2.VideoCapture('../src/samples/Videos/test.mp4')

rval, frame1 = cap1.read()
rval, frame2 = cap2.read()
rval, frame3 = cap3.read()
rval, frame4 = cap4.read()
frame = frame1

parkingsDown, parkingUp, masks = init.defineParkingPlaces(frame, config)

cam2 = cam2.Cam2(masks, parkingsDown, parkingUp)
cam3 = cam3.Cam3(masks, parkingsDown, parkingUp)
cam4 = cam4.Cam4(masks, parkingsDown, parkingUp)
cam5 = cam5.Cam5(masks, parkingsDown, parkingUp)

lock = Lock()


while rval:
#actualitzar occupació parkUp i parkDown quan hi ha hagut moviment transició de moviment a no moviment i amb una frequencia maxima d'un cop per minut

#actualitzem les imatges de referencia pel matcher cada cop que detectem moviment a la zoneIn i amb una frequencia maxima d'un cop per minut
	p = []
	p.append(Process(target=computeframe, args=(lock,cam2, frame1, "Cam-2")))
	p.append(Process(target=computeframe, args=(lock,cam3, frame2, "Cam-3")))
	#p.append(Process(target=computeframe, args=(lock,cam4, frame3, "Cam-4")))
	#p.append(Process(target=computeframe, args=(lock,cam5, frame4, "Cam-5")))
	for proc in p:
		proc.start()
	for proc in p:
		proc.join()

	print ("Exiting Main Thread")
	rval, frame1 = cap1.read()
	rval, frame2 = cap2.read()
	rval, frame3 = cap3.read()
	rval, frame4 = cap4.read()
	frame = frame1
	cv2.imwrite('framej.jpg',frame1)

cap1.release()
cap2.release()
cap3.release()
cap4.release()

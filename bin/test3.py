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
import threading
import initParkingPlaces as init

class myThread (threading.Thread):
    def __init__(self, name, cam, frame):
        threading.Thread.__init__(self)
        self.name = name
        self.cam = cam
        self.frame = frame
    def run(self):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        self.cam.checkState(self.frame)
        # Free lock to release next thread
        threadLock.release()




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


threadLock = threading.Lock()
threads = []

while rval:
#actualitzar occupació parkUp i parkDown quan hi ha hagut moviment transició de moviment a no moviment i amb una frequencia maxima d'un cop per minut

#actualitzem les imatges de referencia pel matcher cada cop que detectem moviment a la zoneIn i amb una frequencia maxima d'un cop per minut

			
	# Create new threads
	thread1 = myThread("Cam-2", cam2, frame1)
	thread2 = myThread("Cam-3", cam3, frame2)
	thread3 = myThread("Cam-4", cam4, frame3)
	thread4 = myThread("Cam-5", cam5, frame4)

	# Start new Threads
	thread1.start()
	thread2.start()
	thread3.start()
	thread4.start()

	# Add threads to thread list
	threads.append(thread1)
	threads.append(thread2)
	threads.append(thread3)
	threads.append(thread4)

	# Wait for all threads to complete
	for t in threads:
    		t.join()

	print ("Exiting Main Thread")
 
	rval, frame1 = cap1.read()
	rval, frame2 = cap2.read()
	rval, frame3 = cap3.read()
	rval, frame4 = cap4.read()

	cv2.imwrite('framej.jpg',frame1)
	threadLock = threading.Lock()
	threads = []

cap1.release()
cap2.release()
cap3.release()
cap4.release()

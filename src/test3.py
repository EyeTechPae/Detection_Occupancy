import cv2
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
import myThread

cap=cv2.VideoCapture('test.mp4')
rval, frame = cap.read()

#Parking places defined in a config file.....!!!!! DIFERENCIAR PLAÇES DE DALT I PLAÇES D'ABAIX!!!!!!!!!!!!!!!!

#parkingsDown = [parking1, parking2, parking3, parking4, parking5]
#parkingUp = [parking6, parking7, parking8, parking9]  
#masks = ['maskin.jpg', 'maskout.jpg', 'maskdown.jpg', 'maskup.jpg', 'mask_d5_2.jpg']

#s'HAN D'INICIALITZAR COM CAL!!!!
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
	thread1 = myThread("Cam-2", cam2)
	thread2 = myThread("Cam-3", cam3)
	thread3 = myThread("Cam-4", cam4)
	thread4 = myThread("Cam-5", cam5)

	# Start new Threads
	thread1.run(frame)
	thread2.run(frame)
	thread3.run(frame)
	thread4.run(frame)

	# Add threads to thread list
	threads.append(thread1)
	threads.append(thread2)
	threads.append(thread3)
	threads.append(thread4)

	# Wait for all threads to complete
	for t in threads:
    		t.join()
	print ("Exiting Main Thread")
 
	rval, frame = cap.read()

	cv2.imwrite('framej.jpg',frame)
	
	threadLock = threading.Lock()
	threads = []
cap.release()





















import cv2
import classParkingPlace as cPP
import Occupancy_functions as occ
import numpy as np
import d5_2 as track
import classCam2 as cam


cap=cv2.VideoCapture('samples/Videos/test.mp4')
rval, frame = cap.read()

parking1 = cPP.ParkingPlace('samples/Occupancy/placa1.jpg', 1, 65, False)
parking1.setMask(frame)
parking2 = cPP.ParkingPlace('samples/Occupancy/placa2.jpg', 2, 65, True)
parking2.setMask(frame)
parking3 = cPP.ParkingPlace('samples/Occupancy/placa3.jpg', 3, 65, True)
parking3.setMask(frame)
parking4 = cPP.ParkingPlace('samples/Occupancy/placa4.jpg', 4, 65, False)
parking4.setMask(frame)
parking5 = cPP.ParkingPlace('samples/Occupancy/placa5.jpg', 5, 30, False)
parking5.setMask(frame)
parking6 = cPP.ParkingPlace('samples/Occupancy/placa6.jpg', 6, 25, True)
parking6.setMask(frame)
parking7 = cPP.ParkingPlace('samples/Occupancy/placa7.jpg', 7, 20, False)
parking7.setMask(frame)
parking8 = cPP.ParkingPlace('samples/Occupancy/placa8.jpg', 8, 20,False)
parking8.setMask(frame)
parking9 = cPP.ParkingPlace('samples/Occupancy/placa9.jpg', 9, 20,False)
parking9.setMask(frame)

parkingsDown = [parking1, parking2, parking3, parking4, parking5]
parkingUp = [parking6, parking7, parking8, parking9]  
masks = ['samples/Tracking/maskin.jpg', 'samples/Tracking/maskout.jpg', 'samples/Tracking/maskdown.jpg', 'samples/Tracking/maskup.jpg', 'samples/Tracking/mask_d5_2.jpg']
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
while rval:
#actualitzar occupació parkUp i parkDown quan hi ha hagut moviment transició de moviment a no moviment i amb una frequencia maxima d'un cop per minut

#actualitzem les imatges de referencia pel matcher cada cop que detectem moviment a la zoneIn i amb una frequencia maxima d'un cop per minut

			
	if prev_up is not cam.isParkingUp(frame):
		if prev_up==True:				
			prev_up=False
			if timer_down>600:
				cam.updateOccupancyStatesUp(frame)
				timer_up=0
		else:
			prev_up=True
			#cam.updateOccupancyStatesUp(frame)
						
	if prev_down is not cam.isParkingDown(frame):
		if prev_down==True:				
			prev_down=False
			if timer_down>650:
				cam.updateOccupancyStatesDown(frame)
				timer_down=0
		else:
			prev_down=True	
			#cam.updateOccupancyStatesDown(frame)

	#actualitzar màscares quan entra un cotxe zona IN i no hi  ha moviment a parkingUp ni parkingDown					
	if prev_inMotion is not cam.isZoneIn(frame):
		if prev_inMotion==True:				
			prev_inMotion=False
		else:
			prev_inMotion=False
				

		if prev_up==False and prev_down==False and timer_references>9000:
			cam.updateRefMasks(frame)
			timer_references=0

	if timer_up%900==0 and prev_up==False:
		cam.updateOccupancyStatesUp(frame)
		
	if timer_down%900==0 and prev_down==False:
		cam.updateOccupancyStatesDown(frame)
		
	centres= cam.track_centers(frame)


	#print(centres)
#cam.checkCamState(frame) 
	rval, frame = cap.read()
	timer_references=timer_references+1
	timer_down=timer_down+1
	timer_up=timer_up+1
	cv2.imwrite('framej.jpg',frame)
	#frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	
cap.release()





















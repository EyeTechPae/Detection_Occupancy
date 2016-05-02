import sys
import d5_2 as camera2
import cv2

class Cam2(object):

	""" Class Cam2 constructor. Masks are array of masks,  parksDown is an array
	    of ParkingPlaces and parksUp other array of parking places, for the bottom zone
	    of the parking and for the top side respectivly."""

	def __init__(self, masky, parksDown, parksUp):
		self.masks = []
		self.parksUp = []
		self.parksDown = []
		for mask in masky:
			self.masks.append(cv2.imread(mask, 0))
		for parkUp in parksUp:
			self.parksUp.append(parkUp)
		for parkDown in parksDown:
			self.parksDown.append(parkDown)
		
		self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
	""" This method defines if there is a car entering in Cam2. It needs the frame
	    and returns true if there is a car entering and false if there is not.    """

	def isZoneIn(self, frame): #override 
		
		frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame_applied= frame*self.masks[0]
		frame_applied = cv2.resize(frame_applied, (360, 240))		
		str_open, str_dila = camera2.get_strelements(15,12)
		fgmask = self.fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		#centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(contours)>0:
			return True
		else:
			return False

	""" This method defines if there is a car going out of Cam2. It needs the frame
	    and returns true if there is a car going out and false if there is not.    """

	def isZoneOut(self, frame):  #override 
		frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame_applied= frame*self.masks[1]
		frame_applied = cv2.resize(frame_applied, (360, 240))		
		str_open, str_dila = camera2.get_strelements(15,12)
		fgmask = self.fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		#centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(contours)>0:
			return True
		else:
			return False

	""" This method defines if there is a car moving in the bottom side of the 
	    battery parking lots. It returns true if there is a movement and false if 
            there is not."""		

	def isParkingDown(self, frame): #override 
		frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame_applied= frame*self.masks[2]		
		frame_applied = cv2.resize(frame_applied, (360, 240))		
		str_open, str_dila = camera2.get_strelements(15,12)
		fgmask = self.fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		#centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(contours)>0:
			return True
		else:
			return False

	""" This method defines if there is a car moving in the top side of the 
	    battery parking lots. It returns true if there is a movement and false if 
            there is not."""

	def isParkingUp(self, frame): #override 
		frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame_applied= frame*self.masks[3]		
		frame_applied = cv2.resize(frame_applied, (360, 240))		
		str_open, str_dila = camera2.get_strelements(15,12)
		fgmask = self.fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)
		#centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		if len(contours)>0:
			return True
		else:
			return False

#actualitzem totes les imatges de referencia

	def updateRefMasks(self, frame):
		for i in range(len(self.parksDown)):
			self.parksDown[i].setMask(frame)
		for j in range(len(self.parksUp)):
			self.parksUp[j].setMask(frame)
#actualitzar parking states de dalt

	def updateOccupancyStatesUp(self, frame):
		for i in range(len(self.parksUp)):
			self.parksUp[i].checkOccupancy(frame)


#actualitzar parking states de baix
	def updateOccupancyStatesDown(self, frame):
		for i in range(len(self.parksDown)):
			self.parksDown[i].checkOccupancy(frame)


	def track_centers(self, frame):

		frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame_applied= frame*self.masks[4]		
		frame_applied = cv2.resize(frame_applied, (360, 240))		
		str_open, str_dila = camera2.get_strelements(15,12)
		fgmask = self.fgbg.apply(frame_applied)
		img = camera2.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera2.get_contours (img)	
		centres, frame_applied = camera2.get_centroids (contours, frame_applied)
		return centres


	"""Method that checks the state of the battery parking lots if there is any
	   movement in the zones of interest."""
	def checkCamState(self, frame): #override

		if self.isParkingDown(frame):
			self.parkDownCounter=0
			if self.parkDownCounter <1 :
				for parkDown in self.parksDown:
					parkDown.checkOccupancy(frame)
				self.parkDownCounter= self.parkDownCounter+1
			else:
				self.parkDownCounter=0
		if self.isParkingUp(frame):
			self.parkUpCounter=0
			if self.parkUpCounter < 4:           
				for parkUp in self.parksUp:
  					parkUp.checkOccupancy(frame)
				self.parkUpCounter = self.parkUpCounter+1
			else:
				self.parkUpCounter=0
	



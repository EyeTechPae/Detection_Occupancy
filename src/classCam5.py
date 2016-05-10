import sys
import d5_2 as camera2
import cv2

class Cam5(object):

	""" Class Cam2 constructor. Masks are array of masks,  parksDown is an array
	    of ParkingPlaces and parksUp other array of parking places, for the bottom zone
	    of the parking and for the top side respectivly."""

	def __init__(self, masky, parksDown, parksUp):
		self.masks = []
		self.parksUp = []
		self.parksDown = []
		self.timer_references=0

		self.timer_up=0
		self.timer_down=0
		self.prev_down = False
		self.prev_up = False
		self.prev_inMotion = False
		self.prev_outMotion = False
		self.centres=[]
		for mask in masky:
			self.masks.append(cv2.imread(mask, 0))
		for parkUp in parksUp:
			self.parksUp.append(parkUp)
		for parkDown in parksDown:
			self.parksDown.append(parkDown)
		
		self.fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
	""" This method defines if there is a car entering in Cam2. It needs the frame
	    and returns true if there is a car entering and false if there is not.    """

	def get_Parking_States(self): #override 
		states_down=[]
		states_up=[]
		num_up=[]
		num_down=[]
		for i in range(len(self.parksDown)):
			states_down.append(self.parksDown[i].occupied)
			if states_down[i]==True:
				num_down.append(1)
			else:
				num_down.append(0)
		
		for i in range(len(self.parksUp)):
			states_up.append(self.parksUp[i].occupied)
			if states_up[i]==True:
				num_up.append(1)
			else:
				num_up.append(0)
		print(str(states_down))
		print(str(states_up))
		return(num_down, num_up)






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




	"""Advanced state checker with timers and tracking callings."""
	def checkState(self, frame):
		if self.prev_up is not self.isParkingUp(frame):
			if self.prev_up==True:				
				self.prev_up=False
				if self.timer_down>600:
					self.updateOccupancyStatesUp(frame)
					self.timer_up=0
			else:
				self.prev_up=True
				#cam.updateOccupancyStatesUp(frame)
						
		if self.prev_down is not self.isParkingDown(frame):
			if self.prev_down==True:				
				self.prev_down=False
				if self.timer_down>650:
					self.updateOccupancyStatesDown(frame)
					self.timer_down=0
			else:
				self.prev_down=True	
				#cam.updateOccupancyStatesDown(frame)
	#actualitzar màscares quan entra un cotxe zona IN i no hi  ha moviment a parkingUp ni parkingDown					
		if self.prev_inMotion is not self.isZoneIn(frame):
			if self.prev_inMotion==True:				
				self.prev_inMotion=False
			else:
				self.prev_inMotion=False
				

			if self.prev_up==False and self.prev_down==False and self.timer_references>9000:
				self.updateRefMasks(frame)
				self.timer_references=0

		if self.timer_up%900==0 and self.prev_up==False:
			self.updateOccupancyStatesUp(frame)
		
		if self.timer_down%900==0 and self.prev_down==False:
			self.updateOccupancyStatesDown(frame)
		
		self.centres= self.track_centers(frame)
		self.timer_references=self.timer_references+1
		self.timer_down=self.timer_down+1
		self.timer_up=self.timer_up+1
		state_up, state_down = self.get_Parking_States();
		return(state_up, state_down)



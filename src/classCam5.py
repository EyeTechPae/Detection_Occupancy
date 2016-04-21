import cv2
import d5_2 as camera5

class Cam5(object):

	""" Class Cam5 constructor. Masks are array of masks,  parksDown is an array
	    of ParkingPlaces and parksUp other array of parking places, for the bottom zone
	    of the parking and for the top side respectivly."""

	def __init__(self, masks, ID, parksDown, parksUp):
		for mask,index in zip(masks, range(len(masks))):
			self.masks[index]=cv2.imread(mask, 0)
		for parkUp, index in zip(parksUp, range(len(parksUp))):
			self.parksUp[index]=parkUp
		for parkDown, index in zip(parksDown, range(len(parksUp))):
			self.parksDown[index]=parkDown
		self.ID=ID

	""" This method defines if there is a car entering in Cam2. It needs the frame
	    and returns true if there is a car entering and false if there is not.    """

	def isZoneIn(self): #override 
		frame_applied= frame*self.masks[0]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera5.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera5.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera5.get_contours (img)
		centres, frame_applied = camera5.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	""" This method defines if there is a car going out of Cam2. It needs the frame
	    and returns true if there is a car going out and false if there is not.    """


	def isZoneOut(self):  #override 
		frame_applied= frame*self.masks[1]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera5.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera5.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera5.get_contours (img)
		centres, frame_applied = camera5.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	""" This method defines if there is a car moving in the bottom side of the 
	    battery parking lots. It returns true if there is a movement and false if 
            there is not."""

	def isParkingDown(self): #override 
		frame_applied= frame*self.masks[2]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera5.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera5.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera5.get_contours (img)
		centres, frame_applied = camera5.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False


	""" This method defines if there is a car moving in the top side of the 
	    battery parking lots. It returns true if there is a movement and false if 
            there is not."""

	def isParkingUp(self): #override 
		frame_applied= frame*self.masks[3]		
		fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)
		ret = True
		str_open, str_dila = camera5.get_strelements(28,53)
		fgmask = fgbg.apply(frame_applied)
		img = camera5.operacions_morfologiques(fgmask, str_open, str_dila)
		contours = camera5.get_contours (img)
		centres, frame_applied = camera5.get_centroids (contours, frame_applied)
		if len(centres)>0:
			return True
		else:
			return False

	"""Method that checks the state of the battery parking lots if there is any
	   movement in the zones of interest."""

	def checkCamState(self): #override 

		if isParkingDown():
			for parkDown in self.parksDown:
				parkDown.checkOccupancyState()

		if isParkingUp():
			for parkUp in self.parksUp:
				parkUp.checkOccupancyState()


import cv2
import Occupancy_functions as occ
class ParkingPlace(object):

#Mask: path to ParkingPlace mask

    """Constructor of class Parking Place. It needs the parking place mask,
       its ID, its threshold for SURF algorithm, and an optional argument
       "occupied", which can be set if initial occupancy state is occupied."""
    def __init__(self, mask, ID, threshold, occupied=False):
        self.im_mask=cv2.imread(mask, 0)
        self.occupied=occupied
        self.actualMask=None
        self.ID=ID
        self.threshold=threshold
        self.kp=None
        self.des=None

    """Method that sets the Mask with which the input frame will be compared"""

    def setMask(self, frame_path):
        frame=cv2.cvtColor(frame_path,cv2.COLOR_BGR2GRAY)
        self.actualMask= frame*self.im_mask
        self.kp,self.des=occ.computeSurfFeatures(self.actualMask)
        cv2.imwrite('Placa.jpg',self.actualMask)
        self.setMaskState()
       
    """Method that sets the actual state of the parking place. It must be true
       if the parking place is occupied and false if it is not."""

    def setOccupancyState(self, state):
        self.occupied = state
    
    """Method that sets the state of the Mask (whether there is a car in the actual
       mask or there is not)."""

    def setMaskState(self):
        self.maskState=self.occupied

    """ Method that checks occupancy state of the parking place. It changes the
    local attribute "occupied" calling setOccupancyState."""

    def checkOccupancy(self, frame):
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame_masked = frame_gray * self.im_mask
        kp, des= occ.computeSurfFeatures(frame_masked)
        good_matches = occ.computeGoodMatches(frame_masked, self.kp, self.des)
        if not self.maskState:
            if good_matches > self.threshold:
                self.setOccupancyState(False)
            else:
                self.setOccupancyState(True)
            #self.actualMask= frame*self.im_mask
                cv2.imwrite('Placa.jpg',frame_masked)
          #  self.setMask(frame)
            print("Placa "+ str(self.ID) + " ocupada?" + str(self.occupied)+ " " + str(good_matches))
        if self.maskState:
            if good_matches > self.threshold:
                self.setOccupancyState(True)
            else:
                self.setOccupancyState(False)
            #self.actualMask= frame*self.im_mask
                cv2.imwrite('Placa.jpg',frame_masked)
          #  self.setMask(frame)
            print("Placa "+ str(self.ID) + " ocupada?" + str(self.occupied)+ " " + str(good_matches))


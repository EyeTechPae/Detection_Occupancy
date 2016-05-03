import cv2
import classParkingPlace as cPP



def defineParkingPlaces(frame, config):
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
    return parkingsDown, parkingUp, masks

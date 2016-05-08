import cv2
import classParkingPlace as cPP
import numpy as np

def defineParkingPlaces(frame1, frame2, frame3, frame4, config):
    parking0 = cPP.ParkingPlace('../src/samples/Occupancy/placa0.jpg', 0, 65, config.parking0)
    parking0.setMask(frame1)
    parking1 = cPP.ParkingPlace('../src/samples/Occupancy/placa1.jpg', 1, 65, config.parking1)
    parking1.setMask(frame1)
    parking2 = cPP.ParkingPlace('../src/samples/Occupancy/placa2.jpg', 2, 65, config.parking2)
    parking2.setMask(frame1)
    parking3 = cPP.ParkingPlace('../src/samples/Occupancy/placa3.jpg', 3, 65, config.parking3)
    parking3.setMask(frame1)
    parking4 = cPP.ParkingPlace('../src/samples/Occupancy/placa4.jpg', 4, 65, config.parking4)
    parking4.setMask(frame1)
    parking5 = cPP.ParkingPlace('../src/samples/Occupancy/placa5.jpg', 5, 30, config.parking5)
    parking5.setMask(frame2)
    parking6 = cPP.ParkingPlace('../src/samples/Occupancy/placa6.jpg', 6, 25, config.parking6)
    parking6.setMask(frame2)
    parking7 = cPP.ParkingPlace('../src/samples/Occupancy/placa7.jpg', 7, 20, config.parking7)
    parking7.setMask(frame2)
    parking8 = cPP.ParkingPlace('../src/samples/Occupancy/placa8.jpg', 8, 20,config.parking8)
    parking8.setMask(frame2)
    parking9 = cPP.ParkingPlace('../src/samples/Occupancy/placa9.jpg', 9, 20,config.parking9)
    parking9.setMask(frame3)
    parking10 = cPP.ParkingPlace('../src/samples/Occupancy/placa10.jpg', 10, 20,config.parking10)
    parking10.setMask(frame3)
    parking11 = cPP.ParkingPlace('../src/samples/Occupancy/placa11.jpg', 11, 20,config.parking11)
    parking11.setMask(frame3)
    parking12 = cPP.ParkingPlace('../src/samples/Occupancy/placa12.jpg', 12, 65, config.parking12)
    parking12.setMask(frame3)
    parking13 = cPP.ParkingPlace('../src/samples/Occupancy/placa13.jpg', 13, 65, config.parking13)
    parking13.setMask(frame3)
    parking14 = cPP.ParkingPlace('../src/samples/Occupancy/placa14.jpg', 14, 65, config.parking14)
    parking14.setMask(frame3)
    parking15 = cPP.ParkingPlace('../src/samples/Occupancy/placa15.jpg', 15, 65, config.parking15)
    parking15.setMask(frame4)
    parking16 = cPP.ParkingPlace('../src/samples/Occupancy/placa16.jpg', 16, 65, config.parking16)
    parking16.setMask(frame4)
    parking17 = cPP.ParkingPlace('../src/samples/Occupancy/placa17.jpg', 17, 65, config.parking17)
    parking17.setMask(frame1)
    parking18 = cPP.ParkingPlace('../src/samples/Occupancy/placa18.jpg', 18, 65, config.parking18)
    parking18.setMask(frame1)
    parking19 = cPP.ParkingPlace('../src/samples/Occupancy/placa19.jpg', 19, 65, config.parking19)
    parking19.setMask(frame1)
    parking20 = cPP.ParkingPlace('../src/samples/Occupancy/placa20.jpg', 20, 65, config.parking20)
    parking20.setMask(frame1)
    parking21 = cPP.ParkingPlace('../src/samples/Occupancy/placa21.jpg', 21, 65, config.parking21)
    parking21.setMask(frame1)
    parking22 = cPP.ParkingPlace('../src/samples/Occupancy/placa22.jpg', 22, 65, config.parking22)
    parking22.setMask(frame1)
    parking23 = cPP.ParkingPlace('../src/samples/Occupancy/placa23.jpg', 23, 65, config.parking23)
    parking23.setMask(frame2)
    parking24 = cPP.ParkingPlace('../src/samples/Occupancy/placa24.jpg', 24, 65, config.parking24)
    parking24.setMask(frame2)
    parking25 = cPP.ParkingPlace('../src/samples/Occupancy/placa25.jpg', 25, 65, config.parking25)
    parking25.setMask(frame2)
    parking26 = cPP.ParkingPlace('../src/samples/Occupancy/placa26.jpg', 26, 65, config.parking26)
    parking26.setMask(frame2)
    parking27 = cPP.ParkingPlace('../src/samples/Occupancy/placa27.jpg', 27, 65, config.parking27)
    parking27.setMask(frame2)
    parking28 = cPP.ParkingPlace('../src/samples/Occupancy/placa28.jpg', 28, 65, config.parking28)
    parking28.setMask(frame2)
    parking29 = cPP.ParkingPlace('../src/samples/Occupancy/placa29.jpg', 29, 65, config.parking29)
    parking29.setMask(frame2)
    parking30 = cPP.ParkingPlace('../src/samples/Occupancy/placa30.jpg', 30, 65, config.parking30)
    parking30.setMask(frame2)
    parking31 = cPP.ParkingPlace('../src/samples/Occupancy/placa31.jpg', 31, 65, config.parking31)
    parking31.setMask(frame3)
    parking32 = cPP.ParkingPlace('../src/samples/Occupancy/placa32.jpg', 32, 65, config.parking32)
    parking32.setMask(frame3)
    parking33 = cPP.ParkingPlace('../src/samples/Occupancy/placa33.jpg', 33, 65, config.parking33)
    parking33.setMask(frame3)
    parking34 = cPP.ParkingPlace('../src/samples/Occupancy/placa34.jpg', 34, 65, config.parking34)
    parking34.setMask(frame3)
    parking35 = cPP.ParkingPlace('../src/samples/Occupancy/placa35.jpg', 35, 65, config.parking35)
    parking35.setMask(frame3)
    parking36 = cPP.ParkingPlace('../src/samples/Occupancy/placa36.jpg', 36, 65, config.parking36)
    parking36.setMask(frame3)
    parking37 = cPP.ParkingPlace('../src/samples/Occupancy/placa37.jpg', 37, 65, config.parking37)
    parking37.setMask(frame3)
    parking38 = cPP.ParkingPlace('../src/samples/Occupancy/placa38.jpg', 38, 65, config.parking38)
    parking38.setMask(frame3)
    parking39 = cPP.ParkingPlace('../src/samples/Occupancy/placa39.jpg', 39, 65, config.parking39)
    parking39.setMask(frame4)
    parking40 = cPP.ParkingPlace('../src/samples/Occupancy/placa40.jpg', 40, 65, config.parking40)
    parking40.setMask(frame4)
    parking41 = cPP.ParkingPlace('../src/samples/Occupancy/placa41.jpg', 41, 65, config.parking41)
    parking41.setMask(frame4)
    parking42 = cPP.ParkingPlace('../src/samples/Occupancy/placa42.jpg', 42, 65, config.parking42)
    parking42.setMask(frame4)


    parkingsDown_Cam2 = [parking17, parking18, parking19, parking20, parking21, parking22]
    parkingUp_Cam2 = [parking0, parking1, parking2, parking3, parking4]
    parkingsDown_Cam3 = [parking23, parking24, parking25, parking26, parking27, parking28, parking29, parking30]
    parkingUp_Cam3 = [parking5, parking6, parking7, parking8]
    parkingsDown_Cam4 = [parking31, parking32, parking33, parking34, parking35, parking36, parking37, parking38]
    parkingUp_Cam4 = [parking9, parking10, parking11, parking12, parkin13, parking14]
    parkingsDown_Cam5 = [parking39, parking40, parking41, parking42]
    parkingUp_Cam5 = [parking15, parking16]  
    masks_Cam2 = ['../src/samples/Tracking/d5_1_in.jpg', '../src/samples/Tracking/d5_1_out.jpg', '../src/samples/Tracking/d5_1_down.jpg', '../src/samples/Tracking/d5_1_up.jpg', '../src/samples/Tracking/d5_1_road.jpg']
    masks_Cam3 = ['../src/samples/Tracking/d5_2_in.jpg', '../src/samples/Tracking/d5_2_out.jpg', '../src/samples/Tracking/d5_2_down.jpg', '../src/samples/Tracking/d5_2_up.jpg', '../src/samples/Tracking/d5_2_road.jpg']
    masks_Cam4 = ['../src/samples/Tracking/d6_1_in.jpg', '../src/samples/Tracking/d6_1_out.jpg', '../src/samples/Tracking/d6_1_down.jpg', '../src/samples/Tracking/d6_1_up.jpg', '../src/samples/Tracking/d6_1_road.jpg']
    masks_Cam5 = ['../src/samples/Tracking/d6_2_in.jpg', '../src/samples/Tracking/d6_2_out.jpg', '../src/samples/Tracking/d6_2_down.jpg', '../src/samples/Tracking/d6_2_up', '../src/samples/Tracking/d6_2_road.jpg']
    return parkingsDown, parkingUp, masks

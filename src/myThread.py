#!/usr/bin/python3

import threading
import time

class myThread (threading.Thread):
    def __init__(self, name, cam):
        threading.Thread.__init__(self)
        self.name = name
	self.cam = cam
    def run(self, frame):
        print ("Starting " + self.name)
        # Get lock to synchronize threads
        threadLock.acquire()
        self.cam.checkState(frame)
        # Free lock to release next thread
        threadLock.release()


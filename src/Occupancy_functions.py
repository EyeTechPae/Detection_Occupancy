import numpy as np
import cv2
import os, sys

"""This method computes Surf Features for detection of occupancy algorithm."""

def computeSurfFeatures(masked_img):
	#Create SURF, the alpha coeficient must be specified
	surf = cv2.xfeatures2d.SURF_create(500)
	#Detect and Compute the keypoints
	kp, des = surf.detectAndCompute(masked_img,None)
	return kp,des

"""Flann Matcher method."""

def matcher(des1, des2):
	#Inicialize Flann Matcher
	FLANN_INDEX_KDTREE = 0
	index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
	search_params = dict(checks = 50)
	flann = cv2.FlannBasedMatcher(index_params, search_params)
	#Compute Flann Matches
	matches = flann.knnMatch(des1, des2, k=2)
	return matches

"""Method that returns an array of good matches."""

def matcher_select(matches):
	#Select good matches (OPCIONAL!!!!!!! JA ESTEM FENT MASCARES XDDDD)
	good_matches = []
	for m,n in matches:
		if m.distance < 0.75*n.distance:
			good_matches.append(m)
	return good_matches

"""Method that computes Good matches between actual frame and actual Mask."""

def computeGoodMatches(frame, kp1, des1):
	
	#Extract SURF Features from current masked frame
	kp2, des2 = computeSurfFeatures(frame)
	#FlanBasedMatcher to select some matches with a certain distance
	matches = matcher(des1,des2)
	#Select good matches
	good_matches = matcher_select(matches)
	return len(good_matches)
	
	




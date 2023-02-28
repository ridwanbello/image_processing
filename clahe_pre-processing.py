#PRE-PROCESSING CODE

# Install OpenCV library
!pip install opencv-python

# Importing necessary libraries
import cv2 
import numpy as np
import PIL
from PIL import Image
import os


# Create a function for CLAHE Histogram Equalization
def improve_contrast_image_using_clahe(bgr_image: np.array) -> np.array:
    hsv = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)
    hsv_planes = cv2.split(hsv)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    hsv_planes[2] = clahe.apply(hsv_planes[2])
    hsv = cv2.merge(hsv_planes)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
  
  #import cv2
import glob, os, errno

# Def apply clahe function to all images
def apply_clahe():
    for picture in os.listdir(directory):
        image = Image.open(directory + picture).improve_contrast_image_using_clahe(image)
		img.save(directory+picture)

# Convert to Gray Scale
def convert_to_grayscale(directory):
	for picture in os.listdir(directory):
		img = Image.open(directory + picture).convert('L')
		img.save(directory+picture)

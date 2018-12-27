# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 10:02:15 2018

@author: David.Landers

This function reads in digital micrograph files as a numpy array, and changes the data to 
uint16 so as to be usable by opencv and it's image processing techniques.


Inputs -
Dir - Directory where files are stored
fiename - filename of specific file you wish to load

Outputs -
img.data - Returns a numpy array containing just the pixel intensity values
"""
import numpy as np
import hyperspy.api as hs
import os


def read_micrograph(filename):
    # Set directory
    # os.chdir(Dir)

    ##This next line is for reading multiple files - not neccessary yet for me##
    # for file in glob.glob("*.dm3"): #glob.glob is the function that finds files. *.dm3 means find all files with .dm3 ending extension.

    img = hs.load(filename)  # Hyperspy function to load dm3 files

    # The pixel intensity values are stored in the .data extension - as a numpy array.
    # The DM3 data comes in as datatype float32, in order to display it in python,
    # or save as a tiff, I round and convert the values to integers. The range of the
    # micrographs I was dealing with was from 0-65535 - 2^16 (so I converted to uint16). Sometimes the range in intensity
    # can be larger. It is simple to work in images which have grayscale values
    # from 0-255, but the extra resolution in the intensity dimension could be
    # valuable to you.

    img.data = np.around(
        img.data)  # Round to integer - straight converstion to uint16 floors the value - would rather round

    img.data = img.data.astype('uint16')  # Change to data type int

    ##----## - William - You definitely know this but this is an example of how I save the file as a tiff
    # after I have processed the data (with blur, thresholding etc...)

    # file = file[:-4] #Remove the last 4 characters (i.e .dm3)
    # file = file + ".tiff" #add tiff to end of file name
    # cv2.imwrite(file, img)

    ##----##

    return img.data


# Silocon_superSTEM_GO_UA2%_27-05-2018_Area2_0017.dm4
read_micrograph("Silocon_superSTEM_GO_UA2%_27-05-2018_Area2_0017.dm4")

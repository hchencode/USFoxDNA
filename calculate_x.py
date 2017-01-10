#!/usr/bin/env python
'''
1. Calculate x with input of distance between the related site

(hchencode |14 November 2016)
'''
# usage: "python3 calculate_x.py suffix1 suffix2"
# where suffix1 and suffix2 will be present in the name of output file as:  "x_suffix1_suffix2.dat"

import sys
import numpy as np

# get the suffix of the output file

try:
    suffix1 = sys.argv[1]
except:
    suffix1 = None

try:
    suffix2 = sys.argv[2]
except:
    suffix2 = None
    

# load the distance file
# track
infile_t1 = np.loadtxt("dist_35_34.dat")
infile_t2 = np.loadtxt("dist_34_0.dat")
infile_t3 = np.loadtxt("dist_0_102.dat")

# motor leg side 
infile_m1 = np.loadtxt("dist_122_45.dat")
infile_m2 = np.loadtxt("dist_45_102.dat")
infile_m3 = np.loadtxt("dist_102_0.dat")

# calculate the vector of the track
# track
tx = infile_t1[:,2]/2 + infile_t2[:,2] + infile_t3[:,2]/2
ty = infile_t1[:,3]/2 + infile_t2[:,3] + infile_t3[:,3]/2
tz = infile_t1[:,4]/2 + infile_t2[:,4] + infile_t3[:,4]/2

# motor leg side
mx = infile_m1[:,2]/2 + infile_m2[:,2] +infile_m3[:,2]/2
my = infile_m1[:,3]/2 + infile_m2[:,3] +infile_m3[:,3]/2
mz = infile_m1[:,4]/2 + infile_m2[:,4] +infile_m3[:,4]/2

t = infile_t1[:,0]
np.savetxt("t.dat",t)

# calculate x
x = np.sqrt(tx**2 + ty**2 + tz**2)*(0.5-(tx*mx + ty*my + tz*mz)/(tx**2 + ty**2 + tz**2))
if suffix1 is not None:
    if suffix2 is not None:
        outfilename = "x_%s"%suffix1+"_%s"%suffix2
    else:
        outfilename = "x_%s"%suffix1
else:
    outfilename = "x"

np.savetxt("%s.dat"%outfilename,x)

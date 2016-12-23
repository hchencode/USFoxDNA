#!/usr/bin/env python
"""
generate the histogram of x distrabution with input of x.dat

(11 November 2016)
"""


import numpy as np
    
# load x file
x = np.loadtxt("x.dat")

# try:
    # x = np.loadtxt("x.dat")
# except:
    # x = np.loadtxt("x.txt")

    
iqr = np.percentile(x, 75) - np.percentile(x,25)
h   = 2*iqr/10
n   = int((max(x)-min(x))/h)

    
(p,bins) = np.histogram(x, bins=n, normed=True)

bins = 0.5*(bins[1:]+bins[:-1])

datafile = open("x_hist_iqr.dat","w")     # Open(or create) a .txt document named by medata, as "write" style

for j in np.arange(n) :
    # Translate the data to "string" type 
    binst   = '%f' %bins[j]
    pt      = '%f' %p[j]
    # write the strings to ".txt" document
    datafile.write(binst+'	'+pt+'\n')
datafile.close()

# x_max = np.max(x)//1 + 1
# x_min = np.min(x)//1
# n     = 30 
# s     = (x_max - x_min)/n
# bin = s*int(x/s)

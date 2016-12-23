#!/usr/bin/env python
"""
generate the histogram of x distrabution.

(23 December, 2016)
"""
# Usage: "python histogram_x.py x.dat"

import sys
import numpy as np
    
# load x file
xmean = sys.argv[1]
x = np.loadtxt(xmean)

# generate the number of bins
iqr = np.percentile(x, 75) - np.percentile(x,25)
h   = 2*iqr/10
n   = int((max(x)-min(x))/h)

    
(p,bins) = np.histogram(x, bins=n, normed=True)

bins = 0.5*(bins[1:]+bins[:-1])

outfile = "hist_"+sys.argv[1]
datafile = open("%s"%outfile,"w")     # Open(or create) a .txt document named by medata, as "write" style

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

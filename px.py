#!/usr/bin/env python
'''
1. Calculate x with input of distance between the related site
2. Calculate the x_mean and x_std
3. Generate the histogram of x distrabution

(hchencode |14 November 2016)
'''

import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

 
# <1>. Calculate x with input of distance between the related site
    
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
np.savetxt("x.dat",x)


# <2>. Calculate the mean value and standard deviation of x directely
x_mean = np.mean(x)
x_std  = np.std(x)

x_m = '%f' %x_mean
x_s = '%f' %x_std

result_mean = open("x_mean.dat","w") # mean value
result_mean.write(x_m + '\n')
result_mean.close()

result_std = open("x_std.dat","w") # standard deviation
result_std.write(x_s + '\n')
result_std.close()

# <3>. Generate the histogram of x distrabution

n = 25
   
(p,bins) = np.histogram(x, bins=n, normed=True)

bins = 0.5*(bins[1:]+bins[:-1])

datafile = open("x_hist.dat","w")     # Open(or create) a .txt document named by medata, as "write" style
for j in np.arange(n) :
    # Translate the data to "string" type 
    binst   = '%f' %bins[j]
    pt      = '%f' %p[j]
    # write the strings to ".txt" document
    datafile.write(binst+'	'+pt+'\n')
datafile.close()


'''
# <3> Get the fitted curve

text1_x = (np.max(t)-np.min(t))/10 + np.min(t)
text1_y = np.max(x_l)
text2_x = (np.max(x_l)-np.min(x_l))/10 + np.min(x_l)
text2_y = 9*np.max(x_p)/10

#print (text1_x)

# Figure the probability distribution of x
fig1 = plt.figure()
plt.subplot(211)
plt.plot(t, x,'k', t, x_mean* np.exp(0*t), 'r')
plt.xlabel('configuration')
plt.ylabel('x')
plt.title('"x" vs. time')
plt.text(text1_x,text1_y,'x_mean = %g    x_std = %g  '%(x_mean, x_std))

hist_fit = gauss_f(x_l, params[0], params[1], params[2])
plt.subplot(212)
plt.plot(x_l, x_p, 'bo', label='Data')
plt.plot(x_l, hist_fit, 'r')
#plt.plot(x_l, gauss_f(x_l, params[0], params[1], params[2]), 'r')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.title('probabilyty distribution of "x"')
plt.text(text2_x,text2_y,'x_mean_fitted = %g   x_std_fitted = %g  '%(x_mean_fitted, x_std_fitted))

plt.show()
'''

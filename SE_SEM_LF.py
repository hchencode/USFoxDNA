import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

 
# <1>. Calculate x with input of distance between the related site
    
# load the data file

x_mean1 = np.loadtxt("x_mean1.dat")
x_mean2 = np.loadtxt("x_mean2.dat")
x_mean3 = np.loadtxt("x_mean3.dat")
x_mean4 = np.loadtxt("x_mean4.dat")
x_mean5 = np.loadtxt("x_mean5.dat")

x_std1 = np.loadtxt("x_std1.dat")
x_std2 = np.loadtxt("x_std2.dat")
x_std3 = np.loadtxt("x_std3.dat")
x_std4 = np.loadtxt("x_std4.dat")
x_std5 = np.loadtxt("x_std5.dat")

f      = np.loadtxt("force.dat")



# Calculate the SE and SEM

x_mean = (x_mean1 + x_mean2 + x_mean3 + x_mean4 + x_mean5)/5
x_std  = (x_std1 + x_std2 + x_std3 + x_std4 + x_std5)/5
x_sem  = np.zeros(13)
for i in range(13):
    x_sem[i] = np.std([x_std1[i]+x_std2[i]+x_std3[i]+x_std4[i]+x_std5[i]])
    
np.savetxt("x_mean.dat",x_mean)
np.savetxt("x_std",x_std)
np.savetxt("x_sem.dat",x_sem)



# Do the curve fitting

# Define the function with parameters
k_B_T = 4.12 # k_B*(273.15+25) kelvin
def x_f(f, x_0, l, b, f_0):	
    return x_0 + l*(1/np.tanh((f-f_0)*b/k_B_T)-1/((f-f_0)*b/k_B_T))

# Set some given data
x_given = x_mean[2:-2]
f_given = f[2:-2]
x_std_given = x_std[2:-2]

params, extras = curve_fit(x_f, f_given, x_given)

hist_fit = x_f(f[1:-1], params[0], params[1], params[2], params[3])

# Output / Plot the results
x_0_t   = '%f' %params[0]
l_t     = '%f' %params[1]
b_t     = '%f' %params[2]
f_0_t   = '%f' %params[3]

param_file = open("parameters.dat","w")
param_file.write("x_0_t: " + x_0_t + '\n' + "l_t: " + l_t + '\n' + "b_t: " + b_t + '\n' + "f_0_t: " + f_0_t + '\n')
param_file.close()

print("x_0=%g, l=%g, b=%g, f_0=%g " %(params[0], params[1], params[2], params[3]))

#x_ax = range(-20,22,2)
#y_ax = range(-8,12,2)

fig1 =plt.figure()
#plt.errorbar(f_given, x_given, x_std,x_sem, fmt='o')
plt.errorbar(f[1:-1], x_mean[1:-1],x_std[1:-1], fmt='o')
#plt.errorbar(f[1:-1]-0.2, x_mean[1:-1],x_sem[1:-1],fmt='.')
plt.plot(f[1:-1], hist_fit, 'r')
plt.axis([-20.5,20.5,-8,15])
#plt.plot(x_ax,np.zeros(len(x_ax)),'k')
#plt.plot(np.zeros(len(y_ax)),y_ax,'k')
plt.legend(['fit', 'data'])
plt.xlabel("force / pN")
plt.ylabel("lateral  displacement / nm")
plt.show()

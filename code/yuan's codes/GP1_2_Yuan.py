'''
p2
1-D diffusion
'''
from copy import copy
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def diffuse(time):
    #initialize
    time=time
    dt=0.01
    dx=1.0
    D=2.0
    peak=50
    nt=100
    
    center=int(nt/2)
    #rho=[peak*np.exp(-10*(i-center)**2) for i in range(nt)]
    rho=[0.0]*nt
    rho[center]=peak
    rho_new=[0.0]*nt
    #print(rho)
    
    for n in range(time):
        for i in range(nt-1):
            rho_new[i]=rho[i]+D*dt/dx/dx*(rho[i+1]+rho[i-1]-2*rho[i])
        rho=copy(rho_new)
    return rho


#create snapshots for different time
sigma2=[]
tests=[100,500,1000,5000,10000,12000]
for time in tests:
    rho=diffuse(time)
    plt.plot(rho)
    
    #gaussian fit
    def gauss(x,A,mu,sigma):
        return A*np.exp(-(x-mu)**2/(2.*sigma**2))
    
    amplitude_guess=max(rho)
    mu_guess=int(len(rho)/2)
    xrange=range(len(rho))
    popt,pcov=curve_fit(gauss,xrange,rho,p0=[amplitude_guess,mu_guess,1.0])
    
    
    
    fit=[]
    for x in xrange:
        fit.append(gauss(x,popt[0],popt[1],popt[2]))
    plt.plot(fit,'.')
    
    plt.legend(["unfitted","fitted"],loc='upper right')
    
    sigma2.append(popt[2]**2)
    
plt.xlabel("x")
plt.ylabel(r"$\rho$")
plt.title(r"$\rho(x)$ at 6 different time")
plt.savefig("snapshots.pdf")
plt.close()


#sigma fit
dt=0.01
realtime=[dt*test for test in tests]

plt.plot(realtime,sigma2,'.')

#straight line fit
def l(x,a):
    return a*x
popt,pcov=curve_fit(l,realtime,sigma2)

line=[popt[0]*x for x in realtime]

#plot stuff
plt.plot(realtime,line,'-')
plt.title("$\sigma^2$ vs. t")
plt.xlabel("t")
plt.ylabel(r"$\rho$")
plt.legend(["unfitted","fitted"],loc='upper left')
plt.text(80,10,"fitted D:"+str(round(popt[0]/2,3)))

plt.savefig("sigma2fit.pdf")






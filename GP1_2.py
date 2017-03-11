import pylab
from scipy.optimize import curve_fit

class Diffusion_1D(object):
	def __init__(self,D,N=101,dx=1,dt=0.01):# N is the number of the grid sites, D is the diffusion constant
		self.N=N
		self.D=D
		self.dx=dx
		self.dt=dt
		self.t=0
		self.x=[-(self.N-1)/2*self.dx+i*dx for i in range(N)]
		self.rho=[pylab.exp(-1000*self.x[i]*self.x[i]) for i in range(N)]
		self.rho_new=[0.0]*N

	def diffuse(self): #calculate the distribution at t+dt after diffusion
		for i in range(self.N-2):
			self.rho_new[i+1]=self.rho[i+1] + self.D*self.dt/self.dx/self.dx* (self.rho[i+2]+self.rho[i]-2*self.rho[i+1])
		self.rho=self.rho_new[:]
		self.t+=self.dt


def Normal_Distribution(x,sigma):
	return 1/pylab.sqrt(2*pylab.pi)/sigma*pylab.exp(-x*x/2/sigma/sigma)

tfit=[] 
sigmafit=[] #fitted parameter sigma at time tfit

for i in [100,1000,5000,10000,15000]:
	Dif=Diffusion_1D(2)
	for j in range(i):
		Dif.diffuse()
	popt,pcov=curve_fit(Normal_Distribution,Dif.x,Dif.rho)
	tfit.append(Dif.t)
	sigmafit.append(popt)

#theoretical sigma
t=[2*i for i in range(100)]
sigma=[pylab.sqrt(4*i) for i in t]

#plot figure
pylab.plot(t,sigma,'r-',linewidth=2,label='$\sigma (t)= \sqrt{2Dt} $')
pylab.plot(tfit,sigmafit,'ko')
pylab.xlabel('t')
pylab.ylabel('$\sigma(t)$')
pylab.title('Parameter $\sigma$ of the diffusion equation')
pylab.legend(loc=0)
pylab.savefig('sigma.pdf')
pylab.show() 

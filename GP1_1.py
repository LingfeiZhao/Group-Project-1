import random
import pylab

class RandomWalk_2D(object):
	def __init__(self,steps,samples=pow(10,4)): #initialize the walker
		self.x=0
		self.y=0
		self.steps=steps
		self.sumx=0 #sum of x
		self.sumx2=0 #sum of x^2
		self.r2=0  #sum of r^2
		self.samples=samples #number of samples for average

	def walk(self): #let the walker walk "steps" steps
		for i in range(self.steps):
			if random.randint(0,1):
				self.x+=2*random.randint(0,1)-1
			else:
				self.y+=2*random.randint(0,1)-1

	def reset(self): #reset the position of the walker
		self.x=0
		self.y=0

	def average_x(self): #average position x 
		for i in range(self.samples):
			self.walk()
			self.sumx+=self.x
			self.reset()
		return self.sumx/float(self.samples)

	def average_x2(self): #average x^2
		for i in range(self.samples):
			self.walk()
			self.sumx2+=self.x*self.x
			self.reset()
		return self.sumx2/float(self.samples)

	def average_r2(self): #average r^2
		for i in range(self.samples):
			self.walk()
			self.r2+=self.x*self.x+self.y*self.y
			self.reset()
		return self.r2/float(self.samples)

#initialize the lists for average data
N=range(4,101)
Average_x=[]
Average_x2=[]
Average_r2=[]

for n in N:
	Walk=RandomWalk_2D(n)
	Average_x.append(Walk.average_x())
	Average_x2.append(Walk.average_x2())
	Average_r2.append(Walk.average_r2())

#plot figures
pylab.plot(N,Average_x,'co')
pylab.xlabel('n')
pylab.ylabel('<$x_n$>')
pylab.savefig('average_x.pdf')
pylab.show()

pylab.plot(N,Average_x2,'co')
pylab.xlabel('n')
pylab.ylabel('<$x^2_n$>')
pylab.savefig('average_x_sqaure.pdf')
pylab.show()

pylab.plot(N,Average_r2,'co')
pylab.xlabel('n')
pylab.ylabel('<$r^2_n$>')
pylab.savefig('average_r_sqaure.pdf')
pylab.show()




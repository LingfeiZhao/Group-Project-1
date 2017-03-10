import random
import pylab

class RandomWalk_2D(object):
	def __init__(self,steps,samples=pow(10,4)): #initialize the walker
		self.x=0 #position x
		self.y=0 #position y
		self.steps=steps #number of steps 
		self.sumx=0 #sum of x
		self.sumx2=0 #sum of x^2
		self.sumr2=0  #sum of r^2
		self.samples=samples #number of samples for average
		self.average_data={} #the directory of average data

	def walk(self): #let the walker walk "steps" steps
		for i in range(self.steps):
			if random.randint(0,1):
				self.x+=2*random.randint(0,1)-1
			else:
				self.y+=2*random.randint(0,1)-1

	def reset(self): #reset the position of the walker
		self.x=0
		self.y=0

	def average(self): #average over all the samples
		for i in range(self.samples):
			self.walk()
			self.sumx+=self.x
			self.sumx2+=self.x*self.x
			self.sumr2+=self.x*self.x+self.y*self.y
			self.reset()

		self.average_data.update(
			{'x':self.sumx/float(self.samples),
			'x2':self.sumx2/float(self.samples),
			'r2':self.sumr2/float(self.samples)} )


#initialize the lists for average data
N=range(4,101)
Average_x=[]
Average_x2=[]
Average_r2=[]

for n in N:
	Walk=RandomWalk_2D(n)
	Walk.average()
	Average_x.append(Walk.average_data['x'])
	Average_x2.append(Walk.average_data['x2'])
	Average_r2.append(Walk.average_data['r2'])

#plot figures
pylab.plot(N,Average_x,'co',label='<$x_n$>')
pylab.plot(N,Average_x2,'ro',label='<$x^2_n$>')
pylab.plot(N,Average_r2,'ko',label='<$r^2_n$>')
pylab.legend()
pylab.xlabel('n')
pylab.ylabel('Average Data over $10^4$ Samples')
pylab.savefig('average.pdf')
pylab.show()

import random
import pylab
from time import clock


class Mixing(object):
	def __init__(self,Nx=120,Ny=80):
		self.Nx=Nx
		self.Ny=Ny
		self.unoccupied=[] # we want to operate on the unoccupied locations
		#initialize the grid
		self.grid=[[0]*(Ny+2) for i in range(Nx+2)] # 0 represent unoccupied and boundary, set boundary as 0
		for i in range(Nx/3):
			for j in range(Ny):
				self.grid[i+1][j+1]=1 # 1 represent gas A
				self.grid[-(i+2)][j+1]=-1 # -1 represent gas B
		# Initialize the opsitions that are unoccupied
		for i in range(Nx):
			for j in range(Ny):
				if self.grid[i+1][j+1]==0:
					self.unoccupied.append((i+1,j+1))
		self.len_unoccupied=len(self.unoccupied)

	def diffuse(self):
		# pick a random unoccupied location 
		rand_int=random.randint(0,4*self.len_unoccupied-1)
		position=rand_int%self.len_unoccupied
		index=self.unoccupied[position]
		i=index[0]
		j=index[1]
		# look at a random neighbor
		direction=rand_int/self.len_unoccupied
		if direction==0:
			i+=1
		elif direction==1:
			i-=1
		elif direction==2:
			j+=1
		else:
			j-=1
		# if this neighbor has gas, grap it
		if self.grid[i][j]==0: #notice that the boundaty position is 0
			pass
		else:
			# exchange the two positions
			self.grid[index[0]][index[1]]=self.grid[i][j]
			self.grid[i][j]=0 
			# update the unoccupied list
			self.unoccupied[position]=(i,j)

# problem b)
Nx=120

for i in range(6): # number of subplots
	nA=[0]*Nx
	nB=[0]*Nx

	start_time=clock()
	gas=Mixing()
	power=i+3 # number of iterations is 10^power
	for j in range(pow(10,power)):
		gas.diffuse()
	end_time=clock()

	# calculate nA(x) and nB(x)
	for j in range(Nx):
		for pos in gas.grid[j]:
			if pos==1:
				nA[j]+=1
			elif pos==-1:
				nB[j]+=1

	# plot figures
	pylab.figure(1)
	pylab.subplot(2,3,i+1)
	pylab.imshow(gas.grid, cmap='RdBu')
	pylab.axis('tight')
	pylab.title('10$^%d$steps, %.1f sec'%(power,end_time-start_time) )
	pylab.tight_layout()
	pylab.savefig('GP1_3b_1.pdf')

	pylab.figure(2)
	pylab.subplot(2,3,i+1)
	pylab.plot(nA,'co',label='nA(x)')
	pylab.plot(nB,'ro',label='nB(x)')
	pylab.legend(loc=0,numpoints=1,prop={'size':12},ncol=2,borderaxespad=0,mode='expand')
	pylab.xlabel('x')
	pylab.ylabel('n')
	pylab.axis('tight')
	pylab.ylim([-1,100])
	pylab.title('10$^%d$steps, %.1f sec'%(power,end_time-start_time) )
	pylab.tight_layout()
	pylab.savefig('GP1_3b_2.pdf')

pylab.show()

# problem c)
Nx=120
nA_sum=[[0]*Nx for i in range(6)]
nB_sum=[[0]*Nx for i in range(6)]
N_repeats=100

for k in range(N_repeats):
	for i in range(6): # number of subplots
		nA=[0]*Nx
		nB=[0]*Nx

		gas=Mixing()
		power=i+3 # number of iterations is 10^power
		for j in range(pow(10,power)):
			gas.diffuse()

		# calculate nA(x) and nB(x)
		for j in range(Nx):
			for pos in gas.grid[j]:
				if pos == 1:
					nA[j] += 1
				elif pos == -1:
					nB[j] += 1

		for j in range(Nx):
			nA_sum[i][j] += nA[j]
			nB_sum[i][j] += nB[j]


nA=[[y/float(N_repeats) for y in x] for x in nA_sum]
nB=[[y/float(N_repeats) for y in x] for x in nB_sum]

for i in range(6):
	pylab.subplot(2,3,i+1)
	pylab.plot(nA[i],'co',label='nA(x)')
	pylab.plot(nB[i],'ro',label='nB(x)')
	pylab.legend(loc=0,numpoints=1,prop={'size':12},ncol=2,borderaxespad=0,mode='expand')
	pylab.xlabel('x')
	pylab.ylabel('n')
	pylab.axis('tight')
	pylab.ylim([-1,100])
	pylab.title('10$^%d$steps'%(i+3) )
	pylab.tight_layout()
	pylab.savefig('GP1_3c.pdf')

pylab.show()

import random
import pylab

class Mixing(object):
	def __init__(self,Nx=120,Ny=80):
		self.Nx=Nx
		self.Ny=Ny
		self.operate=[] # the list of the positions that we want to operate on
		#initialize the grid
		self.grid=[[0]*Ny for i in range(Nx)] # 0 represent unoccupied
		for i in range(Nx/3):
			for j in range(Ny):
				self.grid[i][j]=1 # 1 represent gas A
				self.grid[-(i+1)][j]=-1 # -1 represent gas B
		# Initialize the opsitions that can be operated
		for i in range(Nx):
			for j in range(Ny):
				if self.can_operate((i,j)):
					self.operate.append((i,j))

	def can_operate( self, (i,j) ):# we only operate on the unoccupied position, also they should have occupied neighbors
		can=False
		if i!=0:
			can=can or self.grid[i-1][j]
		if i!=self.Nx-1:
			can=can or self.grid[i+1][j]
		if j!=0:
			can=can or self.grid[i][j-1]
		if j!=self.Ny-1:
			can=can or self.grid[i][j+1]
		can= can and self.grid[i][j]==0
		return can

	def update(self):
		index=self.operate[random.randint(0,len(self.operate)-1)]
		if self.can_operate(index):
			i=index[0]
			j=index[1]
			# look at a random neighbor
			if random.randint(0,1):
				i+=2*random.randint(0,1)-1
			else:
				j+=2*random.randint(0,1)-1

			# if this neighbor has gas, grap it
			if i==-1 or i==self.Nx or j==-1 or j==self.Ny:
				pass
			elif self.grid[i][j]==0:
				pass
			else:
				self.grid[i][j]=0
				self.grid[index[0]][index[1]]=1 
				# update the operate list
				self.operate.remove(index)
				for a in [i-2,i-1,i,i+1,i+2]:
					for b in [j-2,j-1,j,j+1,j+2]:
						if 0<=a<self.Nx and 0<=b<self.Ny:
							if self.can_operate((a,b)):
								self.operate.append((a,b))
		else:
			self.operate.remove(index)

gas=Mixing()
for i in range(pow(10,7)):
	gas.update()

pylab.imshow(gas.grid)
pylab.show()




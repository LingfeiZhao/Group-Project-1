'''
Random Walk
Yuan Ji
'''
import numpy as np
import matplotlib.pyplot as plt
import random
def successors(point):
    dxlist=[-1,1,0,0]
    dylist=[0,0,-1,1]
    succ=[]
    xp=point[0]
    yp=point[1]
    for (dx,dy) in zip(dxlist,dylist):
        succ.append((xp+dx,yp+dy))
        
    return succ
        
def randomwalk(steps):
    NSteps = steps   # Number of steps in simulation.
    xStart = 0   # x coordinate of starting location. Origin is at centre of square
    yStart = 0   # y coordinate of starting location. Origin is at centre of square
    
    x = xStart   # x coordinate of point.
    y = yStart   # y coordinate of point.
    point=(x,y)
    xList = []   # List of the x coordinates of all points visited.
    yList = []   # List of the y coordinates of all points visited.
    xList.append(xStart)
    yList.append(yStart)
    
    points=[]
    points.append(point)
    
    for i in range(NSteps):
        point=random.choice(successors(point))
        points.append(point)
        xList.append(point[0])
        yList.append(point[1])
    d=dict()
    for poin in points:
        if not d.has_key(poin):
            d[poin]=0
        d[poin]+=1
    #print d
    pointSet=d.keys()
    #print pointSet
    valueSet=d.values()
    #print valueSet
    
    return point
    '''
    plt.rc('grid', linestyle="-", color='black')
    xl=[x for x,y in pointSet]
    yl=[y for x,y in pointSet]
    plt.scatter(xl,yl, c=valueSet,marker='.')
    maxlim=max(max(xl),max(yl))
    minlim=min(min(xl),min(yl))
    plt.xlim([minlim-10,maxlim+10])
    plt.ylim([minlim-10,maxlim+10])
    #plt.xticks(np.arange(min(xl)-5,max(xl)+5))
    #plt.yticks(np.arange(min(yl)-5,max(yl)+5))
    plt.grid(True)
    
    plt.show()
    '''
    
tests=range(3,101)
xaverage=[]
x2average=[]
r2aver=[]
for test in tests:
    endx=[]
    endxsquare=[]
    r2=[]
    for i in range(10000):
        endpoint=randomwalk(test)
        endx.append(endpoint[0])
        endxsquare.append(endpoint[0]**2)
        r2.append(endpoint[0]**2+endpoint[1]**2)
    xaverage.append(np.average(endx))
    x2average.append(np.average(endxsquare))
    r2aver.append(np.average(r2))
plt.plot(tests,xaverage,tests,x2average, tests, r2aver)
plt.xlabel("n")
plt.title("<$x_n$>,<$x^2_n$>,<$r^2_n$> versus n")
plt.legend(["<$x_n$>","<$x^2_n$>", "<$r^2_n$>"],loc='upper right')
plt.savefig("P1.pdf")
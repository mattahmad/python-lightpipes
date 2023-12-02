from LightPipes import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

GridSize = 10*mm
GridDimension = 128
lambda_ = 1000*nm #lambda_ is used because lambda is a Python build-in function.

R=2.5*mm
xs=0*mm; ys=0*mm
T=0.8

Field = Begin(GridSize, lambda_, GridDimension)
Field=GaussAperture(R,xs,ys,T,Field)
NewGridDimension=int(GridDimension/4)
Field=Interpol(GridSize,NewGridDimension,0,0,0,1,Field)
I=Intensity(0,Field)
I=np.array(I)

#3d plot:
X=range(NewGridDimension)
Y=range(NewGridDimension)
X, Y=np.meshgrid(X,Y) 
fig=plt.figure(figsize=(10,6))
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y,I,
                rstride=1,
                cstride=1,
                cmap='rainbow',
                linewidth=0.0,
                )
ax.set_zlabel('Intensity [a.u.]')
plt.show()
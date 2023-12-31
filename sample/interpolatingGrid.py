#! python3

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from LightPipes import *

print(LPversion)
wavelength=1000*nm
size=10*mm
N=256
w=5*mm

z=400*m
sizenew=400*mm
Nnew=64

F = Begin(size,wavelength,N)

F = RectAperture(w, w,0,0, 0, F)
F = Forvard(0.2*m,F)
I0=Intensity(2,F)

F = Interpol(7.5*mm,Nnew,0,0,0,1,F)
F=Forward(z,sizenew,Nnew,F)
I1=Intensity(2,F)
I1=np.array(I1)
plt.imshow(I0, cmap='gray');plt.axis('off'); plt.title('near field')
plt.show()
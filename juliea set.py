
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
fig,ax = plt.subplots()
fig.subplots_adjust(bottom=0.3)
a=np.linspace(-3,3,130)
b=np.linspace(-3,3,130)
cn=a[np.newaxis,:]+b[:,np.newaxis]*1j
za=np.zeros_like(cn)
za=za*0.7885
def divg(z):
 c=cn
 for k in range (10):
    
    c=c**2+z
 for i in range (130):
      for j in range (130):
         if abs(c[i,j])>=18**(1/2):
          c[i,j]=0
         else : 
            c[i,j]=1
 return c

axcolor = 'Green'
axamp = plt.axes([0, 0, 0.65, 0.055], facecolor=axcolor)
s= Slider(axamp, 'Amp', 0, 2*np.pi, valinit=1)
axam = plt.axes([0, 0.065, 0.65, 0.055], facecolor=axcolor)
u= Slider(axam, 'Amp', 0, 1, valinit=1)

img=ax.imshow(abs(divg(za)),cmap='binary')
def xal(f):
   global img,za
   za.fill(np.cos(s.val)+(np.sin(s.val))*1j)
   img.set_data(abs(divg(za)))

s.on_changed(xal)
plt.show()



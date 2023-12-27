import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def julia(z, c, max_iter=100):
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z*z + c
    return 0

def julia_set(xmin, xmax, ymin, ymax, width, height, c, max_iter=100):
    r1 = np.linspace(xmin, xmax, width)
    r2 = np.linspace(ymin, ymax, height)
    n3 = np.empty((width,height))
    for i in range(width):
        for j in range(height):
            n3[i,j] = julia(r1[i] + 1j*r2[j], c, max_iter)
    return (r1, r2, n3)

def update(val):
    c = complex(real_slider.val, imag_slider.val)
    r1, r2, n3 = julia_set(-2, 2, -2, 2, 100, 100, c)
    ax.clear()
    ax.imshow(n3.T, extent=[-2,2,-2,2])
    fig.canvas.draw_idle()

fig, ax = plt.subplots()
r1, r2, n3 = julia_set(-2, 2, -2, 2, 1000, 1000, -0.8 + 0.156j)
ax.imshow(n3.T, extent=[-2,2,-2,2])

axcolor = 'lightgoldenrodyellow'
ax_real = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_imag = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)

real_slider = Slider(ax_real, 'Real', -2, 2, valinit=-0.6)
imag_slider = Slider(ax_imag, 'Imag', -2, 2, valinit=0.156)

real_slider.on_changed(update)
imag_slider.on_changed(update)

plt.show()
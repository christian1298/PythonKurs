import numpy as np
import matplotlib.pyplot as mpl
C=1e-9
R=1590
#h = 1/(1+ np.imag(2*m.pi*f*C*R))

def h(f):
    return 1/(1+ 1j*(2*np.pi*f*C*R))

f = np.logspace(1,7,100)

mag = np.abs(h(f))
phase = np.angle(h(f))

mpl.subplot(2,1,1)
mpl.semilogx(f,20*np.log10(mag))
mpl.grid()
mpl.xlabel("f in Hz")
mpl.ylabel("Amplitudengang")


mpl.subplot(2,1,2)
mpl.semilogx(f,phase)
mpl.grid()
mpl.xlabel("f in Hz")
mpl.ylabel("Frequenzgang")


mpl.show()

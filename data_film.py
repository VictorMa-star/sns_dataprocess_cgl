#!/usr/bin/python3
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
import h5py
from SNS_function import SNS_data
import SNS_dataset

'''plot the spectrum successively so that the trend can be seen'''

result_path = '../result/'

# fileName = 'SN_ellipticity_333K_b2.h5'
fileName = 'SNS_R_IP_295K_site6_12.h5'
f = h5py.File(result_path + fileName, 'r')

data = []
for name in f.keys():
    # if '..\\20220\\' + name in SNS_dataset.SNS_R_IP_320K:
        data.append(SNS_data(f, name))
f.close()

# data = data[:2]

seg_len = np.shape(data[0].PSD)[0]*2 # Nyquist
sr = data[0].sr
df = sr/seg_len
freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

# path = 'raw/test time domain (not blocked)'
# X = np.loadtxt(path)

# ### test signal
T = 0.2
t_axis = np.linspace(0, T, 100)
# data = []
# for i in range(10):
    # data.append(np.sin(i*t_axis))


### plot all
# tau = 3
# plt.plot(t_axis, data[0], 'bo')
# plt.plot(X[:-1*tau], X[tau:], 'b--', lw=1)

### animation
fig, ax = plt.subplots()
xdata, ydata = [], []
# dot, = plt.plot([], [], 'bo')
ln, = plt.plot([], [], 'b-')
# tail_len = 20


def init():
    ax.set_xlim(0, 0.2)
    ax.set_ylim(-1e-9, 1e-8)
    # ax.set_ylim(-1, 1)

    return ln,

def update(frame):
    # # print(frame) # for debugging
    ydata = data[frame].PSD[:,0]/data[frame].factor**2

    seg_len = np.shape(ydata)[0]*2 # Nyquist
    sr = data[frame].sr
    df = sr/seg_len
    freq = np.linspace(0, df*seg_len/2, seg_len//2)/1e6

    xdata = freq
    
    ln.set_data(xdata, ydata)
    # ln.set_data(t_axis, np.sin(frame*t_axis))

    # dot.set_data(xdata, ydata[-1*(tail_len+1):-1])
    return ln,


ani = FuncAnimation(fig, update, frames=list(range(len(data))), init_func=init, blit=True, interval=500, repeat=False)
# ani = FuncAnimation(fig, update, frames=list(range(10)), init_func=init, blit=True, interval=500, repeat=False)

plt.show()

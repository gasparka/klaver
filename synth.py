#%%
import matplotlib.pyplot as plt
import numpy as np
import sounddevice


def tone(f, fs, haronics):
    t = 10
    a = 0.5

    ss = []
    for i in range(0, haronics):
        s = (a / 2**i) * np.sin(f * i * np.linspace(0, t*2*np.pi, t*fs))
        if ss == []:
            ss = s
        else:
            ss += s

    return ss

f = 50
h = 64
ss = tone(f=f, fs=48000, haronics=h) + tone(f=f+(f**-1), fs=48000, haronics=h) + tone(f=f-(f**-3), fs=48000, haronics=h)

# f = f * 2.001
# ss2 = tone(f=f, fs=48000, haronics=32) + tone(f=f+0.01, fs=48000, haronics=32) + tone(f=f-0.01, fs=48000, haronics=32)

# ss = (ss+ss2) / 2

sounddevice.play(ss, fs)  # releases GIL


# %%
from scipy import signal
plt.figure(figsize=(20,10))
f, Pxx_den = signal.periodogram(ss, fs)
plt.semilogy(f, Pxx_den)
plt.ylim([1e-12, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()
# %%

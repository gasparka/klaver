

#%%
import random
random.random() * np.pi
#%%
import matplotlib.pyplot as plt
import numpy as np
import sounddevice
import random

duration = 16
fs = 48000
rr = np.linspace(0.0000001, 1, duration*fs)
r =  np.abs(np.log2(rr))
r /= r.max()

# rr = np.linspace(10, 0, duration*fs)
# r =  np.exp(rr)

# r /= r.max()

gain_slope = r
c = 0
g_freqz = []

def tone(a, f, magic, fs=48000, haronics=32, duration=16):
    global c
    if f > 10000:
        return []

    if f < 20:
        return []

    if a < 0.0001:
        return [] 

    print(a, f)
    c+=1
    g_freqz.append(f)

    rnd_phase = 0
    # res = (a*gain_slope) * np.sin(f * np.linspace(rnd_phase, rnd_phase+duration*2*np.pi, duration*fs))
    res = 0.0001 *gain_slope * np.sin(f * np.linspace(rnd_phase, rnd_phase+duration*2*np.pi, duration*fs))
    for i in range(2, haronics+1):
        childs = tone(a=(a / magic**i), magic=magic*i, f=f*i)
        if childs != []:
            res += childs

        childs = tone(a=(a / magic**i), magic=magic*i, f=f/i)
        if childs != []:
            res += childs

    return res

f = 200
h = 32
fs = 48000
ss = tone(a=0.5, f=f, magic=2) 
print(c)
sounddevice.play(ss, fs)  

# %%
print(sorted(g_freqz))
plt.plot(sorted(g_freqz))

# %%
from scipy import signal
plt.figure(figsize=(20,10))
f, Pxx_den = signal.periodogram(ss, fs)
plt.semilogy(f, Pxx_den)
plt.ylim([1e-12, 1e2])
# plt.xlim([0,4000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()

#%%
import matplotlib.pyplot as plt
import numpy as np
import sounddevice


def tone(a, f, fs, haronics):
    t = 10

    ss = []
    for i in range(0, haronics):
        try:
            s = (a / 2**i) * np.sin(f / i * np.linspace(0, t*2*np.pi, t*fs))
            if ss == []:
                ss = s
            else:
                ss += s
        except ZeroDivisionError:
            pass

    rr = np.linspace(0.001, 0.9, t*fs)
    r =  np.abs(np.log2(rr))
    r /= r.max()
    ss *= r
    # plt.plot(r)

    return ss

f = 440
h = 32
fs = 48000
ss = tone(a=0.5, f=f)

#ss = tone(a=0.25, f=f, fs=48000, haronics=h) + tone(a=0.25, f=(f * 3)/2, fs=48000, haronics=h) + tone(a=0.5, f=(f * 5)/30, fs=48000, haronics=h)
# ss = tone(f=f, fs=48000, haronics=h) + tone(f=f+(f**-1), fs=48000, haronics=h) + tone(f=f-(f**-3), fs=48000, haronics=h)

# f = f * 2.001
# ss2 = tone(f=f, fs=48000, haronics=32) + tone(f=f+0.01, fs=48000, haronics=32) + tone(f=f-0.01, fs=48000, haronics=32)

# ss = (ss+ss2) / 2

sounddevice.play(ss, fs)  # releases GIL

#%%
sounddevice.play(ss, fs)  # releases GIL

# %%
from scipy import signal
plt.figure(figsize=(20,10))
f, Pxx_den = signal.periodogram(ss, fs)
plt.semilogy(f, Pxx_den)
plt.ylim([1e-12, 1e2])
plt.xlim([0,4000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()
# %%
plt.plot(ss)

# %%
import numpy as np
import matplotlib.pyplot as plt
# rr = np.linspace(0, 20, 5*48000)
rr = np.linspace(100, 0, 5*48000)
r =  np.exp(rr)

r /= r.max()
plt.plot(r)
# %%

# %%
r =  np.abs(np.log2(rr))
print(r)
r.max()
# %%

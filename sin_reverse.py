#%%
""" Detect amplitude """
""" Probleem on siis, kui envelope l'heb negativvseks...seda vist ei saagi detekteerida?? 
Hilbert ja hl_envelopes_idx annavad suht sama tulemuse. Kindlasti ei saa kätte "müra" komponenti amplituudis.
Võibolla peaks uurima amplituudi modulatsiooni/demodulatsiooni hoopis, kuigi hilbert vist ongi üks viis selleks. 
Ikkagi...ettevaatlikuks teeb see, et negatiivset amplituuti ei saa kätte..Ehk see probleem pole täiesti lahendatud!
Müra suurust saab tegelt Hilbertiga analüüsida, sest kui nad on samad tekivad 0 errorid beatides!

Hilbert ei toimi, kui on DC offset!!
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def moving_average(inputs, n):
    taps = [1 / n] * n
    return signal.lfilter(taps, [1.0], inputs)

def hl_envelopes_idx(s,dmin=1,dmax=1):
    """
    Input :
    s : 1d-array, data signal from which to extract high and low envelopes
    dmin, dmax : int, size of chunks, use this if size of data is too big
    Output :
    lmin,lmax : high/low enveloppe idx of signal s
    """

    # locals min      
    lmin = (np.diff(np.sign(np.diff(s))) > 0).nonzero()[0] + 1 
    # locals max
    lmax = (np.diff(np.sign(np.diff(s))) < 0).nonzero()[0] + 1 
    
    """
    # using the following might help in some case by cutting the signal in "half"
    s_mid = np.mean(s) (0 if s centered or more generally mean of signal)
    # pre-sorting of locals min based on sign 
    lmin = lmin[s[lmin]<s_mid]
    # pre-sorting of local max based on sign 
    lmax = lmax[s[lmax]>s_mid]
    """

    # global max of dmax-chunks of locals max 
    lmin = lmin[[i+np.argmin(s[lmin[i:i+dmin]]) for i in range(0,len(lmin),dmin)]]
    # global min of dmin-chunks of locals min 
    lmax = lmax[[i+np.argmax(s[lmax[i:i+dmax]]) for i in range(0,len(lmax),dmax)]]
    
    return lmin,lmax

f = 100
fs = 48000
t_sec = 2
t = np.linspace(0, t_sec, fs*t_sec)
amp = 0.1 * (np.linspace(1, 1.5, len(t)) + (np.random.randn(len(t)) * 0.01)) * np.sin(2*np.pi*1*t)
s1 = amp * np.sin(2*np.pi*f*t) + 1

iq = signal.hilbert(s1)
iq.imag += 1
plt.plot(iq.imag)
plt.plot(iq.real)

pow = np.abs(iq)
low_idx2,low_idx = hl_envelopes_idx(s1,dmin=150,dmax=150)
plt.figure(figsize=(15,10))
plt.plot(t, amp, label='tegelik!')
plt.plot(t, pow, label='hilbert')
plt.plot(t[low_idx], s1[low_idx], label='hl_envelopes_idx')
# plt.plot(t, s1, label="s1")
plt.legend()
# plt.plot(s1, label="s1")
# plt.plot(amp, label="amp")
# plt.plot(powl, label="estimated amp")
# plt.plot(amp)

# AVG = 1
# pow_avg = moving_average(pow, AVG)[AVG:]
# err = amp[AVG:] - pow_avg

# plt.figure(figsize=(15,10))
# plt.plot(pow_avg)
# plt.plot(amp)

# plt.figure(figsize=(15,10))
# plt.plot(err)

#%%
t = np.linspace(0,16*np.pi,5000)
s = np.exp(t*1j) + 1

plt.plot(s)
plt.plot(np.abs(s))

#%%
t = np.linspace(0,2*np.pi,5000)
s = 5*np.cos(5*t)*np.exp(-t) + np.random.rand(len(t))

high_idx, low_idx = hl_envelopes_idx(s,dmin=15,dmax=15)

# plot
plt.figure(figsize=(15,10))
plt.plot(t,s,label='signal')
plt.plot(t[high_idx], s[high_idx], 'r', label='low')
plt.plot(t[low_idx], s[low_idx], 'g', label='high')



#%%
f = 10
fs = 48000
t_sec = 1
t = np.linspace(0, t_sec, fs*t_sec)
s1 = np.sin(2*np.pi*f*t)

f = 11
fs = 48000
t_sec = 1
t = np.linspace(0, t_sec, fs*t_sec)
s2 = np.sin(2*np.pi*f*t)

plt.figure(figsize=(15,10))
plt.plot(s1 + s2)
# %%

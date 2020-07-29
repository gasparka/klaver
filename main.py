#%%
import mido

def print_ports(heading, port_names):
    print(heading)
    for name in port_names:
        print("    '{}'".format(name))
    print()

print_ports('Input Ports:', mido.get_input_names())

# %%
"""
Send random notes to the output port.
"""

from __future__ import print_function
import sys
import time
import random
import mido
from mido import Message


if len(sys.argv) > 1:
    portname = sys.argv[1]
else:
    portname = None  # Use default port

portname = 'Midi Through:Midi Through Port-0 14:0'

# A pentatonic scale
notes = [60, 62, 64, 67, 69, 72]

try:
    with mido.open_output(portname, autoreset=True) as port:
        print('Using {}'.format(port))
        note = 60

        on = Message('note_on', note=note)
        print('Sending {}'.format(on))
        port.send(on)
        time.sleep(15)

        off = Message('note_off', note=note)
        print('Sending {}'.format(off))
        port.send(off)
        time.sleep(0.1)
except KeyboardInterrupt:
    pass

print()

# %%
import numpy as np
nn = np.load("samples.npy")
import matplotlib.pyplot as plt
plt.plot(nn)

# %%
import IPython.display
# import librosa
# y, sr = librosa.load(librosa.util.example_audio_file())
IPython.display.Audio(data=nn, rate=48000)

# %%
from scipy.io import wavfile
samplerate, data = wavfile.read("c.wav")
print(f"number of channels = {data.shape[1]}")

length = data.shape[0] / samplerate
print(f"length = {length}s")

import matplotlib.pyplot as plt
import numpy as np
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data[:, 0], label="Left channel")
plt.plot(time, data[:, 1], label="Right channel")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()

# %%
d = data[:, 0]
plt.figure(figsize=(15,15))
plt.plot(d[20000:], label="Left channel")
plt.grid()

# %%

#%%
def get(sec=1, dev='/dev/ttyACM0'):
    DATA_RATE = 1600
    import serial
    serial_device = serial.Serial(
        dev,
        baudrate=115200,
        bytesize=serial.EIGHTBITS,
        parity=serial.PARITY_NONE,
        timeout=1)

    serial_device.read_all()

    buff = []
    while True:
        r = serial_device.read_all()
        if len(r):
            buff.extend(r.split(b'\n'))
            if len(buff) >= DATA_RATE * sec:
                break


    res = []
    for dd in buff:
        if len(dd) == 2:
            i = int.from_bytes(dd, "big", signed=True)
        elif len(dd) == 3:
            b = dd[-2:]
            b = [(b[0] ^ 0x10)] + [b[1]]
            i = int.from_bytes(b, "big", signed=True)
        elif len(dd) == 4:
            b = dd[-2:]
            b = [(b[0])] + [(b[1] ^ 0x10)]
            i = int.from_bytes(b, "big", signed=True)
        elif len(dd) == 5:
            b = dd[-2:]
            b = [(b[0] ^ 0x10)] + [(b[1] ^ 0x10)]
            i = int.from_bytes(b, "big", signed=True)

        i /= 2**12
        res.append(i)
    return res

# %%

res = get(sec=2)
from scipy import signal
winlen = 8
taps = [1 / winlen] * winlen
filt = signal.lfilter(taps, [1.0], res)
filt2 = signal.lfilter(taps, [1.0], filt)

from matplotlib import pyplot as plt
import numpy as np
plt.figure(figsize=(20,10))
plt.plot(res, label='X')
plt.plot(filt, label=f'X avg window {winlen}')
plt.plot(filt2, label=f'X avg window {winlen}')
# plt.plot(np.diff(filt))
plt.grid()
plt.legend()
plt.show()

# %%

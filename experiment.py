#%%
import numpy as np
# import sys
# sys.setrecursionlimit(15000)
mem = []

def func(freq):

    if freq > 20000:
        return

    if freq < 20:
        return


    if len(mem) < 12400:
        mem.append(freq)
    else:
        return


    for i in range(2,6):
        func(freq / i)
        
    # for i in range(2,6):
    #     func(freq / i)


func(440)
# %%

from matplotlib import pyplot as plt
mem = sorted(mem)
print(len(mem))
plt.figure(figsize=(10,10))
plt.plot(mem)
# %%
sorted(mem)
# %%

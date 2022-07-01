
#%%
nodes = []
def ff(f, depth=0):
    # if f > 4500:
    #     return

    # if f < 20:
    #     return

    if depth > 8:
        return

    # if len(nodes) > 1024*10:
    #     return

    if f not in nodes:
        nodes.append(f)
    else:
        return
        #print(f)
    
    for i in range(1,8):
        ff(f*2**i, depth+1)
        ff(f/2**i, depth+1)

ff(440)
print(sorted(nodes))
plt.figure(figsize=(10,10))
# plt.plot(sorted(nodes))
# plt.ylim([10, 4500])
# plt.plot(sorted(nodes))
plt.plot(np.log10(sorted(nodes)))
# plt.plot(sorted(wik_freq))


# %%
wik_freq = [
4186.009,
3951.066,
3729.310,
3520.000,
3322.438,		
3135.963,		
2959.955,		
2793.826,		
2637.020,		
2489.016,		
2349.318,		
2217.461,		
2093.005,		
1975.533,		
1864.655,		
1760.000,		
1661.219,		
1567.982,		
1479.978,		
1396.913,		
1318.510,		
1244.508,		
1174.659,		
1108.731,		
1046.502,		
987.7666,		
932.3275,		
880.0000,		
830.6094,		
783.9909,		
739.9888,		
698.4565,		
659.2551,		
622.2540,					
587.3295,					
554.3653,					
523.2511,					
493.8833,		
466.1638,					
440.0000,
415.3047,					
391.9954,					
369.9944,					
349.2282,					
329.6276,		
311.1270,					
293.6648,		
277.1826,					
261.6256,				
246.9417,					
233.0819,					
220.0000,				
207.652,					
195.997,			
184.997,				
174.614,					
164.813,					
155.563,					
146.832,		
138.591,					
130.812,	
123.470,					
116.540,					
110.0000,			
103.8262,					
97.99886,			
92.49861,					
87.30706,				
82.40689,					
77.78175,					
73.41619,				
69.29566,					
65.40639,			
61.73541,			
58.27047,					
55.00000,			
51.91309,					
48.99943,					
46.24930,				
43.65353,					
41.20344,			
38.89087,					
36.70810,					
34.64783,			
32.70320,					
30.86771,					
29.13524,					
27.5000]
# %%


f = 440
base = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])
f = 440 * 2 
pos3 = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])
f = 440 / 3
neg3 = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])

f = 440 * 5 
pos5 = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])
f = 440 / 5
neg5 = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])

f = 440 * 3 * 3
pos3pos3 = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])
f = 440 * 3 / 3
pos3neg3 = sorted([f*2**i for i in range(1, 8)] + [f]+ [f/2**i for i in range(1, 8)])

plt.figure(figsize=(10,10))

plt.plot(np.log10(sorted(base)))
plt.plot(np.log10(sorted(pos3)))
plt.plot(np.log10(sorted(neg3)))

# plt.plot(np.log10(sorted(pos5)))
# plt.plot(np.log10(sorted(neg5)))

# plt.plot(np.log10(sorted(pos3pos3)))
# plt.plot(np.log10(sorted(pos3neg3)))
# plt.plot(sorted(wik_freq))
# %%
plt.figure(figsize=(10,10))
plt.stem(np.log10(sorted(base + pos3 + neg3+ pos5 + neg5)))

# plt.plot(np.log10(base - pos3))
print(np.array(base) - pos3)
# print(pos3)

# %%
f = 440
base = [f*2**i for i in range(7, 0, -1)] + [f]+ [f*2**i for i in range(1, 8)]
f = 440 * 2 
pos3 = [f*2**i for i in range(7, 0, -1)] + [f]+ [f*2**i for i in range(1, 8)]
f = 440 / 3
neg3 = [f*2**i for i in range(7, 0, -1)] + [f]+ [f*2**i for i in range(1, 8)]

f = 440 * 5 
pos5 = [f*2**i for i in range(1, 8)] + [f]+ [f*2**i for i in range(1, 8)]
f = 440 / 5
neg5 = [f*2**i for i in range(1, 8)] + [f]+ [f*2**i for i in range(1, 8)]


plt.figure(figsize=(10,10))

plt.plot(np.log10(base))
plt.plot(np.log10(pos3))
plt.plot(np.log10(neg3))

# plt.plot(pos5)
# plt.plot(neg5)
# %%
plt.figure(figsize=(10,10))
plt.plot(sorted(base + pos3 + neg3 + pos5 + neg5))
# %%

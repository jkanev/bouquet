
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Create sum of sine waves of different frequencies
dt = 0.005
t0 = np.arange(0, 5*np.pi, dt)
f = [(abs(np.sin((0.5)*t0))),
     (abs(np.sin((1.0)*t0))),
     (abs(np.sin((2.0)*t0))),
     (abs(np.sin((4)*t0))),
     (abs(np.sin((8)*t0)))]

# Create 10 circles of different lengths
M = 41
lines = [None] * M
ax = None
fig = None
freq_start = 1.0
freq_step = 0.01
s = [[]] * M  # the circle data, zeros for now, consisting of M*N circles s[M][1..5]
t = [[]] * M  # the base to plot against, will go from 0 to 2pi, t[M]
for m in range(0, M):
    s[m] = [[]]*5
    freq = freq_start + m*freq_step  # our circle frequency
    print(freq)
    for n in range(0, 5):
        s[m][n] = np.zeros(int((2 / freq) * np.pi / dt))
    t[m] = [m for m in np.arange(0, 2 * np.pi * (1 + 2 / len(s[m][0])), 2 * np.pi / (len(s[m][0])))[0:len(s[m][0])]]

# Average over all circles - pre-calculate parts of the sum of sines
for m in range(0, M):
    for n in range(0, 5):
        # only plot if you can fill the entire circle
        for i in range(0, (len(f[n]) // len(s[m][n])) * len(s[m][n])):
            value = f[n][i] #- 0.5
            index = i % len(s[m][n])
            s[m][n][index] += value  # add to front
            s[m][n][-(index + 1)] += value  # add to back, so beginning and end match and the circle stays closed

first = True
for f0 in np.arange(0, 1000, 0.01):
    c1 = np.square(np.sin(2*f0))
    c2 = np.square(np.sin(3*f0))
    c3 = np.square(np.sin(4*f0))
    c4 = np.square(np.sin(5*f0))
    c5 = np.square(np.sin(6*f0))
    norm = c1 + c2 + c3 + c4 + c5
    print("Frequency bands: {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(c1, c2, c3, c4, c5), end='\r')

    # initialise plot if we're here for first time
    if first:
        #plt.plot(t[0], s[0][0])
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_theta_zero_location("N")
        ax.set_ylim(0.0, 5.0)
        ax.set_facecolor('k')
        fig.set_facecolor('k')
        plt.show(block=False)

    # plot curves
    for m in range(0, M):
        offset = (M-m)*0.07
        data = (c1 * s[m][0] + c2 * s[m][1] + c3 * s[m][2] + c4 * s[m][3] + c5 * s[m][4] + 1)
        data /= data.max()
        data += offset
        if first:
            try:
                [lines[m]] = ax.plot(t[m], data, color=(m/M, 0.5*m/M, 1-m/M))
            except BaseException as e:
                print("Plot exception {} for curve n={}".format(e, m))
        else:
            try:
                lines[m].set_ydata(data)
            except BaseException as e:
                print("Plot exception {} for curve n={}".format(e, m))

    plt.pause(0.001)
    first = False

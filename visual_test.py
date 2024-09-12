
import numpy as np
import matplotlib.pyplot as plt
import numpy as np

# Create sum of sine waves of different frequencies
t0 = np.arange(0, 5*np.pi, 0.01)
f1 = (abs(np.sin((3)*t0)))
f2 = (abs(np.sin((4)*t0)))
f3 = (abs(np.sin((5)*t0)))
f4 = (abs(np.sin((6)*t0)))
f5 = (abs(np.sin((7)*t0)))

# Create 10 circles of different lengths
M = 13
lines = [None] * M
ax = None
fig = None
s = [[]] * M  # the circle data, zeros for now
t = [[]] * M  # the base to plot against, will go from 0 to 2pi
for n in range(0, M):
    freq = 1.0 + n / 4.0  # our circle frequency
    print(freq)
    s[n] = np.zeros(int((2 / freq) * np.pi / 0.01))
    t[n] = [n for n in np.arange(0, 2 * np.pi * (1 + 2 / len(s[n])), 2 * np.pi / (len(s[n])))[0:len(s[n])]]

first = True
for f0 in np.arange(0, 1000, 0.01):
    c1 = np.square(np.sin(2*f0))
    c2 = np.square(np.sin(3*f0))
    c3 = np.square(np.sin(4*f0))
    c4 = np.square(np.sin(5*f0))
    c5 = np.square(np.sin(6*f0))
    f =   c1 * f1 + 0.05 \
        + c2 * f2 + 0.05 \
        + c3 * f3 + 0.05 \
        + c4 * f4 + 0.05 \
        + c5 * f5 + 0.05
    f /= c1+c2+c3+c4+c5+0.25

    print("Frequency bands: {:.2f}, {:.2f}, {:.2f}, {:.2f}, {:.2f}".format(c1, c2, c3, c4, c5), end='\r')

    for n in range(0, M):
        s[n] *= 0.0

    # Average over all circles
    for n in range(0, M):
        # only plot if you can fill the entire circle
        for i in range(0, (len(f)//len(s[n]))*len(s[n])):
            value = f[i]
            index = i % len(s[n])
            s[n][index] += value      # add to front
            s[n][-(index+1)] += value # add to back, so beginning and end match and the circle stays closed

    # initialise plot if we're here for first time
    if first:
        #plt.plot(t0, f)
        fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
        fig.set_facecolor('k')
        ax.grid(False)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_theta_zero_location("N")
        ax.set_ylim(0.0, 22.0)
        ax.set_facecolor('k')
        plt.show(block=False)

    # plot curves
    if first:
        for n in range(0, M):
            try:
                [lines[n]] = ax.plot(t[n], s[n], color=(1 - n / M, 0, n / M))
            except BaseException as e:
                print("Plot exception {} for curve n={}".format(e, n))
    else:
        for n in range(0, M):
            try:
                lines[n].set_ydata(s[n])
            except BaseException as e:
                print("Plot exception {} for curve n={}".format(e, n))

    plt.pause(0.001)
    first = False

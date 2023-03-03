#!/usr/bin/env python3
# vim:ts=4:sts=4:sw=4:expandtab
import sys
import numpy as np
import time
import matplotlib.pyplot as plt 
import time
import pulseaudio as pa

framerate = 44100

length = 1

i=0

plt.ion()
fig = plt.figure()
with pa.simple.open(direction=pa.STREAM_RECORD, format=pa.SAMPLE_S16LE, rate=framerate, channels=1) as recorder:
    while True:
        res = recorder.read(int(length * recorder.rate))
        time.sleep(3)
        fig.clear()
        a = fig.add_subplot(311)
        b = fig.add_subplot(312)
        c = fig.add_subplot(313)
        a.plot(range(len(res)), res)

        fig.canvas.draw()


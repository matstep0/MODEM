#!/usr/bin/env python3
# vim:ts=4:sts=4:sw=4:expandtab

import sys
import wave
import math
import pulseaudio as pa
import numpy as np

sample_map = {
    1 : pa.SAMPLE_U8,
    2 : pa.SAMPLE_S16LE,
    4 : pa.SAMPLE_S32LE,
}
def player (fraquency,duration):
    nchannels=1
    sampwidth=2
    #duration= float(sys.argv[2])
    framerate= 44100
    #fraquency=int(sys.argv[1])
    A=10000
    table=[]
    for i in range(0,int(duration*framerate)):
        table.append(A*math.sin(i*fraquency/framerate*2*math.pi))
    with pa.simple.open(direction=pa.STREAM_PLAYBACK, format=sample_map[sampwidth], rate=framerate, channels=nchannels) as player:    
     # frames = np.fromstring(frames, dtype=player.sample_type).astype(np.float)
        frames=table
        player.write(frames)
        player.drain()

def playerud (fraquency,duration):
    nchannels=1
    sampwidth=2
    #duration= float(sys.argv[2])
    framerate= 44100
    #fraquency=int(sys.argv[1])
    A=10000
    table=[]
    for i in range(0,int(duration*framerate)):
        table.append(A*math.sin(i*fraquency/framerate*2*math.pi))
    return table

#!/usr/bin/env python3
# vim:ts=4:sts=4:sw=4:expandtab
import sys
import wave
import math
import pulseaudio as pa
import numpy as np
import re
def freq(note):
        freq_map = {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11,}
        note = note.upper()
        letter = re.sub(r'^[^A-G]*([A-G]).*$', r'\1', note) or 'A'
        num = int(re.sub(r'^[^0-9]*([0-9]).*$', r'\1', note) or 4)
        sharp = 1 if '#' in note or 'S' in note else 0
        freq = 440 * (2 ** (1/12)) ** (12*(num-4) + freq_map[letter] - freq_map['A'] + sharp)
        return freq

sample_map = {
    1 : pa.SAMPLE_U8,
    2 : pa.SAMPLE_S16LE,
    4 : pa.SAMPLE_S32LE,
}

nchannels=1
sampwidth=2
framerate= 44100
A=10000
table=[]
sys.stdin.read

while(True):
    line=(sys.stdin.readline()).split()
    if(line==[]):
        break   
    frequency=int(freq(line[0]))
    duration=float(line[1])
#    print(frequency,duration)
    for i in range(0,int(duration*framerate)):
        table.append(A*math.sin(i*frequency/framerate*2*math.pi))

with pa.simple.open(direction=pa.STREAM_PLAYBACK, format=sample_map[sampwidth], rate=framerate, channels=nchannels) as player:    
     # frames = np.fromstring(frames, dtype=player.sample_type).astype(np.float)
    frames=table
    player.write(frames)
    player.drain()

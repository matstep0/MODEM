#!/usr/bin/env python3
# vim:ts=4:sts=4:sw=4:expandtab
import sys
import numpy as np
import time
import matplotlib.pyplot as plt 
import pulseaudio as pa
framerate = 44100


def sluchaj(length): #slucha przez leggth czasu i zwraca wysluchana tablice
    with pa.simple.open(direction=pa.STREAM_RECORD, format=pa.SAMPLE_S16LE, rate=framerate, channels=1) as recorder:
        return recorder.read(int(length * recorder.rate))
        

def dominujaca(res,length): #zwaraca czestotwilosc dominujaca w danym kawalku tablicy
    a=np.fft.rfft(res)
    maxim=0
    for ind in range(len(a)):
        if abs(a[ind])> abs(a[maxim]):
            maxim=ind
    return maxim/length

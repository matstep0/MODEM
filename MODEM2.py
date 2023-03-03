#!/usr/bin/env python3
# vim:ts=4:sts=4:sw=4:expandtab
#import player.py #generuje frequecy arg1 of duration arg2
import komunikat as kom #napisz czytaj napis
#import sluchaj as slu #slucha dominujaca
import udawanesluchaj as udslu
import sys
import numpy as np
bit_time=1 #czas przesylania jednego bitu
frequency_zero=440 #czestotliwosc zera
frequency_one=880 #czestotliwosc jedynki
frac=0.2 #mowi mi co jaki ulamek czasu sprawdzac ramke
framerate=44100
tab=udslu.sluchaj(8*bit_time)
print("dlugosc",len(tab))
#for i in range(0,int(len(tab)/4)):
 #   print(tab[i]," " ,end='')
time=int(1/frac*8*bit_time)
while(time>0):
    for i in range(0,8):
        print(i)
        print("lenght",len(tab[int(i*bit_time*framerate):int((i+1)*bit_time*framerate)]))
        print(udslu.dominujaca(tab[int(i*bit_time*framerate):int((i+1)*bit_time*framerate)],bit_time),end='')
    print()
    x=udslu.sluchaj(bit_time*frac)
    tab=tab[int(bit_time*frac*framerate):]
    tab=np.append(tab,x)
    time=time-1

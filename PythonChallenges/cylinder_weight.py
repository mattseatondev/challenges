
import math

def weight(r, h):
    area = math.pi * r**2
    vol = area * h
    vol = vol/10
    print(vol)

weight(4, 10)
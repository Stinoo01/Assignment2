#import logarithm
import math
from math import log

#opening file with data 
f = open('dati.txt', 'r').readlines()

def calcProb(gc, seq):
    #probbility of GC 
    gchalf = gc/2.0
    athalf = (1.0-gc)/2.0

    #multiply probability for each letter in the sequence
    prob = 1.0
    #seq = sequence studied 
    for i in range(0, len(seq)):
        if seq[i] == 'A' or seq[i] == 'T':
            prob *= athalf
        elif seq[i] == 'G' or seq[i] == 'C':
            prob *= gchalf
    
    # return the probability value
    return prob

#take log of calcProb
#use 3 decimla points 
gc = f[1].split( )
final_ = []
for x in gc:
    final = calcProb(float(x), f[0])
    final_.append("%.3f" % math.log10(final))

#print result spaced
print(" ".join(final_))

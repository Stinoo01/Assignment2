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
gcCons = f[1].split( )
finalProbs = []
for i in gcCons:
    rawProb = calcProb(float(i), f[0])
    finalProbs.append("%.3f" % math.log10(rawProb))

#print result spaced
print(" ".join(finalProbs))
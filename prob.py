#importing 
import math
from math import log

#opening file with data 
f = open('dati.txt', 'r').readlines()

def calculus(gc, seq):
    #probbility of GC 
    gchalf = gc/2
    athalf = (1-gc)/2

    #multiply probability for each letter in the sequence
    prob = 1
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

result = []
for x in gc:
    final = calculus(float(x), f[0])
    result.append("%.3f" % math.log10(final)) #3 decimal points

#print result with a space
print(" ".join(result))

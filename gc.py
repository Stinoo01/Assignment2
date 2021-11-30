#GC content of DNA sequence 
def counterGC(sequence):

    #count G and C
    def count(base):
        if base == "G" or base == "C":
            return 1
        else:
            return 0

    #sum G and C
    GC = sum(map(count, sequence))

    #doing percentage
    return GC * 100.0 / len(sequence)

#use dictionary with {ID: sequence}
def fastaformat(fasta):
    #current ID
    seq = None
    #creating dictionary 
    output = {}
    #creating fasta and update dictionary
    for x in fasta:
        if x.startswith(">"):
            seq = x.replace(">","")
            output[seq] = ""
        else:
            output[seq] += x
    # Return fasta dictionary
    return output

#open file 
f = open("dati.txt","r").readlines()

#remove end of line 
f = list(map(lambda x: x.replace("\n",""), f))

#pass to the dictionary
fasta_dict = fastaformat(f)

#calculate gc
gc = list(map(lambda x: (x[0], counterGC(x[1])), fasta_dict.items()))

#sort by gc content
gc = sorted(gc, key=lambda x: -x[1])

#retinging highest value 
print("{0}\n{1:6f}".format(gc[0][0], gc[0][1]))

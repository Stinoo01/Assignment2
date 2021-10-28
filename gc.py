#GC content of DNA sequence 
def computeGC(sequence):

    #count G and C
    def _helper(base):
        if base == "G" or base == "C":
            return 1
        else:
            return 0

    #sum G and C
    GC_array = sum(map(_helper, sequence))

    #doing percentage
    return GC_array * 100.0 / len(sequence)

#use dictionary with {ID: sequence}
def fastaDict(fasta):
    #current ID
    currentSeq = None
    #creating dictionary 
    output = {}
    #creating fasta and update dictionary
    for line in fasta:
        if line.startswith(">"):
            currentSeq = line.replace(">","")
            output[currentSeq] = ""
        else:
            output[currentSeq] += line
    # Return fasta dictionary
    return output

#running code by defining fila sets 
if __name__ == "__main__":
    #read file
    fasta_input = open("dati.txt","r").readlines()

    #remove end of lines
    fasta_input = list(map(lambda x: x.replace("\n",""), fasta_input))

    #pass to the dictionary
    fasta_dict = fastaDict(fasta_input)

    #calculate GC 
    gc_content = list(map(lambda x: (x[0], computeGC(x[1])), fasta_dict.items()))

    #sort by GC content
    gc_content = sorted(gc_content, key=lambda x: -x[1])
    #retinging highest value 
    print("{0}\n{1:6f}".format(gc_content[0][0], gc_content[0][1]))
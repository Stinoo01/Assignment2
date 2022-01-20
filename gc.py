from Bio import SeqIO

#open file 
f = open('dati.txt', 'r')

for sequence in SeqIO.parse(f, 'fasta'):
    #sequence id = rosalind 
    ID = sequence.id
    GC = 0 #storge GC
    tot = 0 #len sequence 
    #check if base is G or C and add to count 
    for base in sequence.seq:
        #add count for len sequence 
        tot += 1
        #add if equal to base 
        if base == 'G' or base == 'C':
            GC += 1
        else:
            GC += 0
    
    #percentage 
    percentage = GC*100 /tot

print(ID) #risalind 
print(percentage) #percentage 
f.close() #close file 

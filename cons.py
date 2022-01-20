#open file 
f = open('dati.txt', 'r')

#creating dictionary
dictionary = {}
n = 0
"""
I solved this problem before the FAsta format from biopython
so in order to handle fasta i searched and found this way that works
"""
for line in f:
    if '>' in line:
        id_seq = line.strip()[1:]
        dictionary[id_seq] = []
    else:
        stripped = list(line.strip())
        dictionary[id_seq].extend(stripped)
        
n = len(list(dictionary.values())[0])

#bases
bases = {"A" : [],
         "C" : [],
         "G" : [],
         "T" : []}

#count for each base 
for x in range(n):
        bases['A'].append(0) 
        bases['C'].append(0)                 
        bases['G'].append(0)
        bases['T'].append(0)

for x in range(n):
    for key in dictionary.keys():
        bases[dictionary[key][x]][x]+=1

#store firs output 
list_ = []

for x in range(n):
    max_freq = 0
    max_base = 'A'
    for key in bases.keys():
        if max_freq <= bases[key][x]:
            max_freq = bases[key][x]
            max_base = key
    list_.append(max_base)
    
#output
#first output
print("".join(list_))

#second output
for key in bases.keys():
    #print bases plus :
    print(key + ":", end='') #to be on the same line of the other output
    for x in range (n):
         print(" ", bases[key][x], end="")
    print()

#close file 
f.close()

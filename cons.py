#open file 
f = open('dati.txt', 'r')

#creating dictionary
dictionary = {}
n = 0

for line in f:
    if '>' in line:
        id_seq = line.strip()[1:]
        dictionary[id_seq] = []
    else:
        stripped = list(line.strip())
        dictionary[id_seq].extend(stripped)
        
n = len(list(dictionary.values())[0])

bases = {"A" : [],
         "C" : [],
         "G" : [],
         "T" : []}

for x in range(n):
        bases['A'].append(0) 
        bases['C'].append(0)                 
        bases['G'].append(0)
        bases['T'].append(0)

for x in range(n):
    for key in dictionary.keys():
        bases[dictionary[key][x]][x]+=1
        
list_ = []

for x in range(n):
    max_freq = 0
    max_base = 'A'
    for key in bases.keys():
        if max_freq <= bases[key][x]:
            max_freq = bases[key][x]
            max_base = key
    list_.append(max_base)
    
print("".join(list_))

for key in bases.keys():
    print("%s:" % key, end="")
    for x in range (n):
         print(" ", bases[key][x], end="")
    print()

#close file 
f.close()
inp = 'TAGCCCCTCCATTCCCCCGCCTCCAGAATAACTGAGCCCCACAGGCGGGATACAGCTCTCCCGTACCTCCCATAAGTAGATTTGTGGACATTGGGATAATAGTCCTCATGACTGCCTGAAACGCGTCCCTAAAGCAGTAGAACAGGGAACCATAGCAGTAGATGAGTAACATCTGCCAAAATACGCAGGGGGGGCGCGTTACCATATCGCGTTAAGCCATACGAACTTCGATAGCAGATTGCAGTACCGCTAAGATCCTCCAATTAGGGTGATGTTAAAGGTTGGGATCGGTGCCCTCGTGCGGCACTGACTCGTTCGGTGGCAAGACATGCGTGGGAGGAAAAGATGCGTAGGTACGCAAAACTGGGCCCGAGGCTTCACAGGGGATTGTTAAGGATGGTAAACGTAGACCAATCACTCATGCCTCCCTGTGCAATGATTTTCGTTTTGAACACACCAACAGCCCTCTGATCTGCCGAAGATGTGCGATATCACCACTCCTGTGATTCCGGACGTTTGCAAGGTCATGTATTTTATCATTCAACTTTGTCGGTGCTTGCCGTCAATCGACCTTTGCGAAAGTTCATTGCAACCGCATGATTTATTGTGACTGCCCCTACACTATTCAGCTCAGCCTCTCGCGAGGTACCCAGTTCTACCAACGCCCAGAATGCGATTCAGGAAGGTACTCAAGGATTTTGGGCGTTGGACATAGCCGCTCAGTATGAAGCCACGCCGTAACGGTTATGGGGTAGGAGTGGGTGTCTCGAGGGATAAGCCCAATTCCCGTCCTTCAAAAGCAGTATGCCAAACGGTGGTCCCGGAAGGAGAATTTTACCGAGTGCCCTACACGCTCAGTCGCGGACGGATTTTCTCTAACCATCGTGCTCTCTCTCGCGCA'
#setting counters 
a= 0
g = 0
t = 0
c = 0
#checking each letter and add respective counter
for x in inp:
    if x == 'A':
        a = a + 1
    if x == 'T':
        t = t + 1
    if x == 'C':
        c = c + 1
    if x == 'G':
        g = g + 1
#unifing all results in one string
out = str(a) + ' ' + str(c) + ' ' + str(g) + ' ' + str(t)
#print result 
print(out)
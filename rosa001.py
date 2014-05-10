f = open('rosalind_dna_001.txt')
seq = f.read().strip()

A, C, G, T = 0, 0, 0, 0
for base in seq:
    A += 1 if base == 'A' else 0
    C += 1 if base == 'C' else 0
    G += 1 if base == 'G' else 0
    T += 1 if base == 'T' else 0
print A, C, G, T

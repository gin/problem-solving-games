"""Counting Point Mutations"""

#f_in = open('rna.txt', 'r')
#f_out = open('rna_soln.txt', 'w')
f_in = open('007rosalind_hamm.txt', 'r')
f_out = open('007rosalind_soln.txt', 'w')

seq1 = f_in.readline().strip()
seq2 = f_in.readline().strip()

def hamming_distance(seq1, seq2):
    if len(seq1) != len(seq2): return "Seq lengths are different"

    count_difference = 0
    for idx,base in enumerate(seq1):
        if base != seq2[idx]: count_difference += 1
    return str(count_difference)

print hamming_distance(seq1, seq2)
#f_out.write(hamming_distance(seq1, seq2))

#===============================================================================
# Other methods
#===============================================================================
def method1(seq1, seq2):
    return sum([a!=b for a, b in zip(seq1, seq2)])

import itertools
def method2(seq1, seq2):
    """Saves memory due to iterator compared to method1"""
    return sum([a!=b for a, b in itertools.izip(seq1, seq2)])

def method3(seq1, seq2):
    return sum(map(lambda x, y: 0 if x == y else 1, seq1, seq2))

print method1(seq1, seq2)
print method2(seq1, seq2)
print method3(seq1, seq2)

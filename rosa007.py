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
f_out.write(hamming_distance(seq1, seq2))

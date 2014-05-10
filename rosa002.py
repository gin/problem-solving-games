f_in = open('002rosalind_rna.txt', 'r')
f_out = open('rosalind_soln.txt', 'w')
seq = f_in.read().strip()
transcribed_seq = ''

for base in seq:
    transcribed_seq += 'U' if base == 'T' else base

f_out.write(transcribed_seq)

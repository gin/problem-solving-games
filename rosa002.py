f_in = open('rosalind_rna_002.txt', 'r')
f_out = open('rosalind_rna_002_soln.txt', 'w')
seq = f_in.read().strip()
transcribed_seq = ''

for base in seq:
    #transcribed_seq += 'U' if base == 'T' else transcribed_seq.join(base)
    # or
    if base == 'T':
        transcribed_seq += 'U'
    else:
        transcribed_seq += base

f_out.write(transcribed_seq)

f_in = open('003rosalind_revc.txt', 'r')
f_out = open('rosalind_soln.txt', 'w')
seq = f_in.read().strip()

seq = seq[::-1]  # Reverse
rev_complement_seq = ''

# Complement
for base in seq:
    if base == 'A': rev_complement_seq += 'T'
    if base == 'C': rev_complement_seq += 'G'
    if base == 'G': rev_complement_seq += 'C'
    if base == 'T': rev_complement_seq += 'A'

f_out.write(rev_complement_seq)

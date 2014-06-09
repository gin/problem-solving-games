#f_in = open('rna.txt', 'r')
#f_out = open('rna_soln.txt', 'w')
f_in = open('006rosalind_prot.txt', 'r')
f_out = open('006rosalind_soln.txt', 'w')

seq = ''
current_line = f_in.readline().strip()

with f_in:
    while True:
        if not current_line: break
        seq += current_line
        current_line = f_in.readline().strip()

def amino_acid(seq):
    aa = ''
    rna_dict = {'UUU':'F', 'CUU':'L', 'AUU':'I', 'GUU':'V',
                'UUC':'F', 'CUC':'L', 'AUC':'I', 'GUC':'V',
                'UUA':'L', 'CUA':'L', 'AUA':'I', 'GUA':'V',
                'UUG':'L', 'CUG':'L', 'AUG':'M', 'GUG':'V',
                'UCU':'S', 'CCU':'P', 'ACU':'T', 'GCU':'A',
                'UCC':'S', 'CCC':'P', 'ACC':'T', 'GCC':'A',
                'UCA':'S', 'CCA':'P', 'ACA':'T', 'GCA':'A',
                'UCG':'S', 'CCG':'P', 'ACG':'T', 'GCG':'A',
                'UAU':'Y', 'CAU':'H', 'AAU':'N', 'GAU':'D',
                'UAC':'Y', 'CAC':'H', 'AAC':'N', 'GAC':'D',
                'UAA':'x', 'CAA':'Q', 'AAA':'K', 'GAA':'E',
                'UAG':'x', 'CAG':'Q', 'AAG':'K', 'GAG':'E',
                'UGU':'C', 'CGU':'R', 'AGU':'S', 'GGU':'G',
                'UGC':'C', 'CGC':'R', 'AGC':'S', 'GGC':'G',
                'UGA':'x', 'CGA':'R', 'AGA':'R', 'GGA':'G',
                'UGG':'W', 'CGG':'R', 'AGG':'R', 'GGG':'G'}
    for i in xrange(3, len(seq), 3):
        nuc = seq[i-3:i]
        aa += rna_dict[nuc]
    return aa

print amino_acid(seq)
f_out.write(amino_acid(seq))

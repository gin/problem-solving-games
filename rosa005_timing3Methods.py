# To Do:
# copy and paste code from soln
# test timer on other's methods
import operator     # For iteritems() on dict; Use list to avoid using package

#f_in = open('fasta.txt', 'r')
f_in = open('005rosalind_gc.txt', 'r')
f_out = open('005rosalind_soln.txt', 'w')

def GC_content(seq):
    seq_length = len(seq)
    GC_length = 0.0
    for base in seq:
        if base == 'G' or base == 'C': GC_length += 1
    return (GC_length / seq_length) * 100

GC_dict = {}
seq = ''
current_line = f_in.readline().strip()
print 'begin'
while current_line != '':   # Until end-of-file
    if current_line[0] == '>':
        seq = ''
        gene_id = current_line[1:]
#        print gene_id
        current_line = f_in.readline().strip()
    if current_line[0] != '>':
        while current_line != '' and current_line[0] != '>':
            seq += current_line
            current_line = f_in.readline().strip()
#        print('seq:{}').format(seq)
    GC_dict[gene_id] = GC_content(seq)
print GC_dict
print 'done creating dict'

highest_GC = max(GC_dict.iteritems(), key=operator.itemgetter(1))
print highest_GC[0] # Gene name
print highest_GC[1] # % GC content

f_out.write(str(highest_GC[0]) + '\n')
f_out.write(str(highest_GC[1]))

def method1(seq):
    pass

def method2(seq):
    from Bio import SeqIO
    from Bio.SeqUtils import GC
    GCcont = 0
    GCname = ""
    file = open("rosalind_GC.txt", "r")
    for record in SeqIO.parse(file, "fasta"):
        if GCcont < GC(record.seq):
            GCcont = GC(record.seq)
            GCname = record.id
    print GCname
    print round(GCcont,2), "%"

def method3(seq):
    from string import maketrans
    rev_complement_seq = seq[::-1]  # Init with reversed seq
    translation_table = maketrans('ACTG', 'TGAC')
    rev_complement_seq = rev_complement_seq.translate(translation_table)


if __name__ == '__main__':
    import timeit
    print timeit.repeat("method1('ATGCATGCATGC')", "from __main__ import method1", number=100000)
    print timeit.repeat("method2('ATGCATGCATGC')", "from __main__ import method2", number=100000)
    print timeit.repeat("method3('ATGCATGCATGC')", "from __main__ import method3", number=100000)

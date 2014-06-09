def method1(seq):
    seq = seq[::-1]  # Reverse
    rev_complement_seq = ''

    # Complement
    for base in seq:
        if base == 'A': rev_complement_seq += 'T'
        if base == 'C': rev_complement_seq += 'G'
        if base == 'G': rev_complement_seq += 'C'
        if base == 'T': rev_complement_seq += 'A'

def method2(seq):
    """Fastest method."""
    rev_complement_seq = ''
    mapping = {
            'A':'T', 
            'C':'G',
            'G':'C',
            'T':'A'
            }
    for base in seq:
        rev_complement_seq = mapping[base] + rev_complement_seq

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

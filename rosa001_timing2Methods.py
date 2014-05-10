def method1(seq):
    # 4N
    A, C, G, T = 0, 0, 0, 0
    for base in seq:
        A += 1 if base == 'A' else 0
        C += 1 if base == 'C' else 0
        G += 1 if base == 'G' else 0
        T += 1 if base == 'T' else 0
#    print A, C, G, T

def method2(seq):
    # N
    freq = {'A':0, 'C':0, 'G':0, 'T':0}
    for base in seq:
        freq[base] += 1
#    print freq['A'], freq['C'], freq['G'], freq['T']

if __name__ == '__main__':
    import timeit
    print timeit.repeat("method1('ATGCATGCATGC')", "from __main__ import method1", number=100000)
    print timeit.repeat("method2('ATGCATGCATGC')", "from __main__ import method2", number=100000)

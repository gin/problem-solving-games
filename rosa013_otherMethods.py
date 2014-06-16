"""Calculating Protein Mass"""

f_in = open('013rosalind_prtm.txt', 'r')
f_out = open('013rosalind_soln.txt', 'w')

seq = ''
current_line = f_in.readline().strip()

with f_in:
    while True:
        if not current_line: break
        seq += current_line
        current_line = f_in.readline().strip()

def monoisotropic_mass(seq):
    total_weight = 0
    mass_table = {'A':71.03711  ,
                  'C':103.00919 ,
                  'D':115.02694 ,
                  'E':129.04259 ,
                  'F':147.06841 ,
                  'G':57.02146  ,
                  'H':137.05891 ,
                  'I':113.08406 ,
                  'K':128.09496 ,
                  'L':113.08406 ,
                  'M':131.04049 ,
                  'N':114.04293 ,
                  'P':97.05276  ,
                  'Q':128.05858 ,
                  'R':156.10111 ,
                  'S':87.03203  ,
                  'T':101.04768 ,
                  'V':99.06841  ,
                  'W':186.07931 ,
                  'Y':163.06333 }

    for aa in seq:
        total_weight += mass_table[aa]

    return str(total_weight)

print monoisotropic_mass(seq)
f_out.write(monoisotropic_mass(seq))

#===============================================================================
# Other methods
#===============================================================================
def method1(seq):
    mmt = """
    A   71.03711
    C   103.00919
    D   115.02694
    E   129.04259
    F   147.06841
    G   57.02146
    H   137.05891
    I   113.08406
    K   128.09496
    L   113.08406
    M   131.04049
    N   114.04293
    P   97.05276
    Q   128.05858
    R   156.10111
    S   87.03203
    T   101.04768
    V   99.06841
    W   186.07931
    Y   163.06333
    """.split()
    mmt = dict(zip(mmt[::2],map(float,mmt[1::2])))

    s = seq
    print "%.2f"%(sum(map(lambda x:mmt[x],s)))

print method1(seq)

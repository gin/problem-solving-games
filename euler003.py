big_prime = 600851475143
for i in xrange(big_prime):
    # Find prime and check mod prime == 0
    # Use Fermat's little theorem, check for pseudoprime
    # or use AKS test (no pseudoprimes but runs slower)
    i += 1
    if ((2**i - 2) % i == 0):   # Fermat's little theorem
    #if ( ((2-1)**i - (2**i - 1)) % i == 0 ):    # AKS test
        if (big_prime%i == 0):
            print i
# Manually entered 6857, and got it right before program completion

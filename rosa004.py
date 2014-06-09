## timer test recursion vs dp vs for-loop
f_in = open('004rosalind_fib.txt', 'r')
f_out = open('004rosalind_soln.txt', 'w')

setting = f_in.read().split()  # split() :: space-delimited String -> [String]
n = int(setting[0])
k = int(setting[1])
n, k = 5,3
print n, k
print "\n"

def rabbit(n, k):
    if k == 0: return 1
    if n == 0: return 1 # Base case with init of 1 pair of rabbits
    if n == 1: return 1 # Assume init pair of rabbits is not breeding generation
    if n > 1: return rabbit(n-1, k) + k * rabbit(n-2, k)

def r2(n, k):
    a, b = 1, 1
    for i in range (2, n):
        a, b = b, k*a + b
    return b

cache = {}
def r3(n, k, cache):
    if n == 2 or n == 1:
        return 1
    if (n, k) not in cache:
        cashe[(n, k)] = r3(n-1, k, cashe) + k * r3(n-2, k, cashe)
    print cache
    return cashe[(n, k)]

def soln(n, k=1):
    a, b = 1, 0
    for i in range(n):
        a, b = a+k*b, a
        print a, b
    return b    # This takes n-1

def soln_recursion(n, k=1):
    if n == 1: return 1
    if n == 2: return 1
    return soln_recursion(n-1, k) + soln_recursion(n-2, k)

memo = {}   # Dictionary for memorization
def soln_dp(n, k=1):
    args = (n, k)
    if args in memo: return memo[args]  # Result computed previously

    if n == 1:
        ans = 1
    elif n == 2:
        ans = 1
    else:
        ans = soln_dp(n-1, k) + k * soln_dp(n-2, k)

    memo[args] = ans    # Record result
    print memo
    return ans

#print rabbit(n-1, k)
#print r2(n, k)
##print r3(n, k, cashe)
#print soln(n, k)
#print soln_recursion(n, k)
print soln_dp(n, k)

# parent, f1 = 1, 1   # month 1
# for i in xrange(n):
#     parent, f1 = f1, k * parent + f1  #reversed
#     print parent, f1
# print f1

#f_out.write(str(rabbit(n-1, k)))

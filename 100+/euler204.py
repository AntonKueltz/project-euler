from euler_util import gen_primes_to

typ, n, = 100, 10**9
count = 0

def gen_hamming_num(i, ps, val):
    global count
    count += 1
    
    for ii, p in enumerate(ps):
        newval = val*p
        if newval <= n:
            gen_hamming_num(ii, ps[ii:], newval)

def euler204():
    ps = gen_primes_to(typ)
    gen_hamming_num(0, ps, 1)
    return count

if __name__ == "__main__":
    print euler204()

import euler_util

def perm(n, m):
    return sorted(str(n)) == sorted(str(m))

def split_ps(ps):
    for i, p in enumerate(ps):
        if p > 10**(3.5): break
    return (ps[:i], ps[i:])

def euler70():
    limit = (10**4)
    m, n = 1000.0, 0
    ns = []

    # looking for a composite number with 2 large prime factors ~sqrt(10^7)
    ps = euler_util.gen_primes_to(limit)
    fac1, fac2 = split_ps(ps)
    
    for f1 in fac1[::-1]:
        for f2 in fac2:
            c = f1 * f2
            
            if c > 10**7: break
            
            t = (f1-1)*(f2-1) # fast totient
            if not perm(t, c): continue
            
            ratio = f1*f2 / float(t)
            if ratio < m: m, n = ratio, f1*f2

    return n

if __name__ == "__main__":
    print euler70()

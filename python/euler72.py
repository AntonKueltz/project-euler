from euler_util import gen_primes_to

def gen_totients(n):
    ps = gen_primes_to(n)
    ts = range(n)
    
    for p in ps:
        for idx in range(p, n, p): ts[idx] *= (1.0 - 1.0 / p)

    return ts

def euler72():
    ts = gen_totients(10**6 + 1)
    els = 1

    for d in range(3, len(ts)): 
        els += int(ts[d])

    return els

if __name__ == "__main__":
    print euler72()

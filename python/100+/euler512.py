from euler_util import gen_primes_to, timed


@timed
def euler512():
    n = 5 * 10**8
    ps = gen_primes_to(n+1)
    ts = range(n+1)
    s, last = 0, 3

    for p in ps:
        for r in xrange(p, n, p):
            ts[r] = int(ts[r] * (1.0 - 1.0 / p))
        for i in xrange(last, p, 2):
            s += ts[i]
        last = p

    for i in xrange(last, n+1, 2):
        s += ts[i]

    return s

if __name__ == '__main__':
    print euler512()

from euler_util import gen_primes_to, timed

lowest = 10**100


def gen_hcn(ps, n, i, divs):
    global lowest
    if (ps == [] or i == 0):
        if divs >= 8000000 and n < lowest:
            lowest = n
        return

    for a in range(i+1):
        n_ = n * (ps[0] ** a)
        divs_ = divs if a == 0 else divs * (2 * a + 1)
        gen_hcn(ps[1:], n_, a, divs_)


@timed
def euler110():
    ps = gen_primes_to(50)
    gen_hcn(ps, 1, 8, 1)
    return lowest

if __name__ == '__main__':
    print euler110()

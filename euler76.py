def gen_pents(limit):
    pents = []
    gen = lambda x: x * (3*x - 1) / 2
    pent, n = gen(1), 1

    while pent <= limit:
        pents.append(pent)
        if n > 0: n *= -1
        else: n = abs(n) + 1
        pent = gen(n)

    return pents

def euler76():
    # this is an integer partitions problem
    ps = [0]*101
    ps[0], ps[1], n = 1, 1, 1
    pents = gen_pents(100)

    while n < 100:
        n += 1
        
        for i, p in enumerate(pents):
            if p > n: break
            if i % 4 < 2: ps[n] += ps[n-p]
            else: ps[n] -= ps[n-p]

    return ps[100]-1 # only sum of integers so not 100 itself

if __name__ == "__main__":
    print euler76()

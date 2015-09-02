from bisect import bisect_left

def find(seq, el):
    i = bisect_left(seq, el)
    if i != len(seq) and seq[i] == el: return True
    else: return False

def gen_sequence(func):
    n, seq = 1, []
    
    val = func(n)
    while val < 10000:
        if val >= 1000: seq.append(val)
        
        n += 1
        val = func(n)

    return seq

def find_six_chain(seqs):
    flat_seq = reduce(lambda x,y: x+y, seqs)
    chains = []

    # There's gotta be a better way
    for v1 in seqs[-1]:
        for v2 in flat_seq:
            if v2 / 100 != v1 % 100: continue
            for v3 in flat_seq:
                if v3 / 100 != v2 % 100: continue
                for v4 in flat_seq:
                    if v4 / 100 != v3 % 100: continue
                    for v5 in flat_seq:
                        if v5 / 100 != v4 % 100: continue
                        for v6 in flat_seq:
                            if v6 / 100 != v5 % 100: continue
                            elif v1 / 100 == v6 % 100:
                                chains.append([v1,v2,v3,v4,v5,v6])

    return chains

def validate_chain(seqs, chain):
    s = sum(chain)
    found = []

    for el in chain:
        for i, seq in enumerate(seqs):
            if find(seq, el): found.append(i)

    if set(found) == set(range(len(seqs))): return True, s
    else: return False, 0

def euler61():
    tri = gen_sequence(lambda n: n*(n+1)/2)
    sqr = gen_sequence(lambda n: n*n)
    pnt = gen_sequence(lambda n: n*(3*n-1)/2)
    hxg = gen_sequence(lambda n: n*(2*n-1))
    hpt = gen_sequence(lambda n: n*(5*n-3)/2)
    otg = gen_sequence(lambda n: n*(3*n-2))
    seqs = [tri, sqr, pnt, hxg, hpt, otg]

    chains = find_six_chain(seqs)
    
    for chain in chains:
        valid, s = validate_chain(seqs, chain)
        if valid: return s
            
    return 0

if __name__ == "__main__":
    print euler61()

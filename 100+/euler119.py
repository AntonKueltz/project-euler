def gen_powers(n):
    candidates = []
    for base in range(2, n):
        for exp in range(1, n):
            if base**exp > 10: candidates.append((base**exp, base))
    return sorted(candidates)

def dig_sum(n):
    s = 0
    while n > 0:
        s += n % 10
        n /= 10
    return s

def euler119():
    cands = gen_powers(100)
    target = 30
    count = 0
    
    for cand in cands:
        if dig_sum(cand[0]) == cand[1]: count += 1
        if count == target: return cand[0]

if __name__ == "__main__":
    print euler119()

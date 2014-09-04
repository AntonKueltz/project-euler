import util

primes = util.gen_primes_to(9000)

def is_prime(n):
    for p in primes:
        if p > n**0.5: return True
        if n % p == 0: return False
    return True

def build_cands(p):
    cands = []
    start = primes.index(p)+1

    for i in range(start, len(primes)):
        p_ = primes[i]
        if is_prime(int(str(p)+str(p_))) and is_prime(int(str(p_)+str(p))):
            cands.append(p_)

    return cands

def find_pairs(lists):
    target = 5
    sets = []

    # FUGLY CODE AHEAD
    for lst1 in lists:
        if len(lst1) < target: continue
        for el2 in lst1[1:]:
            lst2 = lists[primes.index(el2)]
            if len(lst2) < target - 1: continue
            for el3 in lst2[1:]:
                if el3 not in lst1: continue
                lst3 = lists[primes.index(el3)]
                if len(lst3) < target - 2: continue
                for el4 in lst3[1:]:
                    if el4 not in lst1 or el4 not in lst2: continue
                    lst4 = lists[primes.index(el4)]
                    if len(lst4) < target - 3: continue
                    for el5 in lst4[1:]:
                        if el5 in lst1 and el5 in lst2 and el5 in lst3:
                            sets.append([lst1[0], el2, el3, el4, el5])

    return sets

def euler60():
    lists = []
    for p in primes: lists.append([p])
    
    for idx, p in enumerate(primes):
        lists[idx] += build_cands(p)

    sets = find_pairs(lists)
    sums = map(sum, sets)

    return min(sums)

if __name__ == "__main__":
    print euler60()

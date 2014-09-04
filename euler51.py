from bisect import bisect_left

def binary_search(lst, find, low, high):
    pos = bisect_left(lst, find, low, high)
    return (pos if pos != high and lst[pos] == find else -1)

def gen_primes_to(n):
    primes = [2]
    cand = 3
    
    while cand < n:
        idx = 0
        is_prime = True

        while primes[idx] <= cand**0.5:
            if cand % primes[idx] == 0:
                is_prime = False
                break

            idx += 1

        if is_prime: primes.append(cand)

        cand += 2

    return primes

def family_size(p, primes):
    idx = primes.index(p)+1
    search_list = primes[idx+1:]
    size0, size1, size2 = 1, 1, 1
    p_s = str(p)

    if "0" in str(p):
        for i in "123456789":
            pos = binary_search(
                search_list, int(p_s.replace("0", i)), 0, len(search_list))
            if pos != -1: size0 += 1

    if "1" in str(p):
        for i in "23456789":
            pos = binary_search(
                search_list, int(p_s.replace("1", i)), 0, len(search_list))
            if pos != -1: size1 += 1

    if "2" in str(p):
        for i in "3456789":
            pos = binary_search(
                search_list, int(p_s.replace("2", i)), 0, len(search_list))
            if pos != -1: size2 += 1

    return max([size0, size1, size2])

def euler51():
    primes = gen_primes_to(10**6)

    for p in primes:
        if family_size(p, primes) == 8:
            return p

    return -1

if __name__ == "__main__":
    print euler51()

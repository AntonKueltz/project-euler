import euler_util

def carry_add(carries, idx, value):
    carries[idx] += value
    if carries[idx] >= 10:
        carries[idx] %= 10
        if idx+1 < len(carries): carries[idx+1] += 1

def S(p1, p2):
    digits1, digits2 = len(str(p1)), len(str(p2))
    carries, factor = [0]*(digits1+2), 0
    first_dig = p2 % 10

    for place in range(1, digits1+1):
        target = (p1 % 10**place) / 10**(place-1)

        fac = 0
        while (fac*first_dig + carries[place-1]) % 10 != target:
            fac += 1

        if (fac*first_dig % 10) + carries[place-1] >= 10: carries[place] += 1

        factor += 10**(place-1) * fac

        for i in range(1, digits1+1 - place):
            carry = (((fac*p2) % 10**(i+1)) / 10**(i))
            carry_add(carries, place+i-1, carry % 10)
            if i < digits1:
                carry_add(carries, place+i, carry / 10)

    assert(factor*p2 % 10**digits1 == p1)
    return factor*p2

def euler134():
    acc = 0
    primes = euler_util.gen_primes_to(1000004)
    primes = primes[primes.index(5):]
    
    for i, p1 in enumerate(primes[:-1]):
        acc += S(p1, primes[i+1])   
    return acc

if __name__ == "__main__":
    print euler134()

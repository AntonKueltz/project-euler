from itertools import permutations
from itertools import combinations

def is_prime(n):
    if sum([int(i) for i in str(n)]) % 3 == 0: return False
    for i in range(2, int(n**0.5)):
        if n % i == 0: return False
    return True

def replace(digit, other_digits, i, order):
    replaced = []
    
    indices = combinations(range(order), i)

    for idx in indices:
        replace_digits = combinations(i*other_digits, i)
        for replace in replace_digits:
            base = [digit]*order
            for j in range(i):
                base[int(idx[j])] = replace[j]
                val = "".join(base)
                if val[0] != "0": replaced.append(int(val))
            
    return set(replaced)
    

def sum_of_primes(digit, order):
    other_digits = list("0123456789")
    other_digits.remove(digit)
    acc = 0
        
    for i in range(1, order):
        checks = replace(digit, other_digits, i, order)
        for check in checks:
            if is_prime(check):
                acc += check

        if acc > 0: return acc
        
def euler111():
    acc = 0
    order = 10

    for digit in "0123456789":
        acc += sum_of_primes(digit, order)

    return acc

if __name__ == "__main__":
    print euler111()

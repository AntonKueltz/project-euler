from fractions import gcd

def euler182():
    p, q = 1009, 3643
    N, phi = p*q, (p-1)*(q-1)
    acc, lowest = 0, N
    
    for e in range(2, phi):
        if gcd(e, phi) == 1:
            unc = (1+gcd(e-1, p-1))*(1+gcd(e-1, q-1))
            if unc < lowest: acc, lowest = e, unc
            elif unc == lowest: acc += e

    return acc

if __name__ == "__main__":
    print euler182()

def minimal_x(D):
    a0 = int(D**0.5)
    a, m, d = a0, 0, 1
    h, k = a, 1
    n = 1
    h_1, k_1 = 1, 0

    while h**2 - D*(k**2) != 1:
        m = d*a - m
        d = (D - m**2) / d
        a = (a0 + m) / d

        nxt = ((a*h + 1*h_1), (a*k + 1*k_1))
        h_1, k_1 = h, k
        (h, k) = nxt

        n += 1

    return h

def euler66():
    max_x = (0, 0)
    
    for D in range(2, 1001):
        if D**0.5 == int(D**0.5): continue
        x = minimal_x(D)
        
        if x > max_x[0]: max_x = (x, D)

    return max_x[1]

if __name__ == "__main__":
    print euler66()

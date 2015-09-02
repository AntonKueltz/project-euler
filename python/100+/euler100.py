def euler100():
    # credit to Dario Alejandro Alpern for the general algorithm
	# this problem is basically a diophantine equation problem
    p, q, k, r, s, l = 3, 2, -2, 4, 3, -3
    n, m = 15, 21
    
    while n + m < 10**12:
        n_, m_ = n, m
        n = p*n_ + q*m_ + k
        m = r*n_ + s*m_ + l

    return n

if __name__ == "__main__":
    print euler100()

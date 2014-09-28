def fill_with(m, n):
    fills = [0]*(n+1)

    for i in range(m, n+1):
        fills[i] += i-(m-1)

        for tilelen in range(m, i+1):
            for j in range(m, i-tilelen):
                fills[i] += fills[j]

    return fills

def euler115():
    n = 50
    
    while True:
        fillcount = 1 + sum(fill_with(50,n))
        if fillcount > 1000000: return n
        n += 1

if __name__ == "__main__":
    print euler115()

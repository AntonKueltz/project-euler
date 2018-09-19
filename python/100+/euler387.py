from Crypto.Util.number import isPrime

def next_level(n):
    nsum = sum([int(x) for x in str(n)])
    hs = []
    ps = []

    for i in range(10):
        h = n * 10 + i
        if h % (nsum + i) == 0:
            hs.append(h)
        elif isPrime(h) and isPrime(n // nsum):
            ps.append(h)

    return hs, ps

def euler387():
    N = 14
    answer = 0

    level = [i for i in range(1, 10)]
    for _ in range(N-1):
        new_level = []
        for x in level:
           hs, ps = next_level(x)
           answer += sum(ps)
           new_level += hs
        level = new_level[:]
        
    return answer

if __name__ == '__main__':
    print euler387()


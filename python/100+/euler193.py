from euler_util import timed, gen_primes_to


def prime_squares(n):
    ps = gen_primes_to(n)
    return [p*p for p in ps]


def product(seq):
    return reduce(lambda x, y: x*y, [s[0] for s in seq])


def non_squarefree(seq, n):
    prod = product(seq)
    return n / prod


@timed
def squarefree(n):
    squares = prime_squares(int(n**0.5))
    n = n-1
    nonsquarefree = 0
    start = 0
    seq = [(squares[start], start)]

    while start < len(squares):
        val = non_squarefree(seq, n)
        if len(seq) % 2:
            nonsquarefree += val
        else:
            nonsquarefree -= val

        nexti = seq[-1][1] + 1

        if nexti >= len(squares):
            return n - nonsquarefree
        elif product(seq) * nexti <= n:
            seq.append((squares[nexti], nexti))
        else:
            seq = seq[:-1] + [(squares[nexti], nexti)]
            while product(seq) > n:
                seq = seq[:-1]
                nexti = seq[-1][1] + 1

                if nexti >= len(squares):
                    return n - nonsquarefree
                else:
                    seq = seq[:-1] + [(squares[nexti], nexti)]

        start = seq[0][1]

    return n - nonsquarefree

if __name__ == '__main__':
    print squarefree(2**50)

def divisors(N):
    ds = [[] for _ in xrange(N + 1)]
    for mul_of_two in range(2, N + 1, 2):
        ds[mul_of_two].append(2)

    for n in xrange(3, N + 1, 2):
        if not ds[n]:
            for p in range(n, N + 1, n):
                ds[p].append(n)

    return ds

def e347():
    answer = 0
    N = 10000000
    ds = divisors(N)
    seen = set()

    for d in ds[::-1]:
        if len(d) == 2 and tuple(d) not in seen:
            answer += N
            seen.add(tuple(d))
        N -= 1

    return answer

if __name__ == '__main__':
    print e347()

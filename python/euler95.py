def divisors(n):
    divs = [1]

    for i in range(2, int(n**0.5)+1):
        if n % i == 0: divs += set([i, n/i])

    return divs

def euler95():
    chains = []
    for _ in range(10**6): chains.append([])
    longest = 0, 0

    for i in range(2, 10**6):
        cur = i
        if cur % 1000 == 0: print cur
        chain = [cur]
        
        while cur < 10**6:
            # already computed from here onward
            if cur < i:
                try:
                    idx = chains[cur].index(1)
                    chain += (chains[cur])[1:idx]
                    break
                except:
                    break

            # compute next number and grow chain
            cur = sum(divisors(cur))
            if cur == i or cur == 1 or cur in chain: break
            chain.append(cur)

        chains[i] = chain
        if cur == i and len(chain) > longest[0]:
            longest = len(chain), i

    return min(chains[longest[1]])

if __name__ == "__main__":
    print euler95()

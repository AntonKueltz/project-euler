def fill_with(rowlen, tilelen):
    fills = [0]*(rowlen+1)

    for i in range(tilelen, rowlen+1):
        fills[i] += 1
        for j in range(tilelen, i-tilelen+1):
            fills[i] += fills[j]

    return fills

def euler116():
    twos = sum(fill_with(50, 2))
    threes = sum(fill_with(50,3))
    fours = sum(fill_with(50,4))
    return twos + threes + fours

if __name__ == "__main__":
    print euler116()

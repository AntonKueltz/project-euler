def fill_with(rowlen):
    fills = [0]*(rowlen+1)

    for i in range(3, rowlen+1):
        fills[i] += i-2

        for tilelen in range(3, i+1):
            for j in range(3, i-tilelen):
                fills[i] += fills[j]

    return fills

def euler114():
    return 1 + sum(fill_with(50))

if __name__ == "__main__":
    print euler114()

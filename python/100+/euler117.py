def fill_with(rowlen):
    fills = [0]*(rowlen+1)

    for i in range(2, rowlen+1):
        if i >= 3: fills[i] += 1
        if i >= 4: fills[i] += 1
        if i >= 2: fills[i] += 1

        for tilelen in [2,3,4]:
            for j in range(2, i-tilelen+1):
                fills[i] += fills[j]
                
    return fills

def euler117():
    return 1 + sum(fill_with(50))

if __name__ == "__main__":
    print euler117()

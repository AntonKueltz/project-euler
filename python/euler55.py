def reverse(n):
    rev = 0
    while n > 0:
        rev = 10*rev + n % 10
        n /=10
    return rev

def euler55():
    acc = 0
    
    for n in range(10000):
        tries = 0
        cand = n
        
        while tries < 50:
            cand = cand + reverse(cand)

            if cand == reverse(cand): break

            tries += 1

        if tries == 50: acc += 1

    return acc

if __name__ == "__main__":
    print euler55()

def euler57():
    acc = 0
    m, n = 3, 2
    
    for _ in range(1000):
        if len(str(m)) > len(str(n)): acc += 1

        tmp = n
        n = m + n
        m = n + tmp

    return acc

if __name__ == "__main__":
    print euler57()

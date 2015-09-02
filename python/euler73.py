def next_term(a,b,c,d):
    # Farey sequence
    tmp = (12000 + b) / d
    return tmp * c - a, tmp * d - b

def euler73():
    p, q = 1, 11999
    c, d = 1, 12000
    acc = 0

    while (p, q) != (1, 2):
        if p / float(q) > 1.0 / 3.0:
            acc += 1

        a, b = c, d
        c, d = p, q
        p, q = next_term(a,b,c,d)

    return acc

if __name__ == "__main__":
    print euler73()

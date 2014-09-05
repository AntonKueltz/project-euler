from collections import Counter

def read_cipher():
    f = open("p059_cipher.txt", "r")
    ctxt = map(int, f.read().split(","))
    return ctxt

def decrypt(ctxt, key):
    ptxt = []

    for i, char in enumerate(ctxt):
        ptxt.append(char^key)

    return ptxt

def sep_ctxt(ctxt):
    c1, c2, c3 = [], [], []
    
    for i, char in enumerate(ctxt):
        if i % 3 == 0: c1.append(char)
        elif i % 3 == 1: c2.append(char)
        elif i % 3 == 2: c3.append(char)

    return c1, c2, c3

def freq(c1, c2, c3):
    # find most common element under each key character
    m1 = Counter(c1).most_common(1)[0][0]
    m2 = Counter(c2).most_common(1)[0][0]
    m3 = Counter(c3).most_common(1)[0][0]

    return (m1, m2, m3)

def check_ptxt(ptxt):
    # look at ASCII values of valid characters and punctuation
    valid_ascii = range(32, 123)

    for p in ptxt:
        if not p in valid_ascii: return False

    return True

def euler59():
    most_freq = [ord("e"), ord("r"), ord(" "), ord("s"), ord("t")]
    ctxt = read_cipher()
    
    c1, c2, c3 = sep_ctxt(ctxt)
    m1, m2, m3 = freq(c1, c2, c3)

    acc = 0

    for char in most_freq:
        key = m1^char
        p1 = decrypt(c1, key)
        if check_ptxt(p1): acc += sum(p1)

        key = m2^char
        p2 = decrypt(c2, key)
        if check_ptxt(p2): acc += sum(p2)

        key = m3^char
        p3 = decrypt(c3, key)
        if check_ptxt(p3): acc += sum(p3)
    
    return acc

if __name__ == "__main__":
    print euler59()

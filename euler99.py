import math

def read_pairs():
    f = open("p099_base_exp.txt", "r")
    rows = f.read().split("\n")

    pairs = []
    for row in rows: pairs.append(map(int, row.split(",")))
    return pairs

def euler99():
    m, n = 0, 0
    pairs = read_pairs()

    # a^b > c^d -> b log a > c log d
    for i, pair in enumerate(pairs):
        cur = pair[1]*math.log(pair[0])
        if cur > m: m, n = cur, i+1

    return n

if __name__ == "__main__":
    print euler99()

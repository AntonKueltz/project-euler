from itertools import product
from euler_util import timed

@timed
def euler205():
    prolls = [sum(p) for p in product(range(1, 5), repeat=9)]
    crolls = [sum(p) for p in product(range(1, 7), repeat=6)]

    pfreq = [0]*(4*9+1)
    cfreq = [0]*(6*6+1)

    for roll in prolls: pfreq[roll] += 1
    for roll in crolls: cfreq[roll] += 1

    psum = float(sum(pfreq))
    csum = float(sum(cfreq))

    total_prob = 0.0

    for idx in range(len(pfreq)):
        roll_prob = pfreq[idx] / psum
        cless_prob = sum(cfreq[:idx]) / csum
        total_prob += roll_prob * cless_prob

    return round(total_prob, 7)

if __name__ == "__main__":
    print euler205()

import math
from euler_util import timed


@timed
def euler207():
    limit = 1.0 / 12345.0
    perfect, ks, ratio = 0, 0, 1
    two_tothe_t = 2

    while ratio >= limit:
        m = two_tothe_t * (two_tothe_t - 1)
        lg = math.log(two_tothe_t, 2)

        if lg == int(lg):
            perfect += 1

        two_tothe_t += 1
        ks += 1
        ratio = perfect / float(ks)

    return m

if __name__ == '__main__':
    print euler207()

from euler_util import timed


def validate(n):
    s = str(n)

    if s[14] != '8':
        return False
    elif s[12] != '7':
        return False
    elif s[10] != '6':
        return False
    elif s[8] != '5':
        return False
    elif s[6] != '4':
        return False
    elif s[4] != '3':
        return False
    elif s[2] != '2':
        return False
    elif s[0] != '1':
        return False
    else:
        return True


@timed
def euler206():
    n = int(1121314151617181910**0.5)
    n = (n / 100) * 100 + 30

    while True:
        if validate(n*n):
            return n
        elif n % 100 == 30:
            n += 40
        else:
            n += 60

if __name__ == '__main__':
    print euler206()

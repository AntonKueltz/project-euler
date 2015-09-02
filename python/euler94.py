def gen_tris(lim):
    x, y, x1, y1, n = 2, 1, 2, 1, 3
    count = 0

    while 2*x + 2 < lim:
        # side is 1 unit shorter than the other two
        a = (2*x - 1) / 3.0
        if int(a) == a:
            area = (y * (a-1)) / 2.0
            if area != 0 and int(area) == area: count += (3*a-1)

        # side is 1 unit longer than the other two
        a = (2*x + 1) / 3.0
        if int(a) == a:
            area = (y * (a+1)) / 2.0
            if area != 0 and int(area) == area: count += (3*a+1)

        # get next x, y
        xprev, yprev = x, y
        x = x1*xprev + n*y1*yprev
        y = x1*yprev + y1*xprev

    return int(count)

def euler94():
    return gen_tris(1000000000)
    

if __name__ == "__main__":
    print euler94()

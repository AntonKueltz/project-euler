def euler71():
    d, i = 7, 0
    while d < 1000000: d, i = d+7, i+1

    return 3 * i - 1

if __name__ == "__main__":
    print euler71()

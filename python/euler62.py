def euler62():
    d = {}
    n = 1

    while True:
        cube = n*n*n
        key = "".join(sorted(str(cube)))

        try:
            d[key].append(cube)
        except:
            d[key] = [cube]

        if len(d[key]) == 5: return min(d[key])

        n += 1

if __name__ == "__main__":
    print euler62()

def read_matrix():
    f = open("p081_matrix.txt", "r")
    rows = f.read().split("\n")[:-1]

    m = []
    for row in rows: m.append(map(int, row.split(",")))
    return m

def shortest_path(m):
    for c in range(len(m[0])):
        for r in range(len(m)):
            if c == 0 and r == 0: continue
            elif c == 0 and r > 0: m[r][c] += m[r-1][c]
            elif c != 0 and r == 0: m[r][c] += m[r][c-1]
            else: m[r][c] += min(m[r-1][c], m[r][c-1])

    return m[-1][-1]

def euler81():
    m = read_matrix()
    return shortest_path(m)

if __name__ == "__main__":
    print euler81()

def read_triangle():
    f = open("p067_triangle.txt", "r")
    rows = f.read().split("\n")[:-1]

    tri = []
    for row in rows: tri.append(map(int, row.split(" ")))
    return tri

def max_path(tri):
    # start with second to last row and work backwards
    for i in range(len(tri)-2, -1, -1):
        for j in range(len(tri[i])):
            tri[i][j] += max(tri[i+1][j], tri[i+1][j+1])

    return tri[0][0]

def euler67():
    tri = read_triangle()
    return max_path(tri)

if __name__ == "__main__":
    print euler67()

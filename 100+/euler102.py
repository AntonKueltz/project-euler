def read_in_tris():
    f = open("p102_triangles.txt", "r")
    tmp = f.read().split("\n")
    tris = []

    for tri in tmp:
        tri = tri.replace(",", " ")
        tris.append(map(int, tri.split()))

    return tris

def euler102():
    tris = read_in_tris()
    origin_inside = 0

    # use barycentric coordinate method
    for tri in tris[:-1]:
        (p1, p2, p3) = ((tri[0], tri[1]), (tri[2], tri[3]), (tri[4], tri[5]))
        tmp = ((p2[1] - p3[1])*(p1[0] - p3[0]) + (p3[0] - p2[0])*(p1[1] - p3[1]))
        a = ((p2[1] - p3[1])*(0 - p3[0]) + (p3[0] - p2[0])*(0 - p3[1])) / float(tmp)
        b = ((p3[1] - p1[1])*(0 - p3[0]) + (p1[0] - p3[0])*(0 - p3[1])) / float(tmp)
        c = 1.0 - a - b

        if 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1: origin_inside += 1
        
    return origin_inside

if __name__ == "__main__":
    print euler102()

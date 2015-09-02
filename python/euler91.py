def euler91():
    size =  50
    tris = size*size # one point is on the x axis, the other is on the y axis
    
    for x in range(1,size+1):
        for y in range(1, size+1):
            tris += 2 # other point is (x,0) or (0,y)

            # slope of line that forms right angle at (x,y) is -x/y
            for y_ in range(size, -1, -1):
                if y_ == y: continue

                # (y_ - y) = (-x/y) * (x_ - x), solve for x, ensure x is int
                if ((y_*y)-(y*y)) % x == 0:
                    x_ = -((y_*y)-(y*y)) / x + x
                    if x_ >= 0 and x_ <=size: tris += 1
                    
    return tris

if __name__ == "__main__":
    print euler91()

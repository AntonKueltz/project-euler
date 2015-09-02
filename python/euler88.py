def prodsum(prod, sm, facs, curfac, mins):
    k = prod - sm + facs
    
    if k < 12000:
        mins[k] = min(mins[k], prod)
        for fac in range(curfac, 24000/prod):
            prodsum(prod*fac, sm+fac, facs+1, fac, mins)

def euler88():
    mins = [24000]*12000
    prodsum(1, 1, 1, 2, mins)
    
    return sum(set(mins[2:]))

if __name__ == "__main__":
    print euler88()

def u(k, r):
    return (900 - (3 * k)) * (r ** (k-1))  

def s(n, r):
    sm = 0
    for i in range(1, n+1):
    	t = u(i, r)
    	sm += t

    return sm

def euler235():
    n = 5000
    r = 1.0
    target = -600000000000

    for place in range(1, 14): # 1 extra digit for rounding
        scale = 10**(-place)
        digit = 0

        while s(n, r + (digit+1)*scale) > target: 
            digit += 1
        
        r += digit*scale

    return r

if __name__ ==  "__main__":
    print "%.12f" % euler235()
def digital_root(n):
    if n == 0: return 0
    elif n % 9 == 0: return 9
    else: return n % 9

def mdrs(n):
    drs = [0]*n
    
    for i in range(2, n):
        if i % 1000 == 0: print i
        drs[i] = max(drs[i], digital_root(i))
			   
        for fac in range(2, i+1):
            cur = i * fac
            if cur >= n: break
            drs[cur] = max(drs[cur], drs[i]+drs[fac])

    return drs[2:]

def euler151():
    return sum(mdrs(1000000))
        
if __name__ == "__main__":
    print euler151()

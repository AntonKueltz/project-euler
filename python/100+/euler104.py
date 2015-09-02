def both(n):
    if not back(n): return False
    return front(n)

def back(n):
    return pandigital(n % 1000000000)

def front(n):
    if n < 100000000: return False
    length = len(str(n))
    return pandigital(n / (10**(length-9)))

def pandigital(n):
    if n < 100000000: return False
    
    digits = [0]*10
    
    while n != 0:
        d = n % 10
        if d == 0 or digits[d] > 0: return False
        else: digits[d] = 1
        n /= 10
        
    return True

def euler104():
    f1, f2, f3, n = 1, 1, 1, 2

    while not both(f3):
        f3 = f1+f2
        f1 = f2
        f2 = f3
        n += 1

    return n
            
if __name__ == "__main__":
    # 32 seconds :/
    print euler104()

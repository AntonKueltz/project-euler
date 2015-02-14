def calc_divisors(n):
    divisors = [1] * n
    
    for i in range(2, n):
        idx = i
        while idx < n:
            divisors[idx] += 1
            idx += i

    return divisors
    
def euler179():
    count = 0
    divs = calc_divisors(10**7)
    
    for i in range(2, len(divs)):
        if divs[i-1] == divs[i]: count += 1

    return count

if __name__ == "__main__":
    print euler179()

from math import log

def basic_twos(n):
    high = int(log(n, 2))
    twos = []

    for i in range(high, -1, -1):
        if(n - 2**i) >= 0:
            twos.append(i)
            n -= 2**i

    return twos[::-1]

def get_partitions(twos):
    count, tmp = 1, 0

    for i in range(len(twos)):
        if i == 0: ways = twos[i] + 1
        else: ways = twos[i] - twos[i-1]

        count = (count * ways) + tmp
        tmp = (ways-1) * ((count-tmp) / ways) + tmp
        
    return count

def euler169():
    return get_partitions(basic_twos(10**25))
        
if __name__ == "__main__":
    print euler169()

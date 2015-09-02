from euler_util import gen_primes_to

def euler03():
        """
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143 ?
        """
        n = 600851475143
        ps = gen_primes_to(10000)

        for p in ps:
                if n % p == 0: n /= p
                if p > n: return p

        return -1 # failure
        
if __name__ == "__main__":
        print euler03()

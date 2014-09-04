from euler_util import gen_primes_to

def euler123():
	primes = gen_primes_to(10**6)
	
	for n, p in enumerate(primes):
		if (n + 1) % 2 == 0: continue
		rem = 2 * (n+1) * p
		if rem > 10000000000: return n+1 

	return -1
		
if __name__ == "__main__":
	print euler123()

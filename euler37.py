import euler_util

primes = euler_util.gen_primes_to(1000000) # fix bound later?

def is_trunc(p):
	single_primes = [2,3,5,7]
	
	if not ((p % 10) in single_primes): return False
	if not ((p / 10 ** (len(str(p))-1)) in single_primes): return False
	
	left = p / 10
	while left > 0:
		if not euler_util.is_prime(left): return False
		left /= 10
		
	right = p % (10 ** (len(str(p))-1))
	while right > 0:
		if not euler_util.is_prime(right): return False
		right = right % (10 ** (len(str(right))-1))
		
	return True

def euler37():
	"""
	The number 3797 has an interesting property. Being prime itself, it is possible
	to continuously remove digits from left to right and remain prime at each
	stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797,
	379, 37, 3.
	
	Find the sum of the only eleven primes that are both truncatable from left to
	right and right to left.
	
	NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes. 
	"""
	found = 0
	truncatable = []
	
	for prime in primes:
		if prime < 10: continue
		if is_trunc(prime): truncatable.append(prime)
		if len(truncatable) == 11:
			return sum(truncatable)

if __name__ == "__main__":
	print euler37()

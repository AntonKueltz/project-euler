import euler_util

def euler50():
	"""
	The prime 41, can be written as the sum of six consecutive primes:

	41 = 2 + 3 + 5 + 7 + 11 + 13

	This is the longest sum of consecutive primes that adds to a prime below
	one-hundred.

	The longest sum of consecutive primes below one-thousand that adds to a
	prime, contains 21 terms, and is equal to 953.

	Which prime, below one-million, can be written as the sum of the most
	consecutive primes?
	"""
	primes = euler_util.gen_primes_to(1000000)
	longest = 0
	sum_prime = 0
	
	for start in range(0, len(primes)):
		if primes[start] * longest > 1000000: break
		
		for stop in range(start+longest+1, len(primes)):
			cand = sum(primes[start:stop])
			if cand > 1000000: break
			
			if cand in primes:
				length = stop - start + 1
				if length > longest: (longest, sum_prime) = (length, cand)
	
	return sum_prime
	
if __name__ == "__main__":
	print euler50()

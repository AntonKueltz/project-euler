import euler_util

def euler87():
	"""
	The smallest number expressable as the sum of a prime square, prime cube,
	and prime fourth power is 28. In fact, there are exactly four numbers
	bleow fifty that can be expressed in such a way.
	
	How many numbers below fifty million can be expressed as the sum of a prime
	square, a prime cube, and prime fourth power?
	"""
	primes = euler_util.gen_primes_to(int(50000000**0.5)+1)
	nums = []
	
	for sqr in range(len(primes)):
		square = primes[sqr]**2
		cub = 0
		while square + primes[cub]**3 < 50000000:
			cube = primes[cub]**3
			quad = 0
			while square + cube + primes[quad]**4 < 50000000:
				fourth = primes[quad]**4
				nums.append(square + cube + fourth)
				quad += 1
			cub += 1
			
	return len(set(nums))

if __name__ == "__main__":
	print euler87()

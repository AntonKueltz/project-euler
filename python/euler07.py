def euler07():
	"""
	By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
	that the 6th prime is 13.

	What is the 10 001st prime number?
	"""
	primes = [2]
	cand = 3
	
	while len(primes) < 10001:
		i = 0
		prime = True
		
		while primes[i] <= cand ** 0.5:
			if cand % primes[i] == 0:
				prime = False
				break
			i += 1
		
		if prime: primes.append(cand)
		
		cand += 2
		
	return primes[-1]

if __name__ == "__main__":
	print euler07()

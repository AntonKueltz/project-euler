def gen_primes_to(n):
	"""
	generate all prime numbers up to n
	"""
	if n == 2: return []
	
	primes = [2]
	cand = 3

	while cand < n:
		is_prime = True
		idx = 0

		while primes[idx] <= cand ** 0.5:
			if cand % primes[idx] == 0:
				is_prime = False
				break

			idx += 1

		if is_prime: primes.append(cand)

		cand += 2

	return primes

def is_prime(n):
	"""
	check if a number is prime
	"""
	if n < 1: return False
	
	cands = range(2, int(n**0.5)+1)
	
	for cand in cands:
		if n % cand == 0: return False
		
	return True

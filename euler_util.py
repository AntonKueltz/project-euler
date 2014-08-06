def gen_primes_to(n):
	"""
	generate all prime numbers up to n
	"""
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

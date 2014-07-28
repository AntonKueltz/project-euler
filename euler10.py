def gen_primes_up_to(n):
	primes = [2]
	cand = 3
	
	while True:
		ind = 0
		is_prime = True
		
		while primes[ind] <= cand**0.5:
			if cand % primes[ind] == 0:
				is_prime = False
				break
			ind += 1
		
		if is_prime: primes.append(cand)
		
		cand += 2
		if cand >= n: return primes
	
def euler10():
	"""
	The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

	Find the sum of all the primes below two million.
	"""
	return sum(gen_primes_up_to(2000000))
	
if __name__ == "__main__":
	print euler10()
	
			
		
	

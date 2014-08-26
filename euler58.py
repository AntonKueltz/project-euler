import euler_util

def euler58():
	"""
	TODO when internet is recovered
	"""
	seed = 1
	side_length = 1
	ratio = 1.0
	primes = 0
	total = 1.0
	
	while ratio >= 0.1:
		side_length += 2
		inc = side_length - 1
		
		for i in range(1, 5):
			cand = seed + (i * inc)
			if euler_util.is_prime(cand): primes += 1
			
		total += 4
		seed += inc * 4
		ratio = primes / total
		
	return side_length
		
if __name__ == "__main__":
	print euler58()

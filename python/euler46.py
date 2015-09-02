import euler_util

def euler46():
	"""
	It was proposed by Christian Goldbach that every odd composite number can
	be written as the sum of a prime and twice a square.

	9 = 7 + 2x1^2
	15 = 7 + 2x2^2
	21 = 3 + 2x3^2
	25 = 7 + 2x3^2
	27 = 19 + 2x2^2
	33 = 31 + 2x1^2

	It turns out that the conjecture was false.

	What is the smallest odd composite that cannot be written as the sum of a
	prime and twice a square?
	"""
	primes = euler_util.gen_primes_to(10000)
		
	for i in range(3, 10000, 2):
		if i in primes: continue
		satisfied = False
		
		for root in range(1, int((i/2)**0.5)+1):
			if (i - 2 * root ** 2) in primes: 
				satisfied = True
				break
			
		if not satisfied: return i
		
if __name__ == "__main__":
	print euler46()

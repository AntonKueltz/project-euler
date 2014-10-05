import numpy

def gen_primes_to(n):
        ps = numpy.arange(3, n+1, 2)
        prime = numpy.ones((n-1) / 2, dtype=bool)

        for f in ps[:int(n**0.5)]:
                if prime[(f-2) / 2]: prime[(f*3 - 2) / 2::f] = 0
                
        return numpy.insert(ps[prime], 0, 2).tolist()

def is_prime(n):
	"""
	check if a number is prime
	"""
	if n < 1: return False
	
	cands = range(2, int(n**0.5)+1)
	
	for cand in cands:
		if n % cand == 0: return False
		
	return True

from euler_util import gen_primes_to

b_ns = [0]
c_ns = [0]
primes = gen_primes_to(100)

def prime_divisors(n):
	divisors = []
	
	for p in primes:
		if p > n: break
		if n % p == 0: divisors.append(p)
		
	return divisors

def prime_partitions(n):
	# this done via a euler transform
	c_n = sum(prime_divisors(n))
	
	tmp = 0
	for k in range(len(b_ns)):
		tmp += c_ns[k]*b_ns[n-2-k]
	
	b_n = (c_n + tmp) / n
	
	b_ns.append(b_n)
	c_ns.append(c_n)
	
	return b_n

def euler77():
	"""
	It is possible to write ten as the sum of primes in exactly five different
	ways:

	7 + 3
	5 + 5
	5 + 3 + 2
	3 + 3 + 2 + 2
	2 + 2 + 2 + 2 + 2

	What is the first value which can be written as the sum of primes in over five
	thousand different ways?
	"""
	n = 2
	
	while prime_partitions(n) <= 5000:
		n += 1
		
	return n

if __name__ == "__main__":
	print euler77()

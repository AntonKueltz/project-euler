from fractions import gcd

def isPrime(n):
	for i in range(2, int(n**0.5)+1):
		if n % i == 0: return False
	return True

def euler131():
	m = 2
	n = m-1
	ps = 0

	while m**3 - n**3 < 1000000:
		p = m**3 - n**3
		
		if isPrime(p): ps += 1

		m += 1
		n = m-1

	return ps

if __name__ == "__main__":
	print euler131()
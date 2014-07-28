def is_prime(n):
	# quick and dirty implementation, there are faster checks
	i = 3
	
	while i <= n**0.5:
		if n % i == 0: return False
		i += 2
		
	return True

def euler03():
	"""
	The prime factors of 13195 are 5, 7, 13 and 29.

	What is the largest prime factor of the number 600851475143 ?
	"""
	largest = 0
	
	for i in range(3, int(600851475143**0.5), 2):
		if 600851475143 % i == 0:
			if is_prime(i): largest = i
			if is_prime(600851475143 / i): return 600851475143 / i
			
	return largest 
	
if __name__ == "__main__":
	print euler03()

def proper_divisors(n):
	divisors = [1]
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n / i)
	return set(divisors)

def euler21():
	"""
	Let d(n) be defined as the sum of proper divisors of n (numbers less than
	n which divide evenly into n).
	If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
	and each of a and b are called amicable numbers.

	For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
	44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
	2, 4, 71 and 142; so d(284) = 220.

	Evaluate the sum of all the amicable numbers under 10000.
	"""
	amic_sum = 0
	skip = [False]*10000
	
	for a in range(1, 10000):
		if skip[a]: 
			continue
		b = sum(proper_divisors(a))
		
		if a == b: 
			continue
		elif a == sum(proper_divisors(b)):
			skip[b] = True
			amic_sum += (a + b)
			
	return amic_sum
	
if __name__ == "__main__":
	print euler21()
	

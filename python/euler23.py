def proper_divisors(n):
	divisors = [1]
	for i in range(2, int(n**0.5)+1):
		if n % i == 0:
			divisors.append(i)
			divisors.append(n / i)
	return set(divisors)

def euler23():
	"""
	A perfect number is a number for which the sum of its proper divisors is
	exactly equal to the number. For example, the sum of the proper divisors
	of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
	number.

	A number n is called deficient if the sum of its proper divisors is less
	than n and it is called abundant if this sum exceeds n.

	As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
	smallest number that can be written as the sum of two abundant numbers is
	24. By mathematical analysis, it can be shown that all integers greater
	than 28123 can be written as the sum of two abundant numbers. However,
	this upper limit cannot be reduced any further by analysis even though it
	is known that the greatest number that cannot be expressed as the sum of
	two abundant numbers is less than this limit.

	Find the sum of all the positive integers which cannot be written as the
	sum of two abundant numbers.
	"""
	upper_bound = 28124
	sum_of_abundant = [False]*upper_bound
	abundant = []
	
	for i in range(1, upper_bound):
		if sum(proper_divisors(i)) > i: 
			abundant.append(i)
		
	for i in range(0, len(abundant)):
		for j in range(0, len(abundant)):
			tmp = abundant[i] + abundant[j]
			if tmp < upper_bound: sum_of_abundant[tmp] = True
				
	return sum([i for i in range(0, upper_bound) if not sum_of_abundant[i]])

if __name__ == "__main__":
	print euler23()

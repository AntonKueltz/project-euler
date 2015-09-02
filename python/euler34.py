fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def fac_sum(n):
	f_sum = 0
	
	while n > 0:
		f_sum += fac[n % 10]
		n /= 10
		
	return f_sum

def euler34():
	"""
	145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

	Find the sum of all numbers which are equal to the sum of the factorial of
	their digits.

	Note: as 1! = 1 and 2! = 2 are not sums they are not included.
	"""
	dig_fac_sum = 0
	
	# 2540160 = 9! * 7
	for n in range(10, 2540160):
		if n == fac_sum(n): dig_fac_sum += n
		
	return dig_fac_sum

if __name__ == "__main__":
	print euler34()

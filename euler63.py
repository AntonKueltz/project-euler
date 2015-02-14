def euler63():
	"""
	The 5-digit number, 16807 = 7^5, is also a fifth power. Similarly, the 
	9-digit number, 134217728 = 8^9, is a ninth power.
	
	How many n-digit positive integers exist which are also an nth power?
	"""
	total = 0
	n = 1
	
	# 10^n always has more digits, once 9^n has less than n digits we're done
	while len(str(9**n)) >= n:
		base = 1
		 
		while len(str(base**n)) <= n:
			if len(str(base**n)) == n: total += 1
			base += 1
						
		n += 1
	
	return total
	
if __name__ == "__main__":
	print euler63()

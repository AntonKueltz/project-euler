def euler32():
	"""
	We shall say that an n-digit number is pandigital if it makes use of all
	the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
	1 through 5 pandigital.

	The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing
	multiplicand, multiplier, and product is 1 through 9 pandigital.

	Find the sum of all products whose multiplicand/multiplier/product
	identity can be written as a 1 through 9 pandigital.
	"""
	found = []
	
	# candidates are 4 dig numbers resulting from 1 dig * 4 dig
	for i in range(2, 10):
		for j in range(1234, 10000):
			if i * j >= 10000: break
			
			digits = set(str(i)+str(j)+str(i*j))
			if "0" in digits: continue # only want digits 1-9
			
			if len(digits) == 9: found.append(i*j)
	
	# candidates are 4 dig numbers resulting from 2 dig * 3 dig
	for i in range(12, 100):
		for j in range(123, 1000):
			if i * j >= 10000: break
			
			digits = set(str(i)+str(j)+str(i*j))
			if "0" in digits: continue # only want digits 1-9
			
			if len(digits) == 9: found.append(i*j)
			
	return sum(set(found))

if __name__ == "__main__":
	print euler32()

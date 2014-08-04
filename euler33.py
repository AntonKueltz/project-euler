import fractions

def euler33():
	"""
	The fraction 49/98 is a curious fraction, as an inexperienced
	mathematician in attempting to simplify it may incorrectly believe that
	49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

	We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

	There are exactly four non-trivial examples of this type of fraction, less
	than one in value, and containing two digits in the numerator and
	denominator.

	If the product of these four fractions is given in its lowest common
	terms, find the value of the denominator.
	"""
	product_top, product_bottom = 1, 1
	
	for n in range(10, 100):
		for d in range(n+1, 100):
			if n % 10 == 0 or d % 10 == 0: continue
			
			# cancel top left, bottom right
			if n / 10 == d % 10 and ((n % 10) / float(d / 10)) == n/float(d):
				product_top *= n
				product_bottom *= d
					
			# cancel top right, bottom left
			if n % 10 == d / 10 and ((n / 10) / float(d % 10)) == n/float(d):
				product_top *= n
				product_bottom *= d
					
	return product_bottom / fractions.gcd(product_top, product_bottom)

if __name__ == "__main__":
	print euler33()

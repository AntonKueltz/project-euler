def euler65():
	"""
	The square root of 2 can be written as an infinite continued fraction.

	The infinite continued fraction can be written, sqrt(2) = [1;(2)], (2)
	indicates that 2 repeats ad infinitum. In a similar way, sqrt(23) = [4
	(1,3,1,8)].

	It turns out that the sequence of partial values of continued fractions for
	square roots provide the best rational approximations. Let us consider the
	convergents for 
 
	Hence the sequence of the first ten convergents for sqrt(2) are:

	1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
	What is most surprising is that the important mathematical constant,
	e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

	The first ten terms in the sequence of convergents for e are:

	2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
	The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

	Find the sum of digits in the numerator of the 100th convergent of the
	continued fraction for e.
	"""
	# numerator_n = (convergent in sequence) * numerator_n-1 + numerator_n-2
	hn_1 = 3
	hn_2 = 2
	k = 1
	for n in range(3, 101):
		if n % 3 == 0:	# every third term is 2*k
			tmp = hn_1 
			hn_1 = k*2*(hn_1) + hn_2
			hn_2 = tmp
			k += 1
		else:			# rest of the terms are 1
			tmp = hn_1
			hn_1 = hn_1 + hn_2
			hn_2 = tmp
	
	return sum([int(c) for c in str(hn_1)])

if __name__ == "__main__":
	print euler65()

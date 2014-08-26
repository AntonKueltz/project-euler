def euler65():
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

def euler38():
	largest = 0
	sorted_pandigital = list("123456789")

	for i in range(1, 10000):
		n = 1
		cand = ""
		
		while len(cand) < 9:
			cand += str(i * n)
			n += 1
			
		if sorted_pandigital ==  sorted(cand) and int(cand) > largest:
			largest = int(cand)
			
	return largest 
		
if __name__ == "__main__":
	print euler38()

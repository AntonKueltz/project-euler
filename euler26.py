def cycle_length(n):
	numer = 1
	digits = []
	rems = []
	
	while True:
		while numer < n: numer *= 10
		digits.append(numer / n)
		numer = numer % n
		
		if numer == 0: return 0
		if numer in rems: return len(rems) - rems.index(numer)
		else: rems.append(numer)
				
def euler26():
	"""
	A unit fraction contains 1 in the numerator. The decimal representation of
	the unit fractions with denominators 2 to 10 are given:

	1/2	= 	0.5
	1/3	= 	0.(3)
	1/4	= 	0.25
	1/5	= 	0.2
	1/6	= 	0.1(6)
	1/7	= 	0.(142857)
	1/8	= 	0.125
	1/9	= 	0.(1)
	1/10	= 	0.1
	Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
	be seen that 1/7 has a 6-digit recurring cycle.

	Find the value of d < 1000 for which 1/d contains the longest recurring 	cycle in its decimal fraction part.	
	"""
	max_cycle = (0,0)
	
	for d in range(2, 1000):
		d_cycle = cycle_length(d)
		if d_cycle > max_cycle[0]: max_cycle = (d_cycle, d)
		
	return max_cycle[1]

if __name__ == "__main__":
	print euler26()

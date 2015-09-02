def euler162():
	s = 0

	for digits in range(3, 17):
		total = 15*16**(digits-1) # no leading zero

		# 0, 1 or A is missing
		mis = 15**(digits) + 2 * 14 * 15**(digits-1)
		# 0 and 1, 0 and A, 1 and A missing
		z_o = 14**(digits)
		z_a = 14**(digits)
		o_z = 13 * 14**(digits-1)
		# 0 1 and A all missing
		z_o_a = 13**digits

		# inclusion exclusion principle
		s += total - (mis - z_o - z_a - o_z + z_o_a)

	return s

if __name__ == "__main__":
	print "%X" % euler162()
from itertools import permutations

def valid(n):
	if int(n[1:4]) % 2: return False
	if int(n[2:5]) % 3: return False
	if int(n[3:6]) % 5: return False
	if int(n[4:7]) % 7: return False
	if int(n[5:8]) % 11: return False
	if int(n[6:9]) % 13: return False
	if int(n[7:]) % 17: return False
	return True

def euler43():
	"""
	The number, 1406357289, is a 0 to 9 pandigital number because it is made
	up of each of the digits 0 to 9 in some order, but it also has a rather
	interesting sub-string divisibility property.

	Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we
	note the following:

	d2d3d4=406 is divisible by 2
	d3d4d5=063 is divisible by 3
	d4d5d6=635 is divisible by 5
	d5d6d7=357 is divisible by 7
	d6d7d8=572 is divisible by 11
	d7d8d9=728 is divisible by 13
	d8d9d10=289 is divisible by 17
	
	Find the sum of all 0 to 9 pandigital numbers with this property.
	"""
	cands = ["".join(p) for p in permutations("0123456789")]
	s = 0
	
	for cand in cands:
		if valid(cand): s += int(cand)
		
	return s

if __name__ == "__main__":
	print euler43()



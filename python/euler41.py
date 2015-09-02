from itertools import permutations
import euler_util

def euler41():
	"""
	We shall say that an n-digit number is pandigital if it makes use of all the
	digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is
	also prime.
	
	What is the largest n-digit pandigital prime that exists?
	"""
	# last digit can't be 5 or even
	last_digits = [1,3,7,9]
		
	# all pandigitals of length 8 and 9 are divisible by 3 since the sum of their
	# digits (36 and 45) are divisible by 3 so start with length 7
	cands = ([int("".join(p)) for p in permutations("1234567")])[::-1]
	
	for cand in cands:
		if not cand % 10 in last_digits: continue
		if euler_util.is_prime(cand): return cand
		
if __name__ == "__main__":
	print euler41()

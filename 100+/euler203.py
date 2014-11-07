from euler_util import gen_primes_to

def gen_next_row(prev_row):
	next_row = []

	for i in range(1, len(prev_row)):
		next_row.append(prev_row[i] + prev_row[i-1])

	return [1] + next_row + [1]

def square_free(val, ps):
	for p in ps:
		if p*p > val: break
		if val % (p*p) == 0: return False
	return True

def euler203():
	vals = [1, 2]
	row = [1, 2, 1]

	for _ in range(51-3):
		row = gen_next_row(row)
		vals += row

	vals = set(vals)
	ps = gen_primes_to(int(max(vals)**0.5))
	sm = 0

	for val in vals:
		if square_free(val, ps): sm += val

	return sm

if __name__ == "__main__":
	print euler203()
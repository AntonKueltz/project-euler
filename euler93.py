from itertools import combinations
from itertools import permutations

def generate_vals(digits):
	add = lambda x,y: x + y
	sub = lambda x,y: x - y
	div = lambda x,y: x / y if y != 0 else -100000000000
	mul = lambda x,y: x * y
	ops = [add, sub, div, mul]
	digs = map(float, [digits[0], digits[1], digits[2], digits[3]])
	vals = []
	
	dig_indices = [map(int, p) for p in permutations("0123")]
	op_indices = [map(int, p) for p in permutations("000111222333", 3)]
	
	for op_i in op_indices:
		for dig_i in dig_indices:
			tmp1 = ops[op_i[0]](digs[dig_i[0]], digs[dig_i[1]])
			tmp2 = ops[op_i[1]](digs[dig_i[2]], digs[dig_i[3]])
			vals.append(ops[op_i[2]](tmp1, tmp2))
			
			tmp1 = ops[op_i[1]](digs[dig_i[1]], digs[dig_i[2]])
			tmp2 = ops[op_i[2]](tmp1, digs[dig_i[3]])
			vals.append(ops[op_i[0]](digs[dig_i[0]], tmp2))
			
			tmp1 = ops[op_i[0]](digs[dig_i[0]], digs[dig_i[1]])
			tmp2 = ops[op_i[1]](tmp1, digs[dig_i[2]])
			vals.append(ops[op_i[2]](tmp2, digs[dig_i[3]]))
			
	return vals

def consec_ints(values):
	sort = sorted(set(values))
	
	for i in range(len(sort)):
		if not i+1 in sort: break
		
	return i

def euler93():
	dig_set = [map(int, c) for c in combinations("123456789", 4)]
	longest = (0, [])
	
	for digits in dig_set:
		vals = generate_vals(digits)
		consec = consec_ints(vals)
		
		if consec > longest[0]: longest = (consec, digits)
		
	return reduce(lambda x,y: x+y, [str(c) for c in sorted(longest[1])])

if __name__ == "__main__":
	print euler93()

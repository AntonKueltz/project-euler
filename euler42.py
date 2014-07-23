def create_val_list():
	f = open("words.txt")
	words = f.read().replace("\"", "")
	word_arr = words.split(",")
	int_val = lambda x: sum([(ord(c) - 64) for c in x])
	return [int_val(w) for w in word_arr]
	
def gen_tri_up_to(n):
	next = 1
	i = 1
	tris = [1]
	
	while next <= n:
		i += 1
		next = int(0.5*i*(i+1))
		tris.append(next)
		
	return tris

def euler42():
	"""
	The nth term of the sequence of triangle numbers is given by, tn = 1/2(n
	+1); so the first ten triangle numbers are:

	1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

	By converting each letter in a word to a number corresponding to its
	alphabetical position and adding these values we form a word value. For
	example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
	value is a triangle number then we shall call the word a triangle word.

	Using words.txt, a 16K text file containing nearly two-thousand common 
	English words, how many are triangle words?
	"""
	val_list = create_val_list()
	tri_nums = gen_tri_up_to(max(val_list))
	
	return sum([val_list.count(tri) for tri in tri_nums])

if __name__ == "__main__":
	print euler42()

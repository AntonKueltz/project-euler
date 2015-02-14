from itertools import permutations

def read_in_words():
	f = open("p098_words.txt", "r")
	return f.read().replace("\"","").split(",")
	
def find_anagrams(words):
	letters = []
	for word in words: letters.append(sorted(word))
	
	tmp = []
	for word in letters:
		if letters.count(word) > 1 and not word in tmp: 
			tmp.append(word)
		
	anagrams = []
	for t in tmp:
		for idx, word in enumerate(letters):
			if t == word: anagrams.append(words[idx])
				
	return anagrams

def max_square(word1, word2, word3=""):
	num_letters = len(set(word1))
	possible_vals = permutations("123456789", num_letters)
	max_val = 0
	
	for vals in possible_vals:
		m = {}
		cand3 = 0
		for letter, val in zip(set(word1), vals): m[letter] = val
		
		cand1 = int("".join([m[w] for w in word1]))
		if int(cand1**0.5) != cand1**0.5: continue
		cand2 = int("".join([m[w] for w in word2]))
		if int(cand2**0.5) != cand2**0.5: continue
		
		if word3 != "":
			cand3 = int("".join([m[w] for w in word3]))
			if int(cand3**0.5) != cand3**0.5: continue
			
		high = max([cand1, cand2, cand3])
		if high > max_val: max_val = high
		
	return max_val	

def euler98():
	words = read_in_words()
	anagrams = find_anagrams(words)
	max_val, i = 0, 0
	
	while i < len(anagrams):
		if i == 66:
			val = max_square(anagrams[i], anagrams[i+1], anagrams[i+2])
			i += 3
		else: 
			val = max_square(anagrams[i], anagrams[i+1])
			i += 2
			
		if val > max_val: max_val = val
	
	return max_val
	
if __name__ == "__main__":
	print euler98()

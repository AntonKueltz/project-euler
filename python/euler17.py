def euler17():
	"""
	If the numbers 1 to 5 are written out in words: one, two, three, four,
	five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

	If all the numbers from 1 to 1000 (one thousand) inclusive were written
	out in words, how many letters would be used?
	"""
	num_to_word = {
		1:"one", 
		2:"two", 
		3:"three", 
		4:"four",
		5:"five",
		6:"six",
		7:"seven",
		8:"eight",
		9:"nine",
		10:"ten",
		11:"eleven",
		12:"twelve",
		13:"thirteen",
		14:"fourteen",
		15:"fifteen",
		16:"sixteen",
		17:"seventeen",
		18:"eighteen",
		19:"nineteen",
		20:"twenty",
		30:"thirty",
		40:"forty",
		50:"fifty",
		60:"sixty",
		70:"seventy",
		80:"eighty",
		90:"ninety"
	}
	
	total_letters = 0
	
	for i in range(1, 1001):
		word = ""
		# 1000 is an asshole
		if i == 1000:
			word = "onethousand"
			total_letters += len(word)
			continue
	
		# value is in the dict
		if i in num_to_word.keys():
			word = num_to_word[i]
			total_letters += len(word)
			continue
			
		# value is not in the dict
		if i >= 100:
			word += num_to_word[i/100] + "hundred"
		
		if i % 100 != 0:
			if i > 100:
				word += "and"
			if 19 >= (i % 100) >= 10:
				word += num_to_word[i % 100]
			else:
				if i % 100 >= 20:
					word += num_to_word[((i % 100) / 10) * 10]
				if i % 10 > 0:
					word += num_to_word[i % 10]
					
		total_letters += len(word)
		
	return total_letters

if __name__ == "__main__":
	print euler17()

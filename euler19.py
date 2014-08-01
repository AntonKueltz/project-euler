def euler19():
	"""
	You are given the following information, but you may prefer to do some
	research for yourself.

	1 Jan 1900 was a Monday.
	Thirty days has September,
	April, June and November.
	All the rest have thirty-one,
	Saving February alone,
	Which has twenty-eight, rain or shine.
	And on leap years, twenty-nine.
	A leap year occurs on any year evenly divisible by 4, but not on a century
	unless it is divisible by 400.
	
	How many Sundays fell on the first of the month during the twentieth
	century (1 Jan 1901 to 31 Dec 2000)?
	"""
	# first day = Tuesday
	days = 0
	sundays = 0 # sunday is a day % 7 = 5
	
	#year cycle
	for year in range(1901, 2001):
		days += 31 # January
		if days % 7 == 5: sundays += 1
		
		if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
			days += 29 # February (leap year)
			if days % 7 == 5: sundays += 1
		else:
			days += 28	# February
			if days % 7 == 5: sundays += 1
		
		days += 31	# March
		if days % 7 == 5: sundays += 1
		
		days += 30	# April
		if days % 7 == 5: sundays += 1
		
		days += 31 	# May
		if days % 7 == 5: sundays += 1
		
		days += 30	# June
		if days % 7 == 5: sundays += 1
		
		days += 31	# July
		if days % 7 == 5: sundays += 1
		
		days += 31	# August
		if days % 7 == 5: sundays += 1
		
		days += 30	# September
		if days % 7 == 5: sundays += 1
		
		days += 31	# October
		if days % 7 == 5: sundays += 1
		
		days += 30	# November
		if days % 7 == 5: sundays += 1
		
		days += 31	# December
		if days % 7 == 5: sundays += 1
		
	if days % 7 == 5: sundays -= 1	# now in 2001
	
	return sundays 

if __name__ == "__main__":
	print euler19()

# 1. Add simple doctests that you think will pass
# 2. Add a doctest that fails
# 3. Modify code to pass your  failing doctest
# 4. Add more doctests to test thoroughly
# 5. Modify code as needed to pass doctests

# Note that each time you run, you rerun former dectests:
#  ensuring that new code does not break formerly working code

# Given positive integer n between 7 and 9 digits long,
#  the formated version of n (with commas) is printed
def format_num(n):
		"""
		>>> format_num(123456789)
		123,456,789
		>>> format_num(1123456789)
		1,123,456,789
		>>> format_num(12345678.9)
		123,456,789
		>>> format_num(999999999)
		999,999,999
		>>> format_num(999999998)
		999,999,999

		>>> format_num(103006789)
		103,006,789
		
		>>> format_num(103036789)
		103,036,789
		"""
		ones =n%1000
		temp = n/1000
		thous = temp %1000
		if(thous <1000 and thous >= 100):
			thous= str(thous)	
		elif (thous <100 and thous >= 10):
			thous= "0"+str(thous)
		else:
			thous= "00"+str(thous)
		mils = temp /1000
		print str(mils)+"," +thous+"," +str(ones)


if __name__  == "__main__":
    import doctest
    doctest.testmod()

def is_divisible_by_n (num, divisor):
 	if ((num % divisor)== 0):
		print "Yes!, number "+str(num)+" is divisible by "+ str(divisor)+"."
	else :
		print "No!, number "+str(num)+" is not divisible by "+ str(divisor)+"."

is_divisible_by_n(20, 4)
is_divisible_by_n(21, 8)

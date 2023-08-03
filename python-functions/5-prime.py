def is_prime(number):
	if number <= 3:
		return number>1
	if ((number/number) == 1) | ((number/1) == number):
		return True
	if ((number/number) != 1) | ((number/1) != number):
		return False
	#if number % 2 == 0 or n % 3 == 0 or n % 7 == 0:
        #return False
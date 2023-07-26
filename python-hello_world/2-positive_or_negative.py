# !/usr/bin/python3
# import random
# number = random.randint(-10, 10)
# 
# Check if the number is greater than 0, equal to 0, or less than 0, and print the corresponding message
# if number > 0:
    # print("{} is positive.".format(number))
# elif number == 0:
    # print("0 is zero.")
# else:
    # print("{} is negative.".format(number))

import random
number = random.randint(-10, 10)
# YOUR CODE HERE
a = "is positive"
b = "is negative"
c = "is zero"
if number>0: 
    print(number, a, sep=" ")
if number<0: 
    print(number, b, sep=" ")
if number==0: 
    print(number, c, sep=" ")


    
# !/usr/bin/python3
# import random
# number = random.randint(-10, 10)
# YOUR CODE HERE
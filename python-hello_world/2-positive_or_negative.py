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


    

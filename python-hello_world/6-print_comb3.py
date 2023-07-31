#!/usr/bin/python3

for i in range(45):
    for j in range(46):
      if (i+j) == 89:
        print("{:02}" .format(i+j), end="\n")
      else:
         print("{:02}" .format(i+j), end=", " )
         



        
 
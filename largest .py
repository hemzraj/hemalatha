# Python Program to find Largest of Three Numbers using Elif Statement

e = float(input("Please Enter the First value: "))
f = float(input("Please Enter the First value: "))
g = float(input("Please Enter the First value: "))

if (e > f and e > g):
          print("{0} is Greater Than both {1} and {2}". format(e, f, g))
elif (f > e and f > g):
          print("{0} is Greater Than both {1} and {2}". format(e, f, g))
elif (g > e and g > f):
          print("{0} is Greater Than both {1} and {2}". format(e, f, g))
else:
          print("Either any two values or all the three values are equal")
    
    

Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from math import sqrt
>>> x=2
>>> y=4
>>> print("The product of x and y is ",x*y)
The product of x and y is  8
>>> print("The root of their difference is", sqrt(y-x))
The root of their difference is 1.4142135623730951
>>> print("The root of their difference is"%.2f %sqrt(y-x))
SyntaxError: invalid syntax
>>> print("The root of their difference is %.2f" %sqrt(y-x))
The root of their difference is 1.41
>>> 

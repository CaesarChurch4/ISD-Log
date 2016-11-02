Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:01:18) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print(3+4+5)/3
12
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print(3+4+5)/3
TypeError: unsupported operand type(s) for /: 'NoneType' and 'int'
>>> int(3+4+5)/3
4.0
>>> float(3+4+5)/3
4.0
>>> 

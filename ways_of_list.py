Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> A = [5,6,7,8,9,10,11]
>>> A = A+[12]
>>> 
>>> A = A + [1]
>>> A
[5, 6, 7, 8, 9, 10, 11, 12, 1]
>>> 
>>> A
[5, 6, 7, 8, 9, 10, 11, 12, 1]
>>> A=A+"BCA"
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    A=A+"BCA"
TypeError: can only concatenate list (not "str") to list
>>> A=A+["BCD"]
>>> A
[5, 6, 7, 8, 9, 10, 11, 12, 1, 'BCD']
>>> A=A+list("bcd")
>>> a
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> A
[5, 6, 7, 8, 9, 10, 11, 12, 1, 'BCD', 'b', 'c', 'd']
>>> 
>>> A=A+list(123)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    A=A+list(123)
TypeError: 'int' object is not iterable
>>> A=A+[55664]
>>> A
[5, 6, 7, 8, 9, 10, 11, 12, 1, 'BCD', 'b', 'c', 'd', 55664]
>>> A=A+list(str(123))
>>> A
[5, 6, 7, 8, 9, 10, 11, 12, 1, 'BCD', 'b', 'c', 'd', 55664, '1', '2', '3']
>>> [5, 6, 7, 8, 9, 10, 11, 12, 1, 'BCD', 'b', 'c', 'd', 55664, '1', '2', '3']
[5, 6, 7, 8, 9, 10, 11, 12, 1, 'BCD', 'b', 'c', 'd', 55664, '1', '2', '3']
>>> M
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    M
NameError: name 'M' is not defined
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 


>>> 

>>> 


>>> 
>>> 
>>> 


>>> 

>>> 


>>> 

>>> 


>>> 

>>> 
>>> 
>>> 
>>> 
>>> 
>>> A=[1,2,3,4,5,6]
>>> A=A+

Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_tuple=1,2,3,"a","b",c"
SyntaxError: EOL while scanning string literal
>>> typ
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    typ
NameError: name 'typ' is not defined
>>> 
>>> our_tuple = 1,2,3,"A","B","C"
>>> type(our_tuple)
<class 'tuple'>
>>> our_tuple(0:3)
SyntaxError: invalid syntax
>>> our_tuple[0:3]
(1, 2, 3)
>>> our_tuple[1::2]
(2, 'A', 'C')
>>> our_tuple[3:4]
('A',)
>>> our_tuple[3:5]
('A', 'B')
>>> our_list = [1,2,3,4,5,6]
>>> our_list[2]=100
>>> our_list
[1, 2, 100, 4, 5, 6]
>>> our_list[4]=200
>>> our_list
[1, 2, 100, 4, 200, 6]
>>> our_tuple
(1, 2, 3, 'A', 'B', 'C')
>>> our_tuple[2]=100
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    our_tuple[2]=100
TypeError: 'tuple' object does not support item assignment
>>> A=[1,2,3,4]
>>> tuple(A)
(1, 2, 3, 4)
>>> A
[1, 2, 3, 4]
>>> a
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 1
1
>>> A
[1, 2, 3, 4]
>>> (A,B,C)=1,2,3
>>> A
1
>>> B
2
>>> C
3
>>> 

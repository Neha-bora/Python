Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def add(x,y)
SyntaxError: invalid syntax
>>> def add(x,y):
	return x+y

>>> add(5,7)
12
>>> add(10000000,1)
10000001
>>> 
>>>  def add(x,y):
	print(x+y)
	
SyntaxError: unexpected indent
>>> add(5,4)
9
>>> answer=add(5,8)
>>> 
>>> answer
13
>>> answer
13
>>> 
>>> type(answer)
<class 'int'>
>>> def add(x,y):
	print(x+y)

	
>>> add(6,8)
14
>>> cold = add(5,2)
7
>>> cold
>>> 
>>> 
>>> type(cold)
<class 'NoneType'>
>>> rev="neha"
>>> rev[::-1]
'ahen'
>>> def rev(text)
SyntaxError: invalid syntax
>>> def rev(text):
	return text[::-1]

>>> rev("neha")
'ahen'
>>> rev(ashu)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    rev(ashu)
NameError: name 'ashu' is not defined
>>> rev("ashu")
'uhsa'
>>> rev([1,2,3,4,5])
[5, 4, 3, 2, 1]
>>> 

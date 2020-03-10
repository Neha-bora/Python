Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print(1,2,3,4,5)
1 2 3 4 5
>>> number=[1,2,3,4,5]
>>> print(number)
[1, 2, 3, 4, 5]
>>> print(*number)
1 2 3 4 5
>>> print("abc")
abc
>>> print(*"abc")
a b c
>>> print("a","b","c")
a b c
>>> def add(x,y):
	return x+y
add(10+20)
SyntaxError: invalid syntax
>>> add(10,20)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    add(10,20)
NameError: name 'add' is not defined
>>> def add(x,y):
	return x+y
add(10,10)
SyntaxError: invalid syntax
>>> def add(x , Y):
	return x+y

>>> 
>>> add(10,10)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    add(10,10)
  File "<pyshell#15>", line 2, in add
    return x+y
NameError: name 'y' is not defined
>>> def add(x,y):
	return x+y

>>> 
>>> add(1,5)
6
>>> add(10,10)
20
>>> 
>>> 
>>> def add(*number):
	total=0
	for number in numbers:
		total = total+number

		
>>> def add(*numbers):
	total=0
	for number in numbers:
		total = total + number
		return(total)

	
>>> add(1,2,3,4,5)
1
>>> def add(*number):
	total = 0
	for number in numbers:
		total = total + number
	return(total)

>>> add(10,10,10,10,10)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    add(10,10,10,10,10)
  File "<pyshell#36>", line 3, in add
    for number in numbers:
NameError: name 'numbers' is not defined
>>> def add(*numbers):
	total = 0
	for number in numbers:
		total = total + number
	return(total)

>>> add(10,10,10,10)
40
>>> add(10,100,1000,10000)
11110
>>> 
>>> 
>>> 
>>> def about(name,age,likes):
	sentence="meet {}! they are {} years old and they likes {}".format(name,                    age,likes)
	return sentence

>>> dictionary ={"name":"neha","age":23,"likes":"python"}
>>> about(**dictionary)
'meet neha! they are 23 years old and they likes python'
>>> 

Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def about(name,age,likes):
	sentence = "meet{}!they are{}years old and they like {}".format(name,age,likes)
	return sentence

>>> about("neha",22,"hangout")
'meetneha!they are22years old and they like hangout'
>>> 
>>> 
>>> aboout(age=23,name="jack",likes="python")
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    aboout(age=23,name="jack",likes="python")
NameError: name 'aboout' is not defined
>>> about(age=23,name="jack",likes="python")
'meetjack!they are23years old and they like python'
>>> 
>>> 
>>> about("neha",22)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    about("neha",22)
TypeError: about() missing 1 required positional argument: 'likes'
>>> 
>>> 
>>> def about(name,age,likes):
	sentence = "meet {}!They are {}years old and they like {}".format(name,age,likes)
	return sentence

>>> 
>>> def about(name,age,likes= "java"):
	sentence = "meet{}!they are{}years old and they like {}".format(name,age,likes)
	return sentence

>>> 
>>> about(anju,22)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    about(anju,22)
NameError: name 'anju' is not defined
>>> about("anju",23)
'meetanju!they are23years old and they like java'
>>> about("ashu",18,"nothing")
'meetashu!they are18years old and they like nothing'
>>> 
>>> 
>>> about()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    about()
TypeError: about() missing 2 required positional arguments: 'name' and 'age'
>>> 

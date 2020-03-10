sPython 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> students={}
>>> student={"anju":23,"kajal":22,"neha":21,"ashu":18,"abhishek":20}
>>> student[anju]
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    student[anju]
NameError: name 'anju' is not defined
>>> atudent["anju"]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    atudent["anju"]
NameError: name 'atudent' is not defined
>>> student["anju"]
23
>>> student["sourav"]=20
>>> student["sourav"]
20
>>> del student["sourav"]
>>>  student["sourav"]
 
SyntaxError: unexpected indent
>>> student["sourav"]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    student["sourav"]
KeyError: 'sourav'
>>> students.key()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    students.key()
AttributeError: 'dict' object has no attribute 'key'
>>> student.key()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    student.key()
AttributeError: 'dict' object has no attribute 'key'
>>> student.keys()
dict_keys(['anju', 'kajal', 'neha', 'ashu', 'abhishek'])
>>> student.keys()[2]
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    student.keys()[2]
TypeError: 'dict_keys' object is not subscriptable
>>> a=list(student.keys())
>>> a
['anju', 'kajal', 'neha', 'ashu', 'abhishek']
>>> a[0]
'anju'
>>> a[-1]
'abhishek'
>>> student.values()
dict_values([23, 22, 21, 18, 20])
>>> list(student.value())
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    list(student.value())
AttributeError: 'dict' object has no attribute 'value'
>>> list(student.values())[2:]
[21, 18, 20]
>>> list(student.values())[0::3]
[23, 18]
>>> print(student)
{'anju': 23, 'kajal': 22, 'neha': 21, 'ashu': 18, 'abhishek': 20}
>>> student["abhishek"]
20
>>> studeent[2]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    studeent[2]
NameError: name 'studeent' is not defined
>>> student["kajal"]=21
   student.items()


   

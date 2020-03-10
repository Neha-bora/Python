Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> our_list=[27, 46,73,-87,836,75]
>>> print("our_list")
our_list
>>> print(our_list)
[27, 46, 73, -87, 836, 75]
>>>  type(our_list)
 
SyntaxError: unexpected indent
>>> type(our_list)
<class 'list'>
>>> jackson=["A","B","C",1,2,3, "Do","Rey","Mi",True,False]
>>> jackson[4]
2
>>> jackson[6]
'Do'
>>> jackson[-3]
'Mi'
>>> jackson[-1]
False
>>> x=jackson[6]
>>> 
>>> x = jackson[6]
>>>  jackson[0:3]
 
SyntaxError: unexpected indent
>>> jackson[0:3]
['A', 'B', 'C']
>>> ['A', 'B', 'C']
['A', 'B', 'C']
>>> jackson[3:5]
[1, 2]
>>> jackson[6:9]
['Do', 'Rey', 'Mi']
>>> jackson[6::10]
['Do']
>>> 
>>> 
>>> 
>>> 
>>> 
>>> our_list=[1,2,[3,4,5],6,7,8,9,10]
>>> our_list[3]
6
>>> our_list[3][1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    our_list[3][1]
TypeError: 'int' object is not subscriptable
>>> out_list[2][1]
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    out_list[2][1]
NameError: name 'out_list' is not defined
>>> our_list[2][2]
5
>>> our_list[2][1]
4
>>> our_list[-3]
8
>>> our_list[2][1:]
[4, 5]
>>> our_list[2][0::2]
[3, 5]
>>> our_list[5:7]
[8, 9]
>>> our_list[4::8]
[7]
>>> our_table=[ [1,2,3],[4,5,6],[7,8,9]]
>>> our_table[0]
[1, 2, 3]
>>> our_table[1]
[4, 5, 6]
>>> our_table[2]
[7, 8, 9]
>>> our_table[1]+[2]
[4, 5, 6, 2]
>>> 

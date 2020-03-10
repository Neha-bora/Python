Python 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:21:23) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> even_number=(x for x in range (1,101) if x%2==0)
>>> print(even_number)
<generator object <genexpr> at 0x039348E8>
>>> even_number = [x for x in range (1,101) if x%2==0]
>>> 
>>> even_numbers =[x for x in range (1,101) if x%2 ==0]
>>> print(even_number)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> odd_number=(x for x in range (1,101) if x%2!=0)
>>> print(odd_number)
<generator object <genexpr> at 0x039348E8>
>>> odd_number=[x for x in range (1,101) if x%2!=0]
>>> print(odd_number)
[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59, 61, 63, 65, 67, 69, 71, 73, 75, 77, 79, 81, 83, 85, 87, 89, 91, 93, 95, 97, 99]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> word["anju","neha","kajal","ashu","akash","pooja","abhishek","sourav"]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    word["anju","neha","kajal","ashu","akash","pooja","abhishek","sourav"]
NameError: name 'word' is not defined
>>> word=["anju","neha","kajal","ashu","akash","pooja","abhishek","sourav"]
\
>>> password=[[w.upper(),w.lower(),len(w)]for w in word]
>>> print(password)
[['ANJU', 'anju', 4], ['NEHA', 'neha', 4], ['KAJAL', 'kajal', 5], ['ASHU', 'ashu', 4], ['AKASH', 'akash', 5], ['POOJA', 'pooja', 5], ['ABHISHEK', 'abhishek', 8], ['SOURAV', 'sourav', 6]]
>>> 

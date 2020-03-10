#Ask user for name
name=input("what is your name?:")

#Ask user for age
age=input("how old are you?:")

#Ask user for city
city=input("what city do you live:")

#Ask user what they enjoy
love=input("what do you love doing?:")

#create output text
string= "your name is {}and you r {} year old you r live in {} you love to {}"
output=string.format(name,age,city,love)

#Print output to screen
print(output)                      

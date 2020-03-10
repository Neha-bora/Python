class student:
    def __init__(self,name,school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/ len(self.marks)

class workingstudent(student):
    def __init__(self,name,school,salary):
       super().__init__(name,school)
       self.salary = salary

    def weekly_salary(self):
        return self.salary*37.5

 


neha = workingstudent('neha','JBKP',2000)
print(neha.salary)
neha.marks.append(57)
neha.marks.append(99)
print(neha.average())
print(neha.weekly_salary())


anna = student('anna','oxford',2000)
print(anna.weekly_salary())
        
        

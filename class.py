my_student =  {
    'name':'neha',
    'grade':[70,88,90,99],
    'average': None #something here
    }
def average_grade(student):
    return sum(student['grade'])/len(student['grade'])


class student:
    def __init__(self,new_name,new_grade):
        self.name = new_name
        self.grade = new_grade



    def average(self):
        return sum(self.grade)/len(self.grade)


student_one = student('neha',[70,88,90,99])
student_two = student('kajal',[60,88,40,90])



print(student_one.average())

print(student.average(student_two))

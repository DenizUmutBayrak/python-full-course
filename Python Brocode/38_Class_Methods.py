# Class Methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.

class Student:

    count = 0
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa


#Instance Method
    def get_info(self):
        return f"Name: {self.name}, GPA: {self.gpa}"

    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.total_gpa / cls.count}"

student1 = Student("Spongebob", 3.31)
student2 = Student("Patrick", 2.90)

print(Student.get_count())
print(Student.get_average_gpa())
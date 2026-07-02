class Student:
    def __init__(self,student_id,name,marks):
        self.student_id = student_id
        self.name=  name
        self.marks = marks
    def display_student(self):
        print("student name : ",self.name)
        print("student id : ",self.student_id)
        print("student marks : ",self.marks)
    def update_marks(self,mar):
        self.marks = mar
        return self.marks
    def is_pass(self):
        if self.marks > 35:
            return True
        else:
            return False
S = Student('1','bhavs','36')
S.display_student()
print(S.update_marks(45))
print(S.is_pass())
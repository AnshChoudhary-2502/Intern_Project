class Students:
    def __init__(self):
        self.students = []

    def add_student(self, student_id, name, age):
        student = {'student_id': student_id, 'name': name, 'age': age}
        self.students.append(student)

    def get_students(self):
        return self.students
    

s1 = Students()
s1.add_student(1, 'Alice', 20)
s2 = Students()
s2.add_student(2, 'Bob', 22)
s3 = Students()
s3.add_student(3, 'Charlie', 23)
s4 = Students()
s4.add_student(4, 'David', 21) 
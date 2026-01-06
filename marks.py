class marks:

    def __init__(self):
        self.student = {}

    def add_marks(self , student_id , subject , score):
        if student_id not in self.student:
            self.student[student_id] = {}
            self.student[student_id][subject] = score
        else:
            self.student[student_id][subject] = score
class marks:

    def __init__(self):
        self.student = {}

    def add_marks(self , student_id , subject , score):
        if student_id not in self.student:
            self.student[student_id] = {}
            self.student[student_id][subject] = score
        else:
            self.student[student_id][subject] = score

    def update_marks(self , student_id , subject , score):
        if student_id in self.student and subject in self.student[student_id]:
            self.student[student_id][subject] = score
        else:
            print("Student or subject not found.")

    def get_marks(self , student_id):
        if student_id in self.student:
            return self.student[student_id]
        else:
            print("Student not found.")
            return None
        
    def delete_marks(self , student_id , subject):
        if student_id in self.student and subject in self.student[student_id]:
            del self.student[student_id][subject]
        else:
            print("Student or subject not found.")

    def percentage(self , student_id):
        if student_id in self.student:
            total_score = sum(self.student[student_id].values())
            num_subjects = len(self.student[student_id])
            if num_subjects > 0:
                return (total_score / (num_subjects * 100)) * 100
            else:
                return 0
        else:
            print("Student not found.")
            return None 
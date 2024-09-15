class student:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.courses = []
        self.exam_score = {}

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(scourse)
            course.add_student(self)

    def take_exam(self, exam, score):
        if exam.courese in self.courses:
            slef.exam_scores[exam] = score
            exam.record_score(self.score)


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.students = []
        self.exams = []

    def add_students(self, student):
        if student not in self.students:
            self.student.append(student)
            student.enroll(self)
    
    def add_exam(self, exam):
        if exam not in slef.exams:
            self.exams.append(exam)


class InPerson(Course):
    def __init__(self, course_id, course_name, room_number):
        super().__init__(course_id, course_name)
        slef.room_number = room_number

class Online(Course):
    def __init__(self, course_id, course_name, url):
        super().__init__(course_id, course_name)
        self.url = url


class Exam:
    def __init__(self, exam_id, course):
        self.exam_id = exam_id
        self.course = course
        self.scores = {}

    def record_score(self, student, score):
        if student in self.score.students:
            slef.scores[student] = score




# Example usage
student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

in_person_course = InPerson(201, "Mathematics", "Room 101")
online_course = Online(202, "Physics", "http://example.com/physics")

student1.enroll(in_person_course)
student2.enroll(in_person_course)
student1.enroll(online_course)

math_exam = Exam(301, in_person_course)
physics_exam = Exam(302, online_course)

in_person_course.add_exam(math_exam)
online_course.add_exam(physics_exam)

student1.take_exam(math_exam, 85)
student2.take_exam(math_exam, 90)
student1.take_exam(physics_exam, 95)

# Get all scores for Alice
all_scores = student1.get_all_scores()
print(f"{student1} has the following exam scores:")
for exam, score in all_scores.items():
    print(f"{exam}: {score}")


# Assuming we already have the following setup:
# student1, in_person_course, online_course, math_exam, physics_exam

# Get all scores for Alice
print(f"{student1} has the following exam scores:")
for exam, score in student1.exam_scores.items():
    print(f"Exam ID: {exam.exam_id}, Course: {exam.course.course_name}, Score: {score}")



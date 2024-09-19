class student:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(scourse)
            course.add_student(self)

class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
        self.student = []

    def add_students(self, student):
        if student not in self.students:
            self.student.append(student)
            student.enroll(self)

class InPerson(Course):
    def __init__(self, course_id, course_name, room_number):
        super().__init__(course_id, course_name)
        slef.room_number = room_number

class Online(Course):
    def __init__(self, course_id, course_name, url):
        super().__init__(course_id, course_name)
        self.url = url







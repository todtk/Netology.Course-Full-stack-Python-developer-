students = []
lecturers = []

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def rate(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _average_grade_(self):
        count_grades = 0
        sum_grades = 0
        for list_ in self.grades.values():
            count_grades += len(list_)
            for grade in list_:
                sum_grades += grade
        if count_grades != 0:
            result = sum_grades/count_grades
            return result
        else:
            return 0

    def __str__(self):
        name_ = f"Имя: {self.name}"
        surname_ = f"Фамилия: {self.surname}"
        average_grade_hw = f"Средняя оценка за домашние задания: {round(self._average_grade_(), 2)}"
        courses_in_progress_ = f"Курсы в процессе изучения: {', '.join(self.courses_in_progress)}"
        finished_courses_ = f"Завершенные курсы: {', '.join(self.finished_courses)}"
        result = f"\n{name_}\n{surname_}\n{average_grade_hw}\n{courses_in_progress_}\n{finished_courses_}"
        return result

    def __lt__(self, student):
        if isinstance(student, Student):
            return self._average_grade_() < student._average_grade_()  
        else:
            return 'Ошибка' 
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        lecturers.append(self)

    def _average_grade_(self):
        count_grades = 0
        sum_grades = 0
        for list_ in self.grades.values():
            count_grades += len(list_)
            for grade in list_:
                sum_grades += grade
        if count_grades != 0:
            result = sum_grades/count_grades
            return result
        else:
            return 0

    def __str__(self):
        name_ = f"Имя: {self.name}"
        surname_ = f"Фамилия: {self.surname}"
        average_grade = f"Средняя оценка за лекции: {round(self._average_grade_(), 2)}"
        result = f"\n{name_}\n{surname_}\n{average_grade}"
        return result

    def __lt__(self, lecturer):
        if isinstance(lecturer, Lecturer):
            return self._average_grade_() < lecturer._average_grade_() 
        else:
            return 'Ошибка'          

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        name_ = f"Имя: {self.name}"
        surname_ = f"Фамилия: {self.surname}"
        result = f"\n{name_}\n{surname_}"
        return result

def average_grade_hw(students, cours):
    average_grade = []
    for student in students:
        if cours in student.courses_in_progress or student.finished_courses:
            grades_dict = student.grades
            grades = grades_dict[cours]
            for grade in grades:
                average_grade.append(grade)
    print(round(sum(average_grade)/len(average_grade), 2))
        

def average_grade_lectures(lecturers, cours):
    average_grade = []
    for lecturer in lecturers:
        if cours in lecturer.courses_attached:
            grades_dict = lecturer.grades
            grades = grades_dict[cours]
            for grade in grades:
                average_grade.append(grade)
    print(round(sum(average_grade)/len(average_grade), 2))


some_lecturer = Lecturer('Criss', 'Clever')
some_lecturer.courses_attached += ['Python']

other_lecturer = Lecturer('Pit', 'Clever')
other_lecturer.courses_attached += ['Git']

some_student = Student('Ruoy', 'Eman', 'your_gender')
some_student.courses_in_progress += ['Python']
some_student.finished_courses += ['Введение в программирование']
some_student.rate(some_lecturer, 'Python', 8)

best_student = Student('Billy', 'Butcher', 'your_gender')
best_student.courses_in_progress += ['Python', "Git"]
best_student.finished_courses += ['Введение в программирование']
best_student.rate(some_lecturer, 'Python', 10)
best_student.rate(other_lecturer, 'Git', 10)

some_reviewer = Reviewer('Alex', 'Reader')
some_reviewer.courses_attached += ['Python']
some_reviewer.rate_hw(some_student, 'Python', 6)
some_reviewer.rate_hw(some_student, 'Python', 4)
some_reviewer.rate_hw(some_student, 'Python', 9)
some_reviewer.rate_hw(best_student, 'Python', 10)
some_reviewer.rate_hw(best_student, 'Python', 6)
some_reviewer.rate_hw(best_student, 'Python', 9)

other_reviewer = Reviewer('Todd', 'Reader')
other_reviewer.courses_attached += ['Git']
other_reviewer.rate_hw(best_student, 'Git', 10)
other_reviewer.rate_hw(some_student, 'Git', 8)

print(some_student)
print(best_student)
print(some_lecturer)
print(other_lecturer)
print(some_reviewer)
print(other_reviewer)

print("")
print(some_student < best_student)

print("")
average_grade_hw(students, "Python")

print("")
average_grade_lectures(lecturers, "Python")


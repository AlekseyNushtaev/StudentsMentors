class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        if self.grades == {}:
            return 'Оценок нет'
        else:
            sum_grades = 0
            count_grades = 0
            for key in self.grades:
                sum_grades += sum(self.grades[key])
                count_grades += len(self.grades[key])
            return sum_grades / count_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.average_grade()}\n\
Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}\n'
        return res

    def __lt__(self, another_student):
        if not isinstance(another_student, Student):
            return 'Ошибка'
        return self.average_grade() < another_student.average_grade()


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        if self.grades == {}:
            return 'Оценок нет'
        else:
            sum_grades = 0
            count_grades = 0
            for key in self.grades:
                sum_grades += sum(self.grades[key])
                count_grades += len(self.grades[key])
            return sum_grades / count_grades

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_grade()}\n'
        return res

    def __lt__(self, another_lecturer):
        if not isinstance(another_lecturer, Lecturer):
            return 'Ошибка'
        return self.average_grade() < another_lecturer.average_grade()


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
        res = f'Имя: {self.name}\nФамилия: {self.surname}\n'
        return res


def student_grade(student_list, course):
    student_grades = []
    for student in student_list:
        student_grades += student.grades.get(course)
    res = sum(student_grades)/len(student_grades)
    return res

def lecturer_grade(lecturer_list, course):
    lecturer_grades = []
    for lecturer in lecturer_list:
        lecturer_grades += lecturer.grades.get(course)
    res = sum(lecturer_grades)/len(lecturer_grades)
    return res

student_first = Student('Alexander', 'Pushkin', 'male')
student_first.courses_in_progress = ['Python', 'Java']
student_second = Student('Anna', 'Ahmatova', 'female')
student_second.courses_in_progress = ['Python', 'C++']

lecturer_first = Lecturer('Ivan', 'Bunin')
lecturer_first.courses_attached = ['Python', 'Java']
lecturer_second = Lecturer('Afanasi', 'Phet')
lecturer_second.courses_attached = ['Java', 'C++']

reviewer_first = Reviewer('Mike', 'Lermontov')
reviewer_first.courses_attached = ['Python', 'Java', 'C++']
reviewer_second = Reviewer('Alex', 'Tolstoi')
reviewer_second.courses_attached = ['Python', 'Java', 'C++']

student_first.rate_hw(lecturer_first, 'Python', 5)
student_first.rate_hw(lecturer_first, 'Java', 10)
student_first.rate_hw(lecturer_second, 'Java', 9)
student_second.rate_hw(lecturer_first, 'Python', 10)
student_second.rate_hw(lecturer_first, 'Java', 10)
student_second.rate_hw(lecturer_second, 'C++', 8)

reviewer_first.rate_hw(student_first, 'Python', 3)
reviewer_first.rate_hw(student_first, 'Java', 8)
reviewer_first.rate_hw(student_second, 'Python', 7)
reviewer_first.rate_hw(student_second, 'C++', 4)
reviewer_second.rate_hw(student_first, 'Python', 4)
reviewer_second.rate_hw(student_first, 'Java', 6)
reviewer_second.rate_hw(student_second, 'Python', 9)
reviewer_second.rate_hw(student_second, 'C++', 5)

print(student_first)
print(student_second)
print(lecturer_first)
print(lecturer_second)
print(reviewer_first)
print(reviewer_second)

print(student_first > student_second)
print(lecturer_first < lecturer_second, '\n')

print(student_grade([student_first, student_second], 'Python'))
print(lecturer_grade([lecturer_first, lecturer_second], 'Java'))
class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lec(self, lecturer, lecture, grade):
        if isinstance(lecturer, Lecturer) and lecture in lecturer.courses_attached:
            if lecture in lecturer.grades:
                lecturer.grades[lecture] += [grade]
            else:
                lecturer.grades[lecture] = [grade]
        else:
            return 'Ошибка'

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating


    def __str__(self):
        return f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {self.aver_grade()}\n'
        f'Курсы в процессе изучения: {",".join(self.courses_in_progress)}\n'
        f'Завершенные курсы: {",".join(self.finished_courses)}'


    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Преподавателей и студентов между собой не сравнивают!")
            return
        return self.av_rating() < other.av_rating()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name, surname)
        self.courses_attached = []
        self.grades = {}

    def av_rating(self):
        sum_rating = 0
        len_rating = 0
        for course in self.grades.values():
            sum_rating += sum(course)
            len_rating += len(course)
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def av_rating_for_course(self, course):
        sum_rating = 0
        len_rating = 0
        for lesson in self.grades.keys():
            if lesson == course:
                sum_rating += sum(self.grades[course])
                len_rating += len(self.grades[course])
        average_rating = round(sum_rating / len_rating, 2)
        return average_rating

    def __str__(self):
        aver_grade_lec = numpy.average()
        return f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}\n'
        f'Средняя оценка за лекции: {self.aver_grade_lec}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Преподователей и студентов между собой не сравнивают!")
            return
        return self.av_rating() < other.av_rating()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(self, name, surname)

    def __str__(self):
        return f'Имя: {self.name}\n'
        f'Фамилия: {self.surname}'


    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# best_student = Student('Ruoy', 'Eman', 'your_gender')
# best_student.courses_in_progress += ['Python']
#
# cool_mentor = Mentor('Some', 'Buddy')
# cool_mentor.courses_attached += ['Python']
#
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
# cool_mentor.rate_hw(best_student, 'Python', 10)
#
# print(best_student.grades)

# Студенты
student_1 = Student('Игорь', 'Игорев', 'Муж')
student_1.courses_in_progress += ['Python']
student_1.finished_courses += ["Введение в програмирование"]

student_2 = Student('Светлана', 'Светкина', 'Жен')
student_2.courses_in_progress += ['Python']
student_2.finished_courses += ["Введение в програмирование"]

# Лекторы
lecturer_1 = Lecturer('Олег', 'Олегов')
lecturer_1.courses_attached += ['Python']

lecturer_2 = Lecturer('Ирина', 'Иринова')
lecturer_2.courses_attached += ['Python']

# Проверяющие
reviewer_1 = Reviewer('Сергей', 'Сергеев')
reviewer_1.courses_attached += ['Python']

reviewer_2 = Reviewer('Ольга', 'Ольгова')
reviewer_2.courses_attached += ['Python']

# Оценки студентам
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Python', 7)

reviewer_2.rate_hw(student_2, 'Python', 10)
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 9)

# Оценки лекторам
student_1.rate_lw(lecturer_1, 'Python', 10)
student_1.rate_lw(lecturer_1, 'Python', 8)
student_1.rate_lw(lecturer_1, 'Python', 6)

student_2.rate_lw(lecturer_2, 'Python', 10)
student_2.rate_lw(lecturer_2, 'Python', 6)
student_2.rate_lw(lecturer_2, 'Python', 6)

student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]
reviewer_list = [reviewer_1, reviewer_2]


def average_rating_for_course(course, student_list):
    sum_rating = 0
    quantity_rating = 0
    for stud in student_list:
        for course in stud.grades:
            stud_sum_rating = stud.av_rating_for_course(course)
            sum_rating += stud_sum_rating
            quantity_rating += 1
    average_rating = round(sum_rating / quantity_rating, 2)
    return average_rating


print(average_rating_for_course('Python', student_list))
print(average_rating_for_course('Python', lecturer_list))
print(student_1)
print(student_2)
print(lecturer_1)
print(lecturer_2)

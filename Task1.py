def obj_average_rate(object_grades):
    aver_rate = int(sum(object_grades)/len(object_grades) *10) /10
    return aver_rate

def all_average_rate(person):
    aver_rate = 0
    for obj in person.grades: #цикл по ключам словаря
        aver_rate += obj_average_rate(person.grades[obj])
    if len(person.grades) != 0:
        aver_rate = aver_rate / len(person.grades)
    else:
        aver_rate = 0
    return aver_rate

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecture(self, lec, course, grade):
            if (isinstance(lec, Lecturer) and (course in self.courses_in_progress or course in self.finished_courses) and
                course in lec.courses_attached and grade in range(11)):
                if course in lec.grades:
                    lec.grades[course] += [grade]
                else:
                    lec.grades[course] = [grade]
            else:
                return "Ошибка"

    def __str__(self):
        aver_rate = all_average_rate(self)
        str1 = ""
        str2 = ""
        for course in self.courses_in_progress:
            str1 += (", " + course)
        for course in self.finished_courses:
            str2 += (", " + course)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания : {aver_rate}\nКурсы в процессе изучения: {str1[2:]}\nЗавершенные курсы: {str2[2:]}"

    def __lt__(self, other):
        return all_average_rate(self) < all_average_rate(other)
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
            aver_rate = all_average_rate(self)
            return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {aver_rate}"

class Reviewer(Mentor):
    def rate(self, student, course, grade):
            if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

    def __lt__(self, other):
        return all_average_rate(self) < all_average_rate(other)

    def __gt__(self, other):
            return all_average_rate(self) > all_average_rate(other)

    def __eq__(self, other):
            return all_average_rate(self) = all_average_rate(other)
    
# # # # # 2
lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
reviewer.courses_attached += ['Python', 'C++']
student = Student('Алёхина', 'Ольга', 'Ж')
st = Student('Марина', 'Симонова', 'Ж')
 
student.courses_in_progress += ['Python', 'Java', 'C++']
student.finished_courses += ['Введение']
st.courses_in_progress += ['Python', 'Java']
st.finished_courses += ['C++', 'Введение']
reviewer.rate(st, 'Python', 5)
reviewer.rate(st, 'Python', 3)
reviewer.rate(student, 'C++', 10)
reviewer.rate(student, 'Python', 2)
# lecturer.courses_attached += ['Python', 'C++']
# lecturer.courses_attached += ['Java']
# reviewer.courses_attached += ['Python', 'C++']

# student.rate_lecture(lecturer, 'Python', 10)
# student.rate_lecture(lecturer, 'Python', 5)
# student.rate_lecture(lecturer, 'Python', 10)

# print(student.rate_lecture(lecturer, 'Python', 10))   # None
# print(student.rate_lecture(lecturer, 'Java', 8))     # Ошибка
# print(student.rate_lecture(lecturer, 'С++', 8))      # Ошибка
# print(student.rate_lecture(reviewer, 'Python', 6))   # Ошибка
 
# print(lecturer.grades)  # {'Python': [7]}  
# print(lecturer.courses_attached)
# aver_rate = 0.3
# print(f"Имя: {st.name}\nФамилия: {st.surname}\nСредняя оценка за лекции: {aver_rate}\nКурсы в процессе изучения: {st.courses_in_progress}\nЗавершенные курсы: {st.finished_courses}")
print(st<student)
# # # # # 0
# best_student = Student("Ivan", "Petrov", "gender1")
# best_student.finished_courses += ["Git"]
# best_student.courses_in_progress += ["Python"]
# # best_student.grades["Git"] = [10,10,10,8,9]
# # best_student.grades["Python"] = [10,10]

# # print(best_student.finished_courses)
# # print(best_student.courses_in_progress)
# # print(best_student.grades)

# cool_mentor = Mentor("Imentor","Mysurname")
# cool_mentor.courses_attached += ["Python"]
# # print(cool_mentor.courses_attached)

# cool_mentor.rate(best_student, "Python", 5)
# cool_mentor.rate(best_student, "Git", 10)
# cool_mentor.rate(best_student, "Python", 10)
# print(best_student.grades)

# # # # # 1
# lecturer = Lecturer('Иван', 'Иванов')
# reviewer = Reviewer('Пётр', 'Петров')
# print(isinstance(lecturer, Mentor)) # True
# print(isinstance(reviewer, Mentor)) # True
# print(lecturer.courses_attached)    # []
# print(reviewer.courses_attached)
# A software academy teaches two types of courses:
# - local courses that are held in some of the academy’s local labs and
# - offsite courses held in some other town outside of the academy’s headquarters.
# Each course has a name, a teacher assigned to teach it and a course program (sequence of topics).
# Each teacher has a name and knows the courses he or she teaches.
# Both courses and teachers could be printed in human-readable text form.
# All your courses should implement ICourse.
# Teachers should implement ITeacher.
# Local and offsite courses should implement ILocalCourse and IOffsiteCourse respectively.
# Courses and teachers should be created only through the ICourseFactory interface
# implemented by a class named CourseFactory.
# Write a program that will form courses of software academy.

# from abc import ABC, abstractmethod


class ICourse:
    def __init__(self, name, teacher):
        self.name = name
        self.teacher = teacher
        self.program = []

    def __getattr__(self, atr_name):
        return 'Something wrong...'

    def __setattr__(self, attr_name, attr_value):
        self.__dict__[attr_name] = attr_value

    def add_program(self, topic):
        self.program.append(topic)

    def add_teacher(self, teacher):
        self.teacher = teacher


class ITeacher:
    def __init__(self, name):
        self.name = name
        self.courses = []

    def __getattr__(self, atr_name):
        return 'Something wrong...'

    def __setattr__(self, attr_name, attr_value):
        self.__dict__[attr_name] = attr_value

    def add_course(self, course):
        self.courses.append(course)


class LocalCourse(ICourse):
    def __init__(self, name, teacher, lab):
        super().__init__(name, teacher)
        self.lab = lab


class OffsiteCourse(ICourse):
    def __init__(self, name, teacher, town):
        super().__init__(name, teacher)
        self.town = town


class ICourseFactory:
    def create_teacher(self, name):
        pass

    def create_local_course(self, name, teacher: ITeacher, lab):
        pass

    def create_offsite_course(self, name, teacher: ITeacher, town):
        pass


class CourseFactory(ICourseFactory):
    def create_teacher(self, name):
        return ITeacher(name)

    def create_local_course(self, name, teacher: ITeacher, lab):
        return LocalCourse(name, teacher, lab)

    def create_offsite_course(self, name, teacher: ITeacher, town):
        return OffsiteCourse(name, teacher, town)


factory = CourseFactory()
shevchenko = factory.create_teacher("Oleg Shevchenko")

python = factory.create_local_course("python", shevchenko, "lab1")
python.add_program("Introduction to Python")
python.add_program("Types and Values")
python.add_program("Classes")

cpp = factory.create_offsite_course("C++", shevchenko, "Kyiv")
cpp.add_program("Types and Values")
cpp.add_program("Functions")
cpp.add_program("Functions-II")

shevchenko.add_course(python)
shevchenko.add_course(cpp)

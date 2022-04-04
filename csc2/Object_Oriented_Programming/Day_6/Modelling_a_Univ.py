class Course:
    def __init__(self, subject, number):
        self.subject = subject
        self.number = str(number)

    @property
    def subject(self):
        return self._subject

    @subject.setter
    def subject(self, value):
        self._subject = value

    @property 
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        self._number = value

    def __str__(self):
        return f"{self.subject},{self.number}"


class Schedule:
    def __init__(self, courses=[]):
        self.courses = courses

    @property # decorator for getter
    def courses(self):
        return self._courses

    @courses.setter
    def courses (self, new_courses):
        self._courses = new_courses

    def add_course (self, course):
        self._courses.append (course)

    def drop_course (self, course):
        if course in self._courses:
            self._courses.remove (course)

    def __str__(self):
        result = ''
        for course in self._courses:
            result += f"\n{course}"
        if result == '':
            return "No classes scheduled."
        return result


class Person:
    current_id = 1234

    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year 
        self.schedule = Schedule()
        self.id = Person.current_id
        Person.current_id += 1

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property 
    def birth_year(self):
        return self._birth_year

    @birth_year.setter
    def birth_year(self, value):
        if not hasattr (self, "_birth_year"):
            self._birth_year = "ERROR"
        if 1500 < int(value) < 2022:
            self._birth_year = value

    @property 
    def schedule(self):
        return self._schedule

    @schedule.setter
    def schedule(self, value):
        self._schedule = value

    @property 
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if hasattr (self, '_id'):
            raise PermissionError
        self._id = value

    def view_schedule (self):
        return ("{self.name}'s Schedule: \n{self.schedule.__str__()}")

    def __str__(self):
        return (f"Name: {self.name}\nBirth Year: {self.birth_year}\nID: {self.birth_year}")
    

class Student (Person):
    def __init__ (self, name, birth_year, major):
        # two ways to call super class
        # super ().__init__(name, birth_year)
        Person.__init__(self, name, birth_year)
        self.major = major

    @property
    def major(self):
        return self._major

    @major.setter
    def major (self, value):
        self._major = value

    def __str__(self):
        return super().__str__() + f"\nRole: Student\nMajor: {self.major}"

class Faculty (Person):
    def __init__ (self, name, birth_year, department):
        # two ways to call super class
        # super ().__init__(name, birth_year)
        Person.__init__(self, name, birth_year)
        self.department = department

    @property
    def department(self):
        return self._department
    @department.setter
    def department (self, value):
        self._department = value

    def __str__(self):
        return super().__str__() + f"\nRole: Faculty\nDepartment: {self.department}"


p1 = Student ("Samuel Noel", "2006", "Undeclared")
p2 = Faculty ("You John", "2030", "Agriculture")

c1 = Course ("AGRI", "212")
c2 = Course ("BIOB", "702")

print (f"{p1} \n {p2}")
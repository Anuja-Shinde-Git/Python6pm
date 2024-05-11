# Inheritance

# single inheritance

# program 1

# parent wiht constructor, child without constructor

class Student:
    def __init__(self,fn,ln,adharno):
        self.firstname = fn
        self.lastname = ln
        self.adharno = adharno

    def displayName(self):
        print(self.firstname+self.lastname)

class Teacher(Student):
    salary = 10000

    def displaySalary(self):
        print(self.salary)

sanket = Teacher("sanket","shinde",1234)

print(sanket.firstname)
print(sanket.lastname)
print(sanket.adharno)
print(sanket.salary)

sanket.displayName()
sanket.displaySalary()

# program 2

class Student:

    def __init__(self,fn,ln,adharno):
        self.firstname = fn
        self.lastname = ln
        self.adharno = adharno

    def displayName(self):
        print(self.firstname+self.lastname)

class Teacher(Student):

    def __init__(self, fn, ln,adharno,salary):
        super().__init__(fn, ln,adharno)
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

sanket = Teacher("sanket","shinde",1234,123456)

print(sanket.firstname)
print(sanket.lastname)
print(sanket.adharno)
print(sanket.salary)

sanket.displayName()
sanket.displaySalary()

# program 3 

# multi-level inheritance

class Student:

    def __init__(self,fn,ln,adharno):
        self.firstname = fn
        self.lastname = ln
        self.adharno = adharno

    def displayName(self):
        print(self.firstname+self.lastname)

class Teacher(Student):

    def __init__(self, fn, ln, adharno,salary):
        super().__init__(fn, ln, adharno)   
        self.salary = salary

    def displaySalary(self):
        print(self.salary)

class Professor(Teacher):

    def __init__(self, fn, ln, adharno, salary,spec):
        super().__init__(fn, ln, adharno, salary)  
        self.specialization = spec

    def displaySpecialization(self):
        print(self.specialization)

sanket = Professor("sanket","shinde",1234,123456,"xyz")

print(sanket.firstname)
print(sanket.lastname)
print(sanket.adharno)
print(sanket.salary)
print(sanket.specialization)

sanket.displayName()
sanket.displaySalary()
sanket.displaySpecialization()




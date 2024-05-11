# Program 1
# class with instance method 

class Person:
    # constructor
    def __init__(self,fn,ln):
        # instance variable
        self.firstname = fn
        self.lastname = ln
    # instance method
    def displayName(self):
        print(self.firstname+self.lastname)    

    def UpdateLname(self,ln):
        self.lastname = ln

chaitali = Person("chaitali","dongare")
print(chaitali.firstname)
print(chaitali.lastname)
chaitali.displayName()

chaitali.UpdateLname("borade")

print(chaitali.lastname)

# program 2 

# class with class method

class PersonB:
    # class varible
    country = "INDIA"

    # constructor
    def __init__(self,fn,ln):

        # instance varible
        self.firstname = fn
        self.lastname = ln

    #   instance method
    def displayName(self):
        print(self.firstname+self.lastname)    

    def UpdateFname(self,fn):
        self.firstname = fn
    
    # class method
    @classmethod 
    def UpdateCountry(cls,cnty):
        cls.country = cnty

s = PersonB("sanket","shinde")

print(s.firstname)
print(s.lastname)
print(s.country)

# instance varible updated
s.country = "BHARAT"

a = PersonB("aniket","shinde")

print(a.country)

# class method called on class
PersonB.UpdateCountry("INDIA B")

print(s.country)
print(a.country)

# program 3

# static method
# count the number of object

# in stacti method to count no. of object define count = 0 in class 
# while set properties define  PersonC.count = PersonC.count + 1

class PersonC:

    count = 0
    country = "BHARAT"

    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln
        PersonC.count = PersonC.count + 1
    
    def displayName(self):
        print(self.firstname+self.lastname)

    @classmethod
    def UpdateCountry(cls,cnty):
        cls.country = cnty

    @staticmethod
    def countObj():
        return PersonC.count

sanket = PersonC("sanket","shinde")
aniket = PersonC("aniket","shinde")

# call object on count method and store  in varible

a = PersonC.countObj()

print(a)

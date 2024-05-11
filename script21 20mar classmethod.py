# program 1

class Person:
    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    # instancec method
    def disaplayName(self):
        print(self.firstname+' '+self.lastname)

sanket = Person("sanket","shinde")
aniket = Person("aniket","shinde")

print(sanket.firstname)
print(sanket.lastname)
print(aniket.firstname)
print(aniket.lastname)

sanket.disaplayName()
aniket.disaplayName()


# class method and class varible

# class variable is set befor constructor declaration. for all object created the value of class varible remain common.
# if the value updated later for instance reference object then that object refers updated value and no longer refers to commaon value
# remaining object refers common class variable.

# class method is used to update or set values for whole class. value is set within class using @classmethod and then all the objects
# follows updated value

# program 2

class Person2 :
    # class variable
    country = 'BHARAT'

    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    #   instance method
    def displyaname(self):
        print(self.firstname+' '+self.lastname)

sanket = Person2("sanket","shinde")
aniket = Person2("aniket","shinde")

# class variable value will call "BHARAT" for both the objects
print(sanket.country)
print(aniket.country)

# updated value for country instance variable 
sanket.country = 'INDIA'
# instance variable value will call only for current reference object i.e for sanket not for aniket
print(sanket.country)
print(aniket.country)

# now want to update country value for whole class using @classmethod
# class method is always called on class

# program 3

class Person3:
    #  class variable
    country = "BHARAT"

    def __init__(self,fn,ln):
      self.firstname = fn
      self.lastname = ln 

    def displayName(self):
        print(self.firstname+' '+self.lastname)
    
    # class method
    @classmethod
    def changeCountry(cls,cnty):
        cls.country = cnty

sanket = Person3("sanket","shinde") 
aniket = Person3("aniket","shinde")
sai = Person3("sai","shinde")

# class variable called
print(sanket.country)
print(aniket.country)
print(sai.country)

# instance variable
sai.country = "Hindustan"
print(sai.country)

# class method called to update country value always on class>>Person3
# value will update only for sanket and aniket not for sai as refernce variable already referes sai

Person3.changeCountry("INDIA")

print(sanket.country)
print(aniket.country)
print(sai.country)






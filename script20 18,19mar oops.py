# Inheritance

# program 1

class Person:
    # fields or properties
    first_name = "sai"
    last_name = "shinde"
    
    # instance method
    def walk(self):
        print('i am walking')

    def talk(self):
        print('i am talking')

sai = Person()
print(sai.first_name)
print(sai.last_name)

sai.walk()
sai.talk()

# on this reference variable(sai) above 4 this are available two properties and two methods

# now created new reference variable (amol) the same properties and methods are available for this but for the firstname and
# lastname will be the same as 1st one so we need to update that valuse

amol = Person()
amol.first_name = "amol"
amol.last_name = "rao"

print(amol.first_name)
print(amol.last_name)

# but this not good practise everytime we need to updates values so this in case we are using inheritance
# we will set class properties while creating object using constructor

# program 2 

class PersonB:

    # constructor
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def walk(self):
        print('I am walking') 

    def talk(self):
        print('I am talking')

# when we create object constructor will call and we have to set values in constructor here fn and ln
        
sanket = PersonB("sanket","shinde")
aniket = PersonB("aniket","shinde")

print(sanket.firstname)
print(sanket.lastname)

print(aniket.firstname)
print(aniket.lastname)

# here out of class we can set one more property for current object
aniket.city = 'Tuljapur'

print(aniket.city)

# print(sanket.city)   this will give error as only set for aniket object ie instance variable

sanket.walk()
sanket.talk()

aniket.walk()
aniket.talk()

#Assignment
# Vehicle 
# type model
# start() , stop()

# program 3

class Vehical:
    def __init__(self,type,model):
        self.type = type
        self.model = model

    def start(self):
        print('start:'+self.type+' '+self.model)

    def stop(self):
        print('stop:'+self.type+' '+self.model)
        
activa = Vehical("two wheeler","6g")
thar = Vehical("four wheeler","4x4")           

print(activa.type)
print(activa.model)

print(thar.type)
print(thar.model)

activa.start()
activa.stop()

thar.start()
thar.stop()

 

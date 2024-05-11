# Polymorphism >> takes place where same method is used to do more than one operation

# 1. method overloading
# 2. duck typing
# 3. operator overloading
# 4. method overriding

# method overloading

# program 1

class Calculator:
    def addition(self,x,y):
        print(x+y)

    def addition(self,x,y,z):
        print(x+y+z)

    def addition(self,x,y,z,a):
        print(x+y+z+a)

cc = Calculator()

# cc.addition(12,3)
# TypeError: Calculator.addition() missing 2 required positional arguments: 'z' and 'a'
# cc.addition(12,3,4)
# TypeError: Calculator.addition() missing 1 required positional argument: 'a'

cc.addition(12,3,4,5)
# python will consider lastly updated method only when all the 4 reference variable present 

# so overcome this method overloading takes place

# program 2

class Calculator:

    def addition(self, x = None, y = None, z = None, a = None):
        if x != None and y != None and z != None and a != None:
            print(x+y+z+a)

        elif x != None and y != None and z != None:
            print(x+y+z)

        elif x != None and y != None :
            print(x+y)
      
cc = Calculator()

cc.addition(12,3)
cc.addition(12,3,4)
cc.addition(12,3,4,5)


# Duck typing

class Dog:

    def talk(self):
        print("bow bow")

class Human:

    def talk(self):
        print("hi hello")

def call_talk(obj):
    obj.talk()

d = Dog()
h = Human()

call_talk(d)
call_talk(h)

# strong typing

class Dog:
    def talk(self):
        print("bow bow")

class Human:
    def talk(self):
        print("hi hello")

class Duck:
    def sound(self):
        print("quack quack")

def call_talk(obj):
    if hasattr(obj,'talk'):
        obj.talk()
    else:
        obj.sound()

a = Dog()
b = Human()
c = Duck()

call_talk(a)
call_talk(b)
call_talk(c)


# operator overloading

# add operator acts differently with each data type
print("hello"+"hi")
print(11+11)
print([11,22,33],[44,55,66])


class BookA:
    def __init__(self,pg):
        self.pages = pg

class BookB:
    def __init__(self,pg):
        self.pages = pg

ramayan = BookA(200)
mahabharat = BookB(100) 

print(ramayan.pages+mahabharat.pages)

# here we add pages of books using add operator but we can add directly objects and perform same operation using
# operator overloading

class BookA:
    def __init__(self,pg):
        self.pages = pg

class BookB:
    def __init__(self,pg):
        self.pages = pg

    def __add__(self,other):
        return(self.pages+other.pages)

ramayan = BookA(200)
mahabharat = BookB(100)

print(mahabharat+ramayan)

# here we introduce __add__ method in class BookB i.e. for mahabharat so here mahabharat is going to add in ramayan
# if we want to add ramayan in mahabharat we have to introduce __add__ method is class BookA ramayan


print(4 > 2)

class BookX:
    def __init__(self,pg):
        self.pages = pg

    def __gt__(self,other):
        return(self.pages > other.pages)
    
class BookY:
    def __init__(self,pg):
        self.pages = pg

ramayan = BookX(200)
mahabharat = BookY(100)

print(ramayan > mahabharat)

# here o/p is boolean, we introduce __gt__ method ie. greater than in class BookX(ramayan)


# method overriding
# in method overriding inherited methods are not called rather than that actual/ current class methods are called

# class WorldBank:
#     def loan(self):
#         print("I am loan from WB")

#     def save(self):
#         print("I am save from WB")

# class SBI(WorldBank):
#     def loan(self):
#         print("I am loan from SBI")

#     def save(self):
#         print("I am save from SBI")

# class PNB(WorldBank):
#     def loan(self):
#         print("I am loan from PNB")

#     def save(self):
#         print("I am save from PNB")

# pune = SBI()
# nagpur = PNB()

# pune.loan()

# nagpur.save()


# In this program we inherited paraent class and user super method in child class so that parent class method also called and child class method 
# both the methods called

class WorkBank:
    def loan(self):
        print("I am loan from WB")
    def save(self):
        print('I am save from WB')

class SBI(WorkBank):
    def loan(self):
        print("I am loan from SBI")
        super().loan()
    def save(self):
        print('I am save from SBI')
        super().save()
    

class PNB(WorkBank):
    def loan(self):
        print("I am loan from SBI")
        super().loan()
    def save(self):
        print('I am save from SBI')
        super().save()
      
a = SBI()
a.loan()
a.save()
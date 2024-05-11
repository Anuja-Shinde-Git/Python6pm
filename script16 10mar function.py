# functions
# integer as parameter integer as return type

def add(x,y):
    return x+y
e = add(2,3)
print(e)


# float as parameter float as return type

def add(x,y):
    return x+y
e = add(12.3,54.6)
print(e)


# boolean as parameter boolean as return type

def canDrive(age,haveVehicle):
    if age > 18 and haveVehicle:
        return True
    else:
        return False
g = canDrive(19,True)
print(g)    


# string as parameter string as return type

def greet(name):
    return('welcome' + name)
j = greet("aashish")
print(j)


# list as parameter list as return type

names= ['ram','laxman','bharat','shatrughn']
def addName(lst):
    lst.append('hanuman')
    return lst
k = addName(names)
print(k)        


# dictionary as parameter dictionary as return type

info = {
    "firstName" : "ram",
    "lastName" : "suryawanshi",
    
}

def addCity(info):
    info['city'] = "ayodhya"
    return info
l = addCity(info)
print(l)


# tuple as parameter tuple as return type

numbers = (111,22,33,44)
def addValue(tupA):
    tupA = list(tupA)
    tupA.append(55)
    tupA = tuple(tupA)
    return tupA
l = addValue(numbers)
print(l)


# set as parameter set as return type

setA = {11,22,33}
def addElement(seta):
    seta.add(44)
    return seta
z = addElement(setA)
print(z)
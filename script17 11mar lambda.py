# lambda function 

def addA(x,y):
    return x+y
e = addA(4,5)
print(e)

add=lambda x,y:x+y
f = add(5,6)
print(f)

# program 2

e=lambda x:x*x
print(e(5))

# program 3

def addition(x,y):
    return x+y
print(addition(2,4))

# function as parameter to another function
add = lambda x,y:x+y
def addition(fn,x,y):
    # fn = add = lambda x,y:x+y
    f = fn(x,y)
    return f
e2 = addition(add,3,4)
print(e2)

sub = lambda x,y : x-y
def subtraction(fn,x,y):
    h = fn(x,y)
    return h
e3 = subtraction(sub,5,4)
print(e3)


# program 4
# function as parameter function as return type

def add():
    return lambda x,y:x+y
e = add()
print(e)
e2 = e(4,7)
print(e2)
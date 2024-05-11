# compile time error

# program 1

# def add():
# print(2+3)  

# run time error

# print('hello')
# e = int(input('enter numberA'))
# f = int(input('enter numberB'))
# print(e/f)
# print('bye')

#     print(e/f)
#           ~^~
# ZeroDivisionError: division by zero

# print('hello')
# numbers = [11,22,33,44,55,66]
# print(numbers[6])
# print('bye')

#     print(numbers[6])
#           ~~~~~~~^^^
# IndexError: list index out of range

# logical error

def CalculateBounceSalary(amount):
    return amount * 0.10 + amount
print(CalculateBounceSalary(10000))

# in below case logical error occures
def CalculateBounceSalary(amount):
    return amount * 0.10 
print(CalculateBounceSalary(10000))


# program 2 

# print('hello')
# try:
#     e = int(input('enter numberA'))
#     f = int(input('enter numberB'))
#     print(e/f)
# except Exception:
#     print('please enter correct input')
# print('bye')        


# try except else finally

# program 3

# print('hello')
# names = ['ketaki','hindavi','shivani','durga','shrija']
# try:
#     e = int(input('enter numberA'))
#     f = int(input('enter numberB'))
#     print(e/f)
#     print(names[8])
# except ArithmeticError:
#     print('please enter correct input')
# except IndexError:
#     print('add more elements to list')
# except Exception:
#     print('please correct the value')
# print('bye')                

# in above code we introduced 3 exception
# arithmatic error for invalid input ie. for divison error if numberB is 0
# index error for out of range index
# exception as generic exception for invalid input

# if you entered numberB as 0 then 1st exception will raise and lastly bye will print
# if you enter out of range index 2nd exception will raise and lastly bye will print
# if you entered invalid input 3rd exception will raise and lastly bye will print

# program 4

# finally block will always execute if exception raised or not it will always exceute
# print('hello')
# try:
#     e = int(input('enter numberA'))
#     f = int(input('enter numberB'))
#     print(e/f)
# except ArithmeticError:
#     print('enter correct input')
# finally:
#     print('I will always execute')
# print('bye')            

# program 5

print('hello')
try:
    e = int(input('enter numberA'))
    f = int(input('entrt numberB'))
    print(e/f)
except ArithmeticError:
    print('please enter correct input')
else:
    print('hello I will run')
finally:
    print('I will always execute')
print('bye')                

# if exception not raised then else block executes if exception raised flow goes to finally block
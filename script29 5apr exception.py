# A single try block can be followed by several except block >> TRUE
# multiple except blocks can be used to handle multiple exception >> TRUE
# we cannot write except block without try block >> TRUE
# we cannot write try block without except block >> FALSE
# Else block and finally block are not compulsory >> TRUE
# When there is no exception raised else block is executed after try block  >>  FALSE 
# Finally block is always executed >> TRUE

# program 1

# try:
#     names = ["sarika","poorva","sharddha"]
#     a = int(input('Enter numberA'))
#     b = int(input('Enter numberB'))
#     print(a/b)
#     print(names[4])
# except ArithmeticError:
#     print('please enter correct input')
# except IndexError:
#     print('please add more values to list')        

# program 2

# we can write try block without except block 
# in below code after try block finally block will execute, here exception raised but finally block will always execute
# and after that exception displayed but exception handled so next code will not executed program haulted.

# print('hello')
# try:
#     print(34/0) 
# finally:
#     print('I will always execute')
# print('bye')        

# program 3

# def calAvg(list):
#     # [11,22,33][4]
#     total = 0
#     for item in list:
#         total = total + item
#     avg = total/len(list) 
#     return total,avg
# try:
#     a,b = calAvg([1,2,3,'a'])
#     print(a)
#     print(b)
# except TypeError:
#     print('enter the correct input')
# except ZeroDivisionError:
#     print('Arithmetic execetion, enter correct value')
# except Exception:
#     print('please enter correct input')              

# program 4
# Assertion 

print('hello')
try:
    x = 18
    assert x > 1 and x <= 9
    print(x)
except AssertionError:
    print('condition not matched')
print('bye')          


# program 5

class lowbalance(Exception):
    def __init__(self,msg):
        self.msg = msg

def check(dict):
    for k,v in dict.items():
        if(v < 20000):
            raise lowbalance('Balance is low')
try:
    names = {'snehal':10000,'hrushali':40000,'ninad': 388888,'chinmay':355}
    check(names)
    check(names)
except lowbalance as msg:
    print(msg)                    
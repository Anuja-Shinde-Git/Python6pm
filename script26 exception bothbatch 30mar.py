# Exception Handling

# 1. compile time error >> syntax error

# def addition(x,y):
# print(x+y)
# addition(12,3)    

# in above example  IndentationError in print statement , print should be inside the function this error is syntax error i.e. compile time error


# 2. run time error >> error depends on user input , we can not predict user input in that case error raised called run time error

# x= int(input("enter the number one "))
# y = int(input("enter the number two "))
# print(x/y)
# print("bye")

# in above code if we give input as 10 and 0 respectively ZeroDivisionError: division by zero error raised and code terminates 
# and next block will not run
# we can not predict input from user


# 3. logical error

# want o/p as amount plus 10 percent of amount

def add10Pr(amount):
    return amount * 0.10 + amount
e = add10Pr(100)
print(e)

# get o/p as 110 but what if coder forget to add amount i.e.

def add10Pr(amount):
    return amount * 0.10 
e = add10Pr(100)
print(e)

# it returns only 10 percent value so this is logical error introduced by coder(human error) while code building

# from all above errors in run time error we can not predict input by user so we can manage this error using 
# exception handling with try: except: blocks

# program 1

print("hello")
try:
   x= int(input('enter the numberA '))
   y = int(input('enter the numberB '))
   print(x/y)
except Exception:
    print('invalid input')   
print('bye')    

# case 1
# hello will print
# try block >> numberA 10 >> numberB 5 >> flow does not go to except block
# bye will print

# case 2
# hello will print
# try block >> numberA 10 >> numberB 0 >> flow goes to except block and error will caught in line 27
# exception raised and handled and invalid input statement will print
# lastly bye will print

# there are two types of exceptions
# 1. inbulit exception
# 2. user defined exception
# both the exception are derived by one class one parent class that is Exception

# in above code we stated exception as exception >> not defined any specified exception



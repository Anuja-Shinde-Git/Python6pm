# 28 feb 2024

x = 10
print(x)

first_name = "akshay"
print(type(first_name))

last_name = 'shinde'
print(type(last_name))

middle_name = ''' shirish'''
print(type(middle_name))

info = '''I am learning python'''
print(type(info))
print(info)

# slicing ==> string store index values (start value:end value-1:step size)

city = 'pune'

# 0  1  2  3
# p  u  n  e

print(city[0])
print(city[1])
print(city[2])
print(city[3])

city2 = 'chandrapur'

# 0   1   2   3   4   5   6   7   8   9
# c   h   a   n   d   r   a   p   u   r
# -10 -9  -8  -7  -6  -5  -4  -3  -2  -1

# string = [start index : end index-1 : step size]

e = city2[5::]
e2 = city2[-7::]
e3 = city2[1:7:]
e4 = city2[1:-2:]
e5 = city2[-7:-2:]
e6 = city2[-7:9:]
e7 = city2[0:10:3]
e8 = city[::-1]
e9 = city2[-1:-4:]
# e9 will return blank string negative reverse
e10 = city2[::]

print(e10)

#  methods of string 
# capitalize()

city = "nagpur"
x = city.capitalize()
# 1st letter capital
print(x)

# upper()
x3 = city.upper()
print(x3)

# casefold()
city2 = "NASHIK"
x2= city2.casefold()
print(x2)

# lower()
city4 = "NASHIK"
x4 = city4.lower()
print(x4)

# count()
city5 = 'chandrapur'
x5 = city5.count('a')
print(x5)




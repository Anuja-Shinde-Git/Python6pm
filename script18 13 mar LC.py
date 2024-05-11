# List Comprehension
# [expression : loop : condition]

# program 1

# calculate age
lst = [1989,1990,1991,1992]
age = []
for i in lst:
    age.append(2024-i)
print(age)

age = [2024-i for i in lst]
print(age)

# program 2
# calculate square
number = [1,2,3,4,5,6,7,8,9,10]
square = [i*i for i in number]
print(square)

# program 3
# separate out even numbers
even = [i for i in number if i %2 == 0]
print(even)

# program 4
# print type of number as even odd even odd
numType = ['even' if i %2 == 0 else 'odd' for i in number]
print(numType)

# program 5
# sort the names whose len > 5
names = ['sarika','mayuri','arti','aashish','sudhakar']
sortNames = [i for i in names if len(i)>5]
print(sortNames)
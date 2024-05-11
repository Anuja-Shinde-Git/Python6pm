# map , filter , reduce

# in these functions we have to use lambda function and mainly to get o/p as list we have to wrap the code in list data type
# 

# map = used where we want to perform a operation with each element
# filter = used where we want to sort/separate/filter elements with certain condition
# reduce = used where we want to combine a result in one single element

# map

# calculate age
# with for loop
lst = [1989,1990,1991,1992]
age = []
for i in lst:
    age.append(2024-i)
print(age)

# with list comprehension 

age =[2024-i for i in lst]
print(age)

# with map
# here we use lambda function and wrap in list to get o/p as list

age = list(map(lambda x:2024-x,lst))
print(age)

# f = lambda x :2024-x
# f(lst[0])
# print(f)

# Filter ==> 

# filter out the names whose len > 5

names = ["aniket","sanket","shivraj","swaraj","raj","sam"]

above5 =[]
for i in names:
    if len(i) > 5:
        above5.append(i)
print(above5)        

above5 = [i for i in names if len(i)>5]
print(above5)

# with Filter

above5 = list(filter(lambda x:len(x)>5,names))
print(above5)

# filter out deposite and withdral

d = [2,4,55,-78,-345,345,89,-532]
transaction = []

for i in d:
    if i > 0:
        # print("depostite")
        transaction.append("deposite")
    else:
        # print("withdral")    
        transaction.append("withdral")
print(transaction)        

transaction = ["deposite" if i > 0 else "withdral" for i in d]
print(transaction) 

# with Filter

deposite = list(filter(lambda x : x > 0, d))
print(deposite)

withdral = list(filter(lambda x : x < 0, d))
print(withdral)

# reduce is remaining




# external practice linkedIn question
d = {
    "milk":1,
    "soap":2,
    "towel":3
}
 
if 'soap'in d:
    print(d["soap"])
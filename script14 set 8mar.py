alpha = ("A","A","C","D")
print(alpha)
print(type(alpha))
print(len(alpha))
aaa = list(alpha)
print(aaa)

aaa.append("E")
print(aaa)
aaa=tuple(aaa)
print(aaa)

# program 1

h = "chinmay"
# h[0]= "a"  str will not support object assignment i.e we want to update character of string
print(h[0])

h = ["chinmay","deshpande"]
h[0] = "a"
print(h)
# get result as we update element of list

listA = [11,22,33,44,33]
print(listA)
# list will allow duplicate values

info = {
    "fname":"sai",
    "lname":"shinde",
    "age":23,
    "age":24
}
print(info)
# dict not allow duplicate value will print last updated value

print(info["fname"])

# SET

setA = {11,22,33,44}
print(type(setA))

setA = {11,22,33,33,44}
print(setA)
# set will not allow duplicate values
print(len(setA))


# store the value of index?? NO

# print(setA[0]) not store value by index

# loop = for loop

for i  in setA:
    print(i)


# methods of set
    
# add()
setC = {11,22,333,44,55,66}
setC.add(66)
print(setC)

# pop  will remove randmloy one element
setC.pop()
print(setC)

# remove()   will revome given value
setC.remove(55)
print(setC)

# union   will combine both the sets
setC={11,22,33,44}
setD={55,66,77}
print(setC.union(setD))





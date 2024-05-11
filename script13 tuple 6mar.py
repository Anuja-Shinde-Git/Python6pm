
strA = "amol"
print(strA)
print(type(strA))

names = ["sarika","amol","ashish"]
print(names)
print(type(names))

info = {
    "Fname" :"amol",
    "Lname" : "roa",
    "age" : 34,
    "city" : "pune"
}

print(info)
print(type(info))

# program B

flowers = ["lily","sunflower","rose"]
flowersB = ("lotus","rose","lily")

flowers[0] = "lotus"
print(flowers)

# flowersB [0] = "sunflower"
# print(flowersB)
# will through error as tuple dose not support item assignment i.e we cant change the tuple

# program C

# dose tuple store the values by index? ==> yes tuple stores the values by index
# how to define tuple

tupleA = ("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[0])

strA = "amol"
print(strA)
print(type(strA))

names = ["chinmay","sarika","rohit"]
print(names)
print(type(names))

info = {
    "firstName":"chinmay",
    "lastName":"deshpande"
}
print(info)
print(type(info))

# ---------------------------------------------->

# program B
flowers = ["lily","lotus","jasmine"]
flowerB  = ("lily","lotus","rose")
flowers[0] = "rose"
print(flowers)
#flowerB[1] = "sunflower"

# program C
#does  tuple stores the value by index??
# how to define tuple

tupleA = ("A","B","C")
print(tupleA)
print(type(tupleA))
print(tupleA[0])

# for with range
for x in range(3):
    #print(x)
    print(tupleA[x])

# for without range
for item in tupleA:
    print(item)

# while loop
i = 0 
while(i < 3):
    print(tupleA[i]) # A # B # C
    i = i + 1 # 1 # 2 # 3


# program D
tupleB = 12,23
print(type(tupleB))
#tupleB[0] = 88

tupleC  = (11,22,33)
a,b,c = tupleC
print(a)
print(b)
print(c)


# programE
tupleF = (11,22,33)
len(tupleF)
e = list(tupleF)
print(e)
e.append(44)
e = tuple(e)
print(e)

#program F
d = (11,22,33,44,44)
print(d)
e2 = d.count(44)
print(e2)

e3 = d.index(22)
print(e3)
print(33 in d)

# how to create tuple with constructor
e4 = ([11,22,33],[33,44,55],[55,66,77])

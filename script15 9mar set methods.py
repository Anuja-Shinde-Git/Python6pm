# union
setA = {11,22}
setB = {55,66,77}
print(setA.union(setB))

# intersection ==>  will return common element
setE = {11,33,44}
setF = {44,55,66}
setG = setE.intersection(setF)
print(setG)

# intersection_update ==> will update the set with common value
setE.intersection_update(setF)
print(setE)
setF.intersection_update(setE)
print(setF)

# program 2

# symmetric_difference ==> will retrun uncommon element
setQ = {11,22,33}
setE = {45,55,77,33}
setR = setQ.symmetric_difference(setE)
print(setR)

# symmetric_difference_update ==> will update set with uncommon elements

setQ.symmetric_difference_update(setE)
print(setQ)

# setE.symmetric_difference_update(setQ)
# print(setE)

# program 3
# difference ==> will return different value from other set
setQ = {11,22,33}
setE = {45,66,77,33}
setW = setQ.difference(setE)
print(setW)

# difference_update  ==>will update the set with different value from other set

# setQ.difference_update(setE)
# print(setQ)

setE.difference_update(setQ)
print(setE)

# program 4
# issubset ==> will return boolean value for all the element of set is present in other set true if not false
setQ = {11,22,33}
setE = {11,22,33,44}
q = setQ.issubset(setE)
print(q)

q2 = setE.issuperset(setQ)
print(q2)

# isdisjoint  will return TRUE if not one element will same ie all element should be different
setQ = {11,22,33,44,88}
setF = {55,66,77,88}
e = setQ.isdisjoint(setF)
print(e)

# program 5
# add() ==> add the element to the set

setW = {11,22,33,44}
setW.add(55)
print(setW)

# pop() ==> will remove element randomly
setW.pop()
print(setW)

# update() ==> will update the set with other set

setW.update({5,6,7,8})
print(setW)

# discard ==> will discard the given element if present if not present return none
setW = {11,22,33,44}
r = setW.discard(5)
print(r)
print(setW)

# clear() ==> will clear the set

setW.clear()
print(setW)
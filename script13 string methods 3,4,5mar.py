# 2 march 2024
# program 1
# upper()
first_name = "chinmay"
print(first_name)

e= first_name.upper()
print(e)

# lower()
last_name = 'Deshpande'
e2 = last_name.lower()
print(e2)

# isupper()
middle_name = 'SHIRISH'
e3= middle_name.isupper()
print(e3)

# islower()
e4=e2.islower
print(e4)

# program 2

# startswith()
city = 'pune'
e5= city.startswith('pu')
e6= city.startswith('P')
# case sensitive
print(e5)
print(e6)

# endswith()
e7 =city.endswith('e')
print(e7)
e8 = city.endswith('une')
print(e8)

city = 'chandrapur'
print(city)

# count()
e9=city.count('a')
print(e9)

# program 3

# len()
city3 = ' wardha'

e9 = len(city3)
print(e9)

# lstrip()
e10 = city3.lstrip()
print(e10)
print(len(e10))

# rstrip()
city4 = ' wardha '
print(len(city4))
e11 = city4.rstrip()
print(e11)
print(len(e11))

# strip()
city5 = ' wardha '
e12 = city5.strip()
print(e12)
print(len(e12))

# program 4
# replace()
info = "I am learning javascript"
e13 = info.replace('javascript','python')
print(e13)
print(info)

# program 5
# isdigit() 0-9
e14 = "123".isdigit()
print(e14)

# isalpha    a-z,A_Z
e15 = 'goa'
e16 = e15.isalpha()
print(e16)

e17 = 'goa1'
e18 = e17.isalpha()
print(e18)

# isalnum  0-9,a-z,A-Z
e19 = e17.isalnum()
print(e19)

e17 = 'goa'
e19 = e17.isalnum()
print(e19)

e17 = '123'
e19 = e17.isalnum()
print(e19)

e17 = '123#'
e19 = e17.isalnum()
print(e19)

# 4 march 2024

e18 ='hello'
e19 ='1234'
e20 = 'h123'
e21 ='h123#'
print(e18.isalpha())
print(e19.isalpha())
print(e19.isalnum())
print(e20.isalnum())
print(e21.isalnum())

# Revision

first_name = "Chinmay"
print(first_name.upper())
print(first_name.lower())
print(first_name.isupper())
print(first_name.islower())

first_name = " Chinmay "
print(len(first_name))
print(len(first_name.rstrip()))
print(len(first_name.lstrip()))
print(len(first_name.strip()))

# program 3

last_name = "Deshpande"
print(last_name.startswith('D'))
print(last_name.startswith('De'))
print(last_name.startswith('d'))

print(last_name.endswith('e'))
print(last_name.endswith('de'))
print(last_name.endswith('Nde'))

# program 4
marks = "123a"
print(marks.isdigit())
print(marks.isalpha())
print(marks.isalnum())


# program 5
# isspace()  blank string with only space will return true value
full_name = " "
print(full_name.isspace())

full_name = " a"
print(full_name.isspace())

# program 6 
# capitalize()  1st letter will capital
Fname = "chinmay"
e4 = Fname.capitalize()
print(e4)

# istitle() if 1st letter is capital will return true value
e4 = "Chinmay"
print(e4.istitle())

e4 = "Chinmay despande"
# each word should start with capital letter
print(e4.istitle())

e4 = "I Am Learning python"
# each word should start with capital letter
print(e4.istitle())

e4 = "I Am Learning Python"
# each word should start with capital letter
print(e4.istitle())

# program 7
# join ==> "-".join will return "-" separated value inplace of comma separated value
info = ["chinmay","despande","1234567789"]
e5 = "-".join(info)
print(e5)

# program 8
# split()
email = "avcd@gmail.com"
e6 = email.split('@')
# will return 'avcd','gmail' i.e splits at @
print(e6) 

# 5 march 2024

# find()  will return index of searched value

emailaddress = "Chinmay@gmail.com"
print(emailaddress.find("@"))

emailaddress = "Chinmay@gmail.@com"
print(emailaddress.find("@"))
print(emailaddress.find("@",8))
# will return next @ index as we put sencond argument as 8 i.e 1st @ is at 7 index so it will search form 8


# removeprefix()   will remove prefix

email2 = "gmail.com@chinamy"
email3 = "gmail.com@sham"
email4 = "gmail.com@samay"

#removeprefix()
email2 = "gmail.com@chinmay"
email3 = "gmail.com@sham"
email4 = "gmail.com@samay"

#print(email4.removeprefix('gmail.com@'))
# ["chinmay","sham","samay"]
students = [email2,email3,email4]
lista = []
for x in students:
  q1 = x.removeprefix("gmail.com@")
  lista.append(q1)
print(lista)

students = {
    "1":"chinmayadmin",
    "2":"poorvaceo",
    "3":"shamcustomer",
    "4":"nirnaymanager"
}

roles = ["admin","ceo","customer","manager"]
names = []
#names =["chinmay","poorva","sham","nirnay"] 
for name in students.values():
  for role in roles:
    if role in name:
      q2 = name.removesuffix(role)
      names.append(q2)
print(names)










# swapcase()   will change the case of the letters

a = 'hello'
print(a.swapcase())

a = 'hEllo'
print(a.swapcase())


# Zfill()   zero fill == will return fix lenght of element
# mainly used in file handling to read files
# want to make lenght of 10

name = 'chinmay'
name2= 'ninad'

print(name2.zfill(10))
print(name.zfill(10))
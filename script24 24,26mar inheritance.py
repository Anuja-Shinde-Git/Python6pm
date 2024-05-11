# Inheritance 
# single inheritance

class Father:
    def __init__(self,fn,ln):
        self.firstname = fn
        self.lastname = ln

    def displayName(self):
        print(self.firstname+self.lastname) 

class Son(Father):
    def __init__(self,fn,ln,sn):
     super().__init__(fn, ln)           
     self.sname = sn

    def displaySname(self):
       print(self.sname+self.lastname) 

sanket = Son("anil","shinde","sanket")

print(sanket.firstname)
print(sanket.lastname)
print(sanket.sname)

sanket.displayName()
sanket.displaySname()

# multi-level inheritance

class GrandFather:
   def __init__(self,fn,ln):
      self.firstname = fn
      self.lastname = ln

   def displayName(self):
      print(self.firstname+self.lastname)

class Father(GrandFather):
   def __init__(self, fn, ln,ffn):
      super().__init__(fn, ln)  
      self.Fname = ffn

   def displayFname(self):
      print(self.Fname+self.lastname)      

class Son(Father):
   def __init__(self, fn, ln, ffn,sn):
      super().__init__(fn, ln, ffn)
      self.sname = sn

   def displaySname(self):
      print(self.sname+self.lastname)  

sanket = Son("shankarrao","shinde","anil","sanket")

print(sanket.sname)
print(sanket.Fname)
print(sanket.firstname)
print(sanket.lastname)

sanket.displayName()
sanket.displayFname()
sanket.displaySname()

# hierarchical inheritance

class Mother:
   def __init__(self,fn,ln):
      self.firstname = fn
      self.lastname = ln

   def displayMname(self):
      print(self.firstname+self.lastname)

class Son(Mother):
   def __init__(self, fn, ln,sn):
      super().__init__(fn, ln)
      self.sname = sn

   def displaySname(self):
      print(self.sname+self.lastname)  

class Daughter(Mother):
   def __init__(self, fn, ln,dn):
      super().__init__(fn, ln)
      self.dname = dn

   def displayDname(self):
      print(self.dname+self.lastname)

sanket = Son("surekha","shinde0","sanket")

sai = Daughter("surekha","shinde","sai")

print(sanket.firstname)
print(sanket.lastname)
print(sanket.sname)

print(sai.firstname)
print(sai.lastname)
print(sai.dname) 

sanket.displayMname()
sanket.displaySname()

sai.displayDname()
sai.displayMname()

# multiple inheritance

class Mother:
   def __init__(self,fn,ln):
      print("Mother constructor called")
      self.firstname = fn
      self.lastname = ln

   def displayname(self):
      print(self.firstname+self.lastname)

class Father:
   def __init__(self,fn,ln):
      print("Father constructor called")
      self.firstname = fn
      self.lastname = ln

   def displayName(self):
      print(self.firstname+self.lastname)

class Son(Mother,Father):
   def __init__(self, fn, ln,sn):
       super().__init__(fn, ln)                  
       self.sname = sn

   def displaySname(self):
      print(self.sname+self.lastname)

sanket = Son("surekha","shinde","sanket")

sanket.displayName()
sanket.displaySname()


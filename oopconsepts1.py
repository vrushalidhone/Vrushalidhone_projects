#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Nilesh
#
# Created:     02/10/2024
# Copyright:   (c) Nilesh 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#oop concepts
#  multilevel inheritance
class A:
    def A(self):
        print("print A")
class B(A):
    def B(self):
        print("print b")
class C(B):
    def C(self):
        print("print c")
obj=C()
print(obj.A())
print(obj.B())
print(obj.C())
..........................................
........................................
....................
........
#  encapsulation
#get ,set method
class Student:
    def __init__(self):          #constructor
        self.name="hi ......."
        print(self.name)
    def getname(self):
        return self.name
    def setname(self,b):
        self.name=b
obj=Student()
obj.setname("vrushali")
name=obj.getname()
print(name)
...................................................
....................................
.............................
..................
# polymoiphisam
class ws:
    def displayin(self,name=""):
     print("vrudhsli"+name)
obj=ws()
obj.displayin()
obj.displayin("....v")    #....method o     verloding with diffrent parameter
..............................................................................
..........................................................
...........................
# polymoiphisam
class ws:

    def displayin(self):
     print("wc")
class IIP(ws):

    def displayin(self,name=""):
        super().displayin()
        print("IIP")

obj=IIP()
obj.displayin()

  #....method o     vriding with diffrent parameter
  #out put
  #ws IIP





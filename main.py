class Person:
 def __init__(self, name, age):
  self.name = name
  self.age = age
 def myfunc(self):
  print("Hello my name is " + self.name + "my age is" + self.age)
p1 = Person("Amr", 21)
p1.myfunc()


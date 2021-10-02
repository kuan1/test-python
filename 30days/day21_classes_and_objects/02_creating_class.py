# Creating a Class
class Person:
 pass

print(Person)

# Creating an Object
p = Person()
print(p)

# Class Constructor
class Person:
  def __init__(self, name = 'default-kuan'):
      self.name = name
  def info(self):
    return f'my name is {self.name}'

p = Person('kuan')
print(p.name)
print(p)
print(p.__dict__)
print(p.info())

p2 = Person()
print(p2.name)

# Inheritance
class Student(Person):
  def __init__(self, name='default-kuan'):
      super().__init__(name=name)
      self.skills = []
  
  def add_skill(self, skill):
      self.skills.append(skill)

student = Student('student')
student.add_skill('javascript')
student.add_skill('python')
print('student', student.skills)
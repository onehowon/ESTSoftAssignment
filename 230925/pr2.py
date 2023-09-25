class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    print(f'Hello World!, 제 이름은 [{self.name}]이고 제 나이는 [{self.age}]살 입니다.')

class Student(Person):
  def __init__(self, name, age, grade):
    Person.__init__(self, name, age)
    self.grade = grade


  def introduce(self):
    print(f'Hello World!, 제 이름은 [{self.name}]이고 제 나이는 [{self.age}]살입니다. 그리고 저는 [{self.grade}]학년입니다.')


고등학생 = Student('김창환', 18, 2)
고등학생.introduce()
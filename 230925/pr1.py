class Animal():
  def __init(self, name= ''):
    self.name = name
  def setName(self, name):
    self.name = name
    self.played =[]
  def playtogether(self, kinds):
    if kinds not in self.played:
      self.played.append(kinds)
      print(f'{self.name}과 함께 {kinds}를 시작합니다.')
    elif kinds in self.played:
      print("했던거라 지겨워 다른거 하자")

class Dog(Animal):

  def __init__(self):
    self.sound = '멍멍!'
  
  def make_sound(self):
    print(self.sound)

class Cat(Animal):

  def __init__(self):
    self.sound = '야옹!'

  def make_sound(self):
    print(self.sound)
    
dog = Dog()
dog.setName('땡글이')
cat = Cat()
cat.setName('참치')

print(dog.name, cat.name)
dog.make_sound()
cat.make_sound()
dog.playtogether('공놀이')
cat.playtogether('놀아주기')
dog.playtogether('공놀이')
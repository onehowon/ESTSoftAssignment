class Person:
		
		def work(self):
				print('열심히 일하자')


class Cook(Person):

		def __init__(self, menu):
				self.menu = menu
				print('주방장이 될꺼야!')
		
		def work(self):
				print(f'{self.menu}를 만들자')


class Developer(Person):
		
		def __init__(self, language):
				self.language = language
				print('CTO가 될꺼야!')

		def work(self):
				print(f'{self.language} 코드를 짜보자')

person = Person()
cook = Cook('피자')
developer = Developer('파이썬')

person.work()
cook.work()
developer.work()

class MultiPlyaer(Developer, Cook):
    pass

multiPlayer = MultiPlyaer('파이썬')
multiPlayer.work()
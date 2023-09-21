class MyIterator:
  def __init__(self, stop):
    self.stop = stop

  def __iter__(self):
    self.current_value = 0
    return self

  def __next__(self):
    if self.current_value >= self.stop:
      raise StopIteration
    result = self.current_value
    self.current_value += 1
    return result

my_iterator = MyIterator(5)

i = iter(my_iterator)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))

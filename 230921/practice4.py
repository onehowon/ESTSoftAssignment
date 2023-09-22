def fib(n):
  pre = 1
  next = 1
  for _ in range(n):
    yield pre
    temp = pre+next
    pre,next = next,temp

for i in fib(5):
  print(i)